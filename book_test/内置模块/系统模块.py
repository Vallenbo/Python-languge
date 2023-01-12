import os

print(os.path)
print(os.getcwd())
print(os.listdir('E:\\Project\\Python\\book_test\\'))




x= os.path.basename('E:\Project\Python\book_test\内置模块')	#返回文件名

x= os.path.getsize('E:\\Project\\Python\\book_test\\test\\1.txt') #返回 path 的大小，以字节为单位
x= os.path.exists('E:\\Project\\Python\\book_test\\test')
print(x)


