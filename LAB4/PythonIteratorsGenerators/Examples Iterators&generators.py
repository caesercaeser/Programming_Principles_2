mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#collections are iterable objects


mystring = "banana"
myit = iter(mystring)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#even string are iterable


mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
#cyclic iterator enumeration
#cycle creating iterator object and executes next() for every element of for
    

#to create iterable class we need to implement method __iter__(), which returns new object-itereator.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        #if x > 20:
        #    raise StopIteration
        #else:
            x = self.a
            self.a += 1
            return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#it never stops
print(next(myiter))


#Generators
#generator expressions returns iterator but not list
mygen = (x**2 for x in range(5))#this isn't a tuple but generator!

print(mygen)

print (next(mygen))
print (next(mygen))
print (next(mygen))
print (next(mygen))
print (next(mygen))



