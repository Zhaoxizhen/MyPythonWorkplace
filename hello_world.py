from turtle import *
from string import Template
print("hello world!")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
print(r'C'+'\\')
input("press ENTER to continue")
tmpl = Template("hello, $name, good $time!")
str1 = tmpl.substitute(name=input("enter your name"), time="night")
print(str1)
input("press ENTER to continue")