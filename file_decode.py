from sys import argv
import base64
import pyperclip
from cryptocode import decrypt, encrypt
import os


def file_decode(base64_file, file, password=None):

	if base64_file != '':

		with open(base64_file, "r") as f:
			extension = f.read(15).rstrip(' ')
			print(f.tell())
			text = f.read()

	else:
		extension = pyperclip.paste()[:15]
		text = pyperclip.paste()[15:]

	if password != None:
		text = decrypt(text, str(password))

	text = base64.b64decode(text)

	with open(file+extension, "wb") as out:
		out.write(text)

if __name__ == '__main__':

	if len(argv)>1:
		password = input('Password >')
		password = password if password != '' else None

		if not os.path.exists("./decoded/"):
			os.mkdir("./decoded/")

		for file in argv[1:]:

			file_decode(file, './decoded/' + os.path.basename(file).split('.')[0])

	else:

		file_decode(input('File to decode (or leave blank to parse from clipboard)>'), input('path to output file>'), input('password>'))
            
        
