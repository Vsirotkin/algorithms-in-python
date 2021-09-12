import collections
div_line = ('*' * 50)
num_company = int(input('Введите количество компаний: '))

name_company = {input(f'Введите название {i} компании: '):
                    int(sum([int(input(f'Введите прибыль компании {i} для {j} квартала: ')) for j in range(1, 5)])/4)
                for i in range(1, num_company + 1)}
name_company = collections.OrderedDict(sorted(name_company.items(), key=lambda x: x[1]))

average = 0
for company_name in name_company:
    average += name_company[company_name]
average = int(average/len(name_company))

print(div_line)
print(f'Название компаний и их средняя прибыль за год: ')
print(*list(f'{company_name}: {name_company[company_name]}$, ' for company_name in name_company))
print(div_line)

print(f'Средняя прибыль всех компаний за год = {average}$')
print(div_line)

print('\nКомпании, чья прибыль больше средней(по всем предприятиям) за год: ', end='')
print(*list(f'{company_name}: {name_company[company_name]}$'
            for company_name in name_company if name_company[company_name] > average), sep=', ')
print(div_line)

print('Компании, чья прибыль ниже средней(по всем предприятиям) за год: ', end='')
print(*list(f'{company_name}: {name_company[company_name]}$'
            for company_name in name_company if name_company[company_name] < average), sep=', ')
print(div_line)
