
#5.Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
mygen = (x for x in range(n, 0, -1))
for i in range(n):
    print(next(mygen))
    