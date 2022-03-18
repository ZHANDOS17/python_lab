l = ['1', '2', '3', '4']

with open('/Users/zandosmirbaj/Desktop/Жандос', "w") as myfile:
    for i in l:
        myfile.write("%s\n" % i)

txt = open('/Users/zandosmirbaj/Desktop/Жандос')
print(txt.read())