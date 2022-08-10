from sys import argv
import base64
import pyperclip
from cryptocode import encrypt, decrypt
import os


def file_encode(file, base64_file, password=None):

    with open(file, "rb") as f:
        
        text = base64.b64encode(f.read()).decode('ascii')
        
        if password != None:
                text = encrypt(text, str(password))
        
    if base64_file != '':
        
       with open(base64_file, "w") as out:


            out.write('.' + os.path.basename(file).split('.')[1] + ' '*(15-len('.' + os.path.basename(file).split('.')[1])))    
            out.write(text)

    else:

        with open(file, "rb") as f:
            pyperclip.copy('.' + os.path.basename(file).split('.')[1] + ' '*(15-len('.' + os.path.basename(file).split('.')[1])) + text)

if __name__ == '__main__':

    if len(argv)>1:
        password = input('Password >')
        password = password if password != '' else None

        if not os.path.exists("./encoded/"):
            os.mkdir("./encoded/")

        for file in argv[1:]:

            file_encode(file, './encoded/' + os.path.basename(file).split('.')[0]+'.encoded')


    else:

        file_encode(input('File to encode>'), input('path to output file(or leave blank to parse from clipboard)>'))

