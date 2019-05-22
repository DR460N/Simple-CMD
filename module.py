import os

def change_dir(i):
    os.chdir(i)

def list_dir():
    print(os.listdir())

def clear_screen():
    os.system('cls')

def make_dir(i):
    os.mkdir(i)

def remove_dir(i):
    os.rmdir(i)

def remove_file(i):
    os.remove(i)

def rename_file(i, j):
    os.rename(i, j)

def show_help():
    print('cd --> Change Directory')
    print('cls --> Clear Screen')
    print('dir --> Show Directory')
    print('listdir --> Show Directory List')
    print('mkdir --> Create a Directory')
    print('rmdir --> Remove a Directory')
    print('remove --> Remove File')
    print('rename --> Rename File Name')