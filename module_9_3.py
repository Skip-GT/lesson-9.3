first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(s) for x, s in zip(first, second) if len(x) != len(s))

second_result = (len(first[y]) == len(second[y]) for y in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
