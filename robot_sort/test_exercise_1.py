def f1(n):
    a = 0
    while (a < n * n * n):
      a = a + n * n
    return a

def f2(n):
    sum = 0
    c = 0
    for i in range(n): # O(n)
        i += 1
        c += 1
        for j in range(i + 1, n): # O(n)
            j += 1
            c += 1
            for k in range(j + 1, n): # O(n)
                k += 1
                c += 1
                for l in range(k + 1, n):
                    l += 1
                    c += 1
    print('c =', c)
    return sum

def f3():
    for i in range(10):
        print('i =', i)
        i += 2

def f4(n):
    for i in range(n):
        print('i =', i)
        for j in range(n):
            print('j =', j)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    print(bunnies)
    return 2 + bunnyEars(bunnies-1)

print('sum =', f2(1000))
# print(f3())
# print('sum =', f2(5)) O(n^3 + 10)
# print('sum =', f2(6)) O(n^3 + 4n)
# f4(5)
#****************************************************************************
# n = 100 -> n^2
    # 100^2 // 2 = 5000
    # 5000 - (100 // 2 - 1) = 4951
    # formula -> O(100^2 // 2 - ((100 // 2) - 1))

# n = 100 -> n^3
    # n^3 = 1,000,000 // 2 (do something and then...) // 2 (do same thing here??) = 166666
    # 9619
    # 166666 - (100 // 2 // 3 = 16) = 157047

# n = 100 -> O(n^3 (?) * (10 * (0.97xxxxxx))) -> 1525911
#****************************************************************************
# n = 1000 -> n^2
    # 1000^2 // 2 = 5000
    # 5000 - (1000 // 2 - 1) = 499501
    # formula -> O(1000^2 // 2 - ((1000 // 2) - 1))

# n = 1000 -> n^3
    # n^3 = 1,000,000 // 2 (do something and then...) // 2 (do same thing here??) = 166666
    # 9619
    # 166666 - (1000 // 2 // 3 = 16) = 165670497
#166666.66666666666666666666666667

# n = 1000 -> O(n^3 (?) * (10 * (0.97xxxxxx))) -> 1652209461