import mymodule as mx
import platform #one of inbuilt modules in python
#from platform import system


mx.greeting("Bolat")
#we used module that was saved previously with .py expansion
#to use function from module we sould use syntax: module_name.function_name()


a = mx.person1["name"]
print(a)
#module can contain also variables


x = platform.system()
print(x)


x = dir(mx)
print(x)
#function to list all function names (or variable names) in the module.


