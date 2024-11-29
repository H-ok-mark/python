#将数据输出文件中
#注意点:   1.所指定的地点   2.要使用file = 文件对象名称

# fp = open("D:/text.txt","a+") #a+的意义:文件不存在则创建,存在则追加
# print("hello world", file=fp)
# fp.close()
#
# #不进行换行输出(输出内容在一行中)
# print("hello","world","hello")

"""
文档的注释
"""

# print("ok")
#
# #\r将前面的内容进行了覆盖
# print('ok',"hello world\r","ok")
# print("no")

#原字符,不希望字符串中的转义字符起作用,使用原字符,就是在字符串之前加上一个r,或R
print("hello \n world")
print(r"hello \n world")
#注意事项:最后一个字符不能是\,但可以是\\
# print(r"hello \n world\")
print(r"hello \n world\\")

print(chr(0b100111001011000))
print(ord("乘"))

#输出关键字
import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
  'try', 'while', 'with', 'yield']
"""