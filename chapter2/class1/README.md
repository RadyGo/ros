# 2.1  Python入门

## 1. 变量

### 1. 1 什么是变量

变量就是可以改变的量，比如：

```python
# x+y = 10  
# x = 5  y = ? --->5
# x = 6  y = ? --->4

#那么这个x,y就是变量
```

变量的赋值：

```python
str1 = "有喜欢的人一定要表白~你丑没关系，万一她瞎呢？"
print(str1)
print(str1)
print(str1)
```

```python
#第二种赋值方式
str1 = str2 = -1000

print(str1,type(str1),id(str1))
print(str2,type(str2),id(str2))
```

变量的命名规范：

- 中文可以使用，但是python大神都不用
- 可以使用数字，但是数字不能在开头
-  变量名称只能使用数字、字母、下划线
- 可以使用下划线，但是下划线不能开头
- 严格区分大小写
- 变量名称要具有描述性
- 不能使用关键字当作变量名

## 2. 数据类型

python可以自定义数据类型，数据类型，默认的数据类型一共有六种

- Numbers           数字类型
- String                 字符串
- List                     列表
- set                      集合
- dict                     字典             
- Tuple                  元祖

### 2.1 Numbers 数字类型

- int 整数型

  ```python
  var = 1
  print(var)
  print(type(var))
  print(id(var))
  ```

- Float 浮点数

  ```python
  var = 3.141592654
  #科学记数法
  var1 = 3141592654e-9   #====>10的-9次方
  print(var,var1)
  print(type(var),type(var1))
  ```

- Complex 复数

  ```python
  #实数  5
  #虚数  i 一个数的平方等于-1
  
  var = 5 + 2j
  print(var)
  print(type(var))
  ```

- 布尔值

  ```python
  # True    表示肯定的语句
  # False   表示否定的语句
  
  if 5 > 3:
      print("有纹身的都怕热，镶金牙的爱咧嘴。")
  ```

### 2.2 String 字符串

声明字符串一共有三种方式：

- 第一种  单引号  变量 = '字符串内容'

  ```python
  str1 = '没有特殊的情况，不要去武汉.'
  print(str1,type(str1))
  ```

- 第二种  双引号  

  ```python
  str2 = "没有特殊的情况，不要去武汉."
  print(str2,type(str2))
  ```

- 第三种 三引号

  ```python
  str3 = """没有特殊的情况，不要去武汉."""
  print(str3,type(str3))
  ```

三种方法的使用：

```python
str1 = """ "钟南山的妈妈"说:"南山，你把这些钱拿给那位同学吧。" """
print(str1)
```

转义字符：

```python
转义字符  作用描述        使用率
\        续行符           *
\\       反斜杠符号(\)     ***
\'       单引号           *****
\"       双引号           *****
\a       响铃
\b       退格(backspace)
\e       转义
\000     空
\n       换行             *****
\v       纵向制表符
\t       横向制表符        *****
\r       回车             *****
\f       换页
\oyy     八进制数，yy代表的字符，例如：\o12代表换行
\xyy     十六进制数，yy代表的字符，例如：\x0a代表换行
\other   其它的字符以普通格式输出

```



---
## Copyright

![Logo](../../joint_logo.png)