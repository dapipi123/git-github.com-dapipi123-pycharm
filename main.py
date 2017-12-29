# -*- encoding: utf -8 -*-
# Mr.Wang

# print "Content-type:text/html \n\n"
# print "Hello Web Development"
import flask

import cgi,cgitb
from engine import *

form1=cgi.FieldStorage()
num1=form1.getvalue("Num1")
num2=form1.getvalue("Num2")
num3=None
if not num1 is None and not num2 is None:
    num1=int(num1)
    num2=int(num2)
    num3=num1+num2

# print "Content-type :text/html \n"
print start_response()
print start_div("center","margin-top:100px;")
print img("../views/add.png")
print end_div()

print start_div("center","margin-top:100px;")
print start_form()
print input_label("Num1","adder-1")
print "+"
print input_label("Num2","adder-2")
print "="
if num3 is None:
    print input_label("Num3","result","","readonly")
else:
    print input_label("Num3","result",str(num3),"readonly")
# print input_label("Num3","result","","readonly")
print end_form()
print end_div()