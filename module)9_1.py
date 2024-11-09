def apply_all_func(int_list, *functions):
    results = {}
    for i in range(len(functions)):
        a = functions[i](int_list)
        results[functions[i].__name__] = a
    return results

#apply_all_func( )
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))