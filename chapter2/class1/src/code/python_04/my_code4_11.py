'''
#将局部变量提升为全局变量

def zui():
    #提升局部变量为全局变量
    global mzj
    #定义局部变量mzj
    mzj = '麻醉剂'
    #在局部环境中调用mzj
    print('局部环境中调用变量',mzj)

#1.测试函数内部调用
zui()

#2.测是外部环境调用
print('在函数外部调用变量',mzj)
'''

