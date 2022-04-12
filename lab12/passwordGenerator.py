import random
password = ''

simb = '!@#$%^&*()_=+-./\\:?,<>[]}{'
num = '1234567890'
alph = 'qwertyuioplkjhgfdsazxcvbnm'
ALPH = alph.upper()

pw = []
password = ''

r = int(input('Введите длину пароля: '))

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
        print('simb')
    if p[i] == '2':
        pw.append(num)
        print('num')
    if p[i] == '3':
        pw.append(alph)
        print('alph')
    if p[i] == '4':
        pw.append(ALPH)
        print('ALPH')

for i in range(r):
    pw1 = random.randint(0,len(pw)-1)
    pw2 = random.randint(0,len(pw[pw1])-1)
    password = password + pw[pw1][pw2]

print(password)
print(pw)