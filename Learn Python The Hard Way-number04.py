# -- coding: utf-8 --

#变量，命名

话说 这里真的手打会死人的- -

偷懒————
#这里全部赋值了，分别赋值成整型和浮点型
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
#cars= 100,drivers=30  实际计算  100-30

cars_driven = drivers
#drivers=30,cars_driven=drivers=30

carpool_capacity = cars_driven * space_in_a_car
cars_driven= 30  space_in_a_car=4.0

average_passengers_per_car = passengers / cars_driven
#相除，passengers 90 cars_driven  30


直接IDLE里运行，IDLE里有冒号的内容为字符串，没冒号的按赋值的内容输出

字符串可以使用下划线


习题:
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
————没有赋值或者命名


我在程序里用了 4.0 作为 space_in_a_car 的值，这样做有必要吗？如果只用 4 会有什么问题?
地板除还是什么来着，反正不会保留余数
记住 4.0 是一个“浮点数”，自己研究一下这是什么意思。
在每一个变量赋值的上一行加上一行注解。
记住 = 的名字是等于(equal)，它的作用是为东西取名。
记住 _ 是下划线字符(underscore)。
将 python 作为计算器运行起来，就跟以前一样，不过这一次在计算过程中使用变量名来做计算，常见的变量名有 i, x, j 等等。
