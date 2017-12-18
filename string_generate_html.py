#!/usr/bin/python
'''Program to generate html ppage'''

title=input("Enter Title: ")
banner=input("Enter banner: ")
para1=input("Enter Paragraph one: ")
para2=input("Enter Paragraph otwo: ")
print("<html>")
print("  <head>")
print("      <title>")
print("\t\t",title)
print("      </title>")
print("  </head>")

print("<body>")
print("\t<h1>",banner,"</h1>\n")
print("\t<p>",para1,"\n\t</p>\n")
print("\t<p>",para2,"\n\t</p>")
print("</body>")
print("</html>")
