def myfunc():
    x = 300
    print(x)
myfunc()
#a variable created inside of a function is accessible only within of this function


myglobalvariable = 100
#A variable created in the main body of Python code is a global variable and refers to the global scope.
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
#a local variable can be accessed from a function witin a function.


x = 300
def myfunc():
  x = 200
  #python considering those as two diverse variables
  print(x)

myfunc()
print(x)



def myfunc():
  global x
  x = 300

myfunc()
print(x)
#The keyword makes the variable global.global


x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)