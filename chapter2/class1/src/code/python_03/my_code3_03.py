#书写几行代码
'''
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
print('一个小苹果')
'''
# 将输出一个小苹果的代码执行10次
'''
#死循环
while True:
    print('一个小苹果')
'''
#带有计数格式的循环
var = 0# （初始化变量）顺序结果
while var < 10:#判断条件
    print('一个小苹果')#循环代码
    var += 1#变量自增或者自减

'''
1.var = 0 初始化变量 (顺序结构)

#########第一次循环#############
2.while 判断 var < 10 -> True
3.执行了循环代码 
4.变量自增或者自减   -> var = 1

##########第二次循环################
5.while 判断 var < 10 -> True
6.执行了循环代码
7.变量自增或者自减代码 -> var =2

##########第三次循环#################
...


##########第四次循环#################
...

##########第五次循环#################
...


##########第六次循环#################
...


##########第七次循环#################
...


##########第八次循环#################
...


##########第九次循环################# var = 8
N while 判断 var < 10 -> True 
N+1 执行循环代码
N+2 变量自增或者自减代码 -> var = 9


##########第十次循环#################
N+3 while 判断var < 10 -> True
N+4 执行循环代码
N+5 变量自增或者自减代码 -> var = 10

#尝试第十一次操作
N+6 while 判断var < 10 -> False
N+7 停止循环操作
'''

#计算 1-20之间数字的和  包含20
#声明计数变量
var = 1
#声明求和变量
total = 0

while var <= 20:
    total = total + var#累计每一个数字
    #自增条件
    var += 1

#输出循环的结果（顺序结果）
print(total)

#实例：输出一个10行10列的小星星(循环中只能使用一个星星)
#print（） 操作自带换行
print('*',end = '') #取消print的换行
print('*',end = '')
print('*',end = '')
print('*',end = '')
print('*',end = '')
print()#输出一个换行
print('*',end = '')

