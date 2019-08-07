import re

# 贪婪模式更多的去匹配
a = "aabbaa"
pat_greedy = r'a{1,2}'
pat_nog = r'a{1,2}?'
c = re.sub(pat_greedy, "gg", a)
c1 = re.sub(pat_nog, "gg", a)
print(c)
print(c1)


# sub(pattern,repl,string) repl是函数的情形
def dashrepl(matchobj):

    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'


c3 = re.sub('(-{1,2})', dashrepl, 'pro----gram-files')
#c4 = re.sub('-{1,2}?', dashrepl, 'pro----gram-files')
print("贪婪： ", c3)
#print("非贪婪： ", c4)


def sub_emphasis(match):
    return '<em>%s</em>' % match.group(1)
