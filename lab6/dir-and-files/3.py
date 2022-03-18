import os.path

p = 'C:\\Users\\Пользователь\\Documents'
print(os.path.exists(p))
if os.path.exists(p):
    print(os.path.basename(p))
    print(os.path.dirname(p))

#Напишите программу на Python, чтобы проверить, существует ли заданный путь или нет. Если путь существует, найдите имя файла и часть каталога данного пути.