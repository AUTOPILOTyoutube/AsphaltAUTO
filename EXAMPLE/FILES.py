import os



#Каталог из которого будем брать файлы
directory = 'BUTTONS/CLOSE'

#Получаем список файлов в переменную files
files = os.listdir(directory)

for f in files:
    patch = str("'"+directory+'/'+f+"'")
    print(patch)