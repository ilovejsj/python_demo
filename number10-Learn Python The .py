# -- coding: utf-8 --

'''
比如你想说"I "understand" joe."，
Python 就会认为 "understand" 前后的两个引号是字符串的边界，
从而把字符串弄错。
所以需要转义
'''


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


"""
\t不知道什么作用，百度
上面这个手打的和教程里一样没错


其他转义：http://www.cnblogs.com/allenblogs/archive/2011/04/28/2031477.html
"""
"""
三个双引号和单引号一样
a = "hello %s " % ("\'word")
print a

瞎写

习题4不懂  20160512
"""
