import re
import sys
sys.path.append("C:\\Users\\MI\\IdeaProjects\\ParseTextToHtml\\Demo1")

from Demo1.util import *

print("<html><head><title>...</title><body>")
title =True
file="test_input.txt"
for block in blocks(open(file,encoding="UTF-8")):
    if title:
        print("<h1>")
        print(block)
        print("</h1>")
        title= False
    else:
        print("<p>")
        print(block)
        print("</p>")

print("</body></html>")


