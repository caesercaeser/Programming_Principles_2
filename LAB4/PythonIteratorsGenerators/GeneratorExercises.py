# #1.Create a generator that generates the squares of numbers up to some number N.
# N = int(input())
# mygenerator = (x**2 for x in range(N))
# for x in range(N):
#     print(next(mygenerator))


# #2.Write a program using generator to print the even numbers between 0 and n in comma separated 
# #form where n is input from console.
# n = int(input())
# mygen = (x for x in range(n) if x % 2 == 0)
# for i in range(n//2):
#     if (i == n//2 - 1):
#         print(next(mygen), end=".")
#     else:
#         print(next(mygen), end=", ")


# #3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, 
# #between a given range 0 and n.
# n = int(input())
# mygen = (x for x in range(n) if (x % 3 == 0) and (x % 4 == 0))
# try:
#     while(True):
#         print(next(mygen))
# except StopIteration:
#     print()


# #4.Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it 
# #with a "for" loop and print each of the yielded values.
# a = int(input())
# b = int(input())
# squares = (x**2 for x in range(a, b+1))
# try:
#     while(True):
#         print(next(squares))
# except StopIteration:
#     print()


#5.Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
mygen = (x for x in range(n, 0, -1))
for i in range(n):
    print(next(mygen))
    