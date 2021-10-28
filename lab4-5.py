

d = {i: {'surname': input('фамилия призывника: '), 'name': input('имя призывника: '), 'sekond_name': input('отчество призывника: '), 'birth_year': input('год рождения призывника: '), 'ill': input('болезни призывника: ')} for i in range(1, 3)}
# Создан словарь в котом пронумерованы словари,содержащи еинформацию о конкретном призывнике.
for i in range(1, len(d.keys()) + 1):
    print('{surname:10} {name:10} {sekond_name:12} {birth_year:5} {ill}'. format(**d[i]))
