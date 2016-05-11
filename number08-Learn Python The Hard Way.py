# -- coding: utf-8 --

f = "%r %r %r %r"
print f % (1,2,3,4)
print f % ("one","two","three","four")
print f % (True,False,False,True)
print f %(f,f,f,f)
print f % ("I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")
    
    
#效果全部答应出来了

'''
习题：
手打代码，没有发生错误
对称引号不用转义，目前只了解这个情况
'''
