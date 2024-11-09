first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
oht = first_strings + second_strings
first_result = [len(x) for x in first_strings if len(x) >5]

b = (i for i in first_strings)
a = (y for y in second_strings)
second_result = [(i, y) for y in second_strings for i in first_strings if len(y) == len(i) ]

third_result = {x: len(x) for x in oht if len(x)%2==0}

print(first_result)
print(second_result)
print(third_result)