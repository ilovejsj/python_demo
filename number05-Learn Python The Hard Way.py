name =  'Zed A. shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeh = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall. " % height
print "He's %d pounds heavy."% weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually &%s depending on the coffee." % teeh

#注释 balabala
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#手打代码都正确了

修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不只是你使用``=``赋值过的地方。
嗯 修改了

试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。
改成%r  还是一样的内容

在网上搜索所有的 Python 格式化字符。

%c	转换成字符（ASCII 码值，或者长度为一的字符串）
%r	优先用repr()函数进行字符串转换（Python2.0新增）
%s	优先用str()函数进行字符串转换
%d / %i	 转成有符号十进制数
%u	转成无符号十进制数
%o	转成无符号八进制数
%x / %X	(Unsigned)转成无符号十六进制数（x / X 代表转换后的十六进制字符的大
小写）
%e / %E	转成科学计数法（e / E控制输出e / E）
%f / %F	转成浮点数（小数部分自然截断）
%g / %G	%e和%f / %E和%F 的简写
%%	输出%

目前用的比较多的是%r  %s%d

试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。

公司怎么写一下子 忘记了。。不管了
