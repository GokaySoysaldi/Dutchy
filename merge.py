from os.path import join, dirname
from os import listdir, rmdir
from shutil import move
import os



parent_dict = "C:/Users/gokay/Desktop/sil"
create = "merged_train"
#TEST BRANCH22
path = join(parent_dict,create)


os.mkdir(path)

root = 'C:/Users/gokay/Desktop/sil/train'
dest = path
root_without_DS = lst_without_DS = [name for name in listdir(root) if not  name.startswith(".")]
root_without_DS.sort()

for i in range(1,10):
    os.mkdir(f'{dest}/00{i}')

for i in range(10,70):
    os.mkdir(f'{dest}/0{i}')


for sub in root_without_DS:
    if 'forg' in  sub:
        for filename in listdir(join(root, sub)):
            new_dest = f'{dest}/{sub.split("_")[0]}'
            fname = f'{filename.split(".")[0]}_F.png'
            print(fname)
            print(new_dest)
            move(join(root, sub, filename), join(new_dest, fname))
    else:
        lst_without_DS = [name for name in listdir(join(root, sub)) if not  name.startswith(".")]
        for filename in lst_without_DS:
            new_dest = f'{dest}/{sub}'
            fname = f'{filename.split(".")[0]}_G.png'
            print(fname)
            print(new_dest)
            move(join(root, sub, filename), join(new_dest, fname))

