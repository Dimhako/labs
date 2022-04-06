import random
password = ''

simb = '!@#$%^&*()_=+-./\\:?,<>[]}{'
num = '1234567890'
alph = 'qwertyuioplkjhgfdsazxcvbnm'
ALPH = alph.upper()

pw = []
password = ''

r = input('Введите длину пароля: ')

print('''
1)Символы
2)Цифры
3)Строчные буквы
4)Заглавные буквы
''')
p = input('Выберите какие символы должны быть в пароле: ')

for i in range(len(p)):
    if p[i] == '1':
        pw.append(simb)
    if p[i] == '2':
        pw.append(num)
    if p[i] == '3':
        pw.append(alph)
    if p[i] == '4':
        pw.append(ALPH)

print(password)
print(pw)