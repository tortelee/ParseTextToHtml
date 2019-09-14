class SuperHandler:
    def callfunc(self, prefix, name, *args):
        method = getattr(self, prefix+name)
        if callable(method): return method(*args)

    def start(self, name):
        self.callfunc('start_', name)

    def end(self, name):
        self.callfunc('end_', name)

    def sub(self, name):
        def substitution(match):
            method = self.callfunc('sub_', name, match)
            if method is None:return match.group(0)   #返回匹配部分
            return method     # 返回的是函数
        return substitution


class Handler(SuperHandler):
    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    @staticmethod
    def start_paragraph():
        print('<p>')

    @staticmethod
    def end_paragraph():
        print('</p>')

    @staticmethod
    def start_heading():
        print('<h2>')

    @staticmethod
    def end_heading():
        print('</h2>')

    @staticmethod
    def start_listitem():
        print('<li>')

    @staticmethod
    def end_listitem():
        print('</li>')

    @staticmethod
    def start_list():
        print('<ul>')

    @staticmethod
    def end_list():
        print('</ul>')

    @staticmethod
    def start_title():
        print('<h1>')

    @staticmethod
    def end_title():
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_hypertext(self, match):
        return '<a href=%s>%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return'<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))





import  re
if __name__=='__main__':
    h = Handler()
    h.start('paragraph')
    
    zz = re.sub(r'\*(.+?)\*', h.sub('emphasis'), 'This is *good*')
    print(zz)