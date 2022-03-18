with open('/Users/zandosmirbaj/Desktop/Жандос', "r") as ffile, open('C:\\Users\\Пользователь\\Documents\\test1.txt', "w") as sfile:
    for line in ffile:
        sfile.write(line)