import os

# 1.
'''
def read_end(lines, file):
    with open(file, 'r', encoding='utf-8') as f:
        listF = f.readlines()
    st = ''

    if lines < 0:
        return 'Количество линий должно быть положительным.'

    if not isinstance(lines, int):
        return 'Количество линий должно быть целым числом.'

    for i in range(len(listF) - lines, len(listF)):
        st += listF[i]
    return st

# Создание файла с текстом
with open('article.txt', 'w', encoding='utf-8') as f:
    lines = ['У лукоморья дуб зелёный;\n', 'Златая цепь на дубе том:\n', 'И днём и ночью кот учёный\n', 'Всё ходит по цепи кругом;\n', 'Идёт направо — песнь заводит,\n', 'Налево — сказку говорит.\n', 'Там чудеса: там леший бродит,\n', 'Русалка на ветвях сидит;\n', 'Там на неведомых дорожках\n', 'Следы невиданных зверей;\n', 'Избушка там на курьих ножках\n', 'Стоит без окон, без дверей;\n']
    f.writelines(lines)
    
print(read_end(4, 'article.txt'))
'''

# 2
'''
def print_reps(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            print('Каталог:', os.path.join(dirname))

        for filename in filenames:
            print('Файл:', os.path.join(filename))

# Создание директории которую будем выводить
if not os.path.isdir('folder1/folder2/folder3'):
    os.makedirs('folder1/folder2/folder3')

if not os.path.isdir('folder1/folder2/folder3/1.txt'):
    text_file = open('folder1/folder2/folder3/1.txt', 'w')

# используем функцию
print_reps('./folder1')
'''

# 3.
'''
def longest_word(file):
    with open(file, 'r', encoding='utf-8') as f:
        listF = f.readlines()
    maxL = 0
    listMax = []
    sepList = ':;,.-!?s'
    clearLs = []
    for sent in listF:
        st = ''
        for w in sent:
            if w not in sepList:
                st += w
        clearLs.append(st)
    for sent in clearLs:
        listSt = sent.split()
        for item in listSt:
            if maxL < len(item):
                maxL =  len(item)
                listMax = []
            if len(item) == maxL:
                listMax.append(item)
    return listMax


# Создание файла с текстом
with open('article.txt', 'w', encoding='utf-8') as f:
    lines = ['У лукоморья дуб зелёный;\n', 'Златая цепь на дубе том:\n', 'И днём и ночью кот учёный\n',
             'Всё ходит по цепи кругом;\n', 'Идёт направо — песнь заводит,\n', 'Налево — сказку говорит.\n',
             'Там чудеса: там леший бродит,\n', 'Русалка на ветвях сидит;\n', 'Там на неведомых дорожках\n',
             'Следы невиданных зверей;\n', 'Избушка там на курьих ножках\n', 'Стоит без окон, без дверей;\n']
    f.writelines(lines)

print(longest_word('article.txt'))
'''

# 4

with open('file.txt', 'w', encoding='utf-8') as f:
    lines = ['Beautiful is better than ugly.\n',
             'Explicit is better than implicit.\n',
             'Simple is better than complex.\n',
             'Complex is better than complicated.\n']
    f.writelines(lines)

with open('file.txt', 'r', encoding='utf-8') as file:
    file_text = file.read()

letter_count = 0

for char in file_text:
    if char.isalpha():
        letter_count += 1

words_count = len(file_text.split())

lines_count = len(file_text.splitlines())

print(f'Число букв латинского алфавита: {letter_count}')
print(f'Количество слов: {words_count}')
print(f'Количество строк: {lines_count}')


