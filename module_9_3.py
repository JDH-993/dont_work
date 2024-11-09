first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0])-len(x[1]) for x in zip(first, second) if len(x[0])>len(x[1]))
second_result = (True if len(first[i]) == len(second[k]) else False for i in range(len(first)) for k in range(len(second)) if i == k)

print(list(first_result))
print(list(second_result))