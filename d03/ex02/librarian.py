#! /usr/bin/python3
import os

def main():
    if (os.environ['VIRTUAL_ENV'].split('/')[-1] != 'nleyton'):
        raise Exception
    os.system('pip3 install -r requirements.txt')
    os.system("pip3 freeze > requirements.txt")
    os.system("cat requirements.txt")
    os.system("tar -c -f nleyton.tar nleyton")
if __name__ == '__main__':
    main()
