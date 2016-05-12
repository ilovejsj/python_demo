# -- coding: utf-8 --

'''
说下逗号的作用
1.逗号在参数传递中的使用：
参数之间的逗号

2.逗号在类型转化中的使用 主要是元组的转换（不理解）
3.逗号在输出语句print中的妙用:加了逗号之后 换行 就变成了 空格
'''

print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "how mach do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." %(age,height,weight)
    
习题：
1.input和raw_input都可以读取控制台的输入，input读取整数型,raw_input返回的是字符串，可以用type查看类型
2.
# -- coding: utf-8 --
b = (1,2)
print b


# -- coding: utf-8 --

print '6\'2"'
搞懂这个就可以了
