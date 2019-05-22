from module import *
import os

while True:
    print(os.getcwd(), end = '> ')
    i = input()
    mylist = []
    mylist = list(map(str, i.split()))
    if mylist[0] == 'cls':
        clear_screen()
    elif mylist[0] =='cd' and mylist[1] != None:
        change_dir(mylist[1])
    elif mylist[0] == 'dir':
        list_dir()
    elif mylist[0] == 'mkdir' and mylist[1] != None:
        make_dir(mylist[1])
    elif mylist[0] == 'rmdir' and mylist[1] != None:
        remove_dir(mylist[1])
    elif mylist[0] =='help':
        show_help()
    elif mylist[0] == 'remove' and mylist[1] != None:
        remove_file(mylist[1])
    elif mylist[0] == 'rename' and mylist[1] != None and mylist[2] != None:
        rename_file(mylist[1], mylist[2])
    elif mylist[0] == 'exit':
        exit()
        break



