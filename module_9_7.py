def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        k = 0
        h = args[0] + args[1] + args[2]
        for i in range(1, h +1):
            if h % i >1:
                k = k +1
        if k == 2:
            print("Простое")
            return result
        else:
            print("Составное")
            return result
    return wrapper

@is_prime
def sum_three(*args):
    r = 0
    for i in args:
        r = r + i
    return str(r)



result = sum_three(2, 3, 6)
print(result)



