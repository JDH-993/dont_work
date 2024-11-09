N = int(input())
x = 1
if bin(N)[2:].count('0') != 0:
    while bin(N+x)[2:].count('1') != bin(N)[2:].count('1'):
        x = x+1
    print(N+x)
else:
    f = '1' + bin(N)[2:]
    print(int(f, 2))

n = int(input())
a = bin(n)[2:]
if a.count('1') == 1:
    print(n*2)
elif a.count('1') == 0:
    a = '10'+a[1:]
    print(int(a, 2))
else:
    for i in range(n+1, 2**30):
        if bin(i)[2:].count('1') == a.count('1'):
            print(i)
            break