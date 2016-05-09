# -- coding: utf-8 --


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e


实际能运行，赋值类型也正确，
w+e  这里的+是拼接的意思，两个字符串类型相同，所以可以拼接
