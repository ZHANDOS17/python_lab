import os

p = '/Users/zandosmirbaj/Desktop/Жандос'

print("Only directories:")
print([name for name in os.listdir(p) if os.path.isdir(os.path.join(p, name))])
print("Only files:")
print([name for name in os.listdir(p) if not os.path.isdir(os.path.join(p, name))])
print("All directories and files :")
print([ name for name in os.listdir(p)])

#файлдын ышынде не бар соны шыгарп берелды
