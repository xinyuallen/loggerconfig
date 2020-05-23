# author: yang time:2020/5/22.
#如何实现反射？
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def say(self):
#         print('<%s:%s>' %(self.name, self.age))
#
# obj = People('egon', 18)

#通过字符串来操作属性值
#实现反射机制的步骤   针对对象 ，对类也可以
#1.先通过dir: 查看出某一个对象下可以.出哪些属性来
# print(dir(obj))

#2.可以通过字符串反射到真正的属性上，得到属性值

#四个内置函数的使用 : 通过字符串来操作属性值
# hasattr() #判断属性是否存在
# print(hasattr(obj, 'name'))
# # getattr() #获取属性值
# print(getattr(obj, 'name'))
# # setattr() #设置属性值
# setattr(obj,'name', 'EGON')  #obj.name ='EGON'
# print(obj.name)
# # delattr()#删除属性值
# delattr(obj, 'name') #del obj.name
# print(obj, __dict__)
#
# #放类的函数的方法   绑定方法
# getattr(obj.,'say') #obj.Say
# getattr(People, 'say') #People.Say

# print(getattr(obj, 'x', None))  #没有想要的属性x就返回none
# obj = 10
# #别人写的程序给我一个obj，我得分析下obj里边有什么，能不能进行赋值操作,一眼看不出对象里有什么
# if hasattr(obj,'x'):
#      setattr(obj, 'x', 1111) # obj.x=11111
# else:
# #     pass
#
#
# class Ftp:
#     def put(self):
#         print('正在上传')
#
#     def __get__(self):
#         print('正在下载')
#
#     def interactive(self):
#
#         method= input(">>>>:").strip() # method = 'put'
#
#         if hasattr(self,method):
#             getattr(self,method)()
#         else:
#             print('输入的指令不存在')
#
# obj = Ftp()
# obj.interactive()
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):  #__str__:在打印对象时会自动触发，然后将返回值当作本次打印的结果
#         return "<%s:%s>" %(self.name, self.age)
#
# obj = People("aaaa",18)
# print(obj)
#
#
# #__del__: 在清理对象时会先执行
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.x = open('a.txt',mode='w')
#         #self.x占用的是操作系统资源
#
#      def __del__(self):
#          #发起系统调用，告诉操作系统回收相关的系统资源
#          self.x.close()
#
# obj = People("aaaa",18)
# print("==============")  #程序执行完后会清理对象，运行__del__

#引入

# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):  #__str__:在打印对象时会自动触发，然后将返回值当作本次打印的结果
#         return "<%s:%s>" %(self.name, self.age)
#
# #如何得到对象
# #obj=调用类（）
# #obj=people('egon',18)
#
# #如果说类也是对象
# #People = 调用类（。。。）
# #看内置的元类
# print(type(People))

# #类的三大特征
# 1.类名
# class_name="People"
# 2.类的基类
# class_bases=(object,)
# 3.执行类体代码拿到类的名称空间
# class_dic={}
# class_body="""
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# def say(self):
#     print('%s:%s' %(self.name,self.age))
# """
# exec(class_body,{},class_dic)
# #print(class_dic)
#
# #4.调用元类
# People=type(class_name,class_bases,class_dic)

#字定义元类来控制类的产生
# class Mymeta(type): #只有继承了type类的类才是元类
#     def __init__(self,x,y,z):
#         # print("run")
#         if not x.istitle():  #判断首字母是否大写
#             raise NameError('类名首字母必须大写！！')
# # 调用所在类，调用类时所传入的参数
#     def __new__(cls, *args, **kwargs):
#         #造Mymeta的对象
#         #print(cls,args,kwargs)
#         #return super().__new__(cls,*args, **kwargs)
#         return type.__new__(cls,*args, **kwargs)

#People=Mymeta(class_name,class_bases,class_dic)
#调用Mymeta发生三件事
#1.先造一个空对象=》People
#2.调用Mymeta这个类内的__init__方法，完成初始化对象的操作
#3.返回初始化好的对象
# class People(metaclass=Mymeta):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s:%s' %(self.name,self.age))

#强调
#只要是调用类，那么一定会一次调用
#1.类内的__new__
#2.类内的__init__


