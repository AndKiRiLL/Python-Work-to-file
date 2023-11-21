import os

#print(os.getcwd())

# if not os.path.isdir('folder'):
#     os.mkdir('folder')

# os.chdir('folder')
# print(os.getcwd())

# os.chdir('..')
# os.makedirs('folder1/folder2/folder3')

# создать новый текстовый файл
# text_file = open('text.txt', 'w')
# запись текста в этот файл
# text_file.write('Это текстовый файл')

# os.rename('text.txt', 'renamed-text.txt')

# os.replace('renamed-text.txt', 'folder/renamed-text.txt')

# os.remove('folder/renamed-text.txt')
# print('Все папки и файлы:', os.listdir())

'''
# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk('.'):
    # перебрать каталоги
    for dirname in dirnames:
        print('Каталог:', os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print('Файл:', os.path.join(dirpath, filename))
'''

#os.rmdir('folder')

# os.removedirs('folder1/folder2/folder3')
# open('text.txt', 'w').write('Это текстовый файл')

# вывести некоторые данные о файле
# print(os.stat('text.txt'))

# print('Размер файла:', os.stat('text.txt').st_size)

'''
f = open('text.txt')

for line in f:
    print(line)
'''

'''
l = [str(i)+str(i-1) for i in range(20)]
f = open('text.txt', 'w')

for index in l:
        print(f.write(index + '\n'))

f.close()
'''

'''
f = open('text.txt', 'r')
l = [line.strip() for line in f]
print(l)
f.close()
'''

'''
with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.read(6)
print(data)
'''

'''
with open('file.txt', 'r', encoding='utf-8') as f:
    print(f.readline())
'''

'''
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
'''

'''
with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
print(data)
'''

'''
with open('file.txt', 'r', encoding='utf-8') as f:
    data = list(f)
print(data)
'''

'''
with open('file.txt', 'a', encoding='utf-8') as f:
    data = 'Привет, Python!'
    f.write(data)
'''

'''
with open('file.txt', 'a', encoding='utf-8') as f:
    grocery = ['Морковь\n', 'Яблоки\n', 'Мука\n', 'Молоко\n']
    f.writelines(grocery)
'''

