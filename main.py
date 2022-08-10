from tkinter import *
import easygui
from time import sleep
from file_decode import file_decode
from file_encode import file_encode
from functools import partial

root = Tk()
root.geometry("360x350+500+250")
root.resizable(width=False, height=False)
root.title("Base64 file encode/decode")


def file_select(var_to_save_path):

	var_to_save_path.set(easygui.fileopenbox())
	encode_status.set('')
	decode_status.set('')

def file_save(var_to_save_path):

	var_to_save_path.set(easygui.filesavebox())
	encode_status.set('')
	decode_status.set('')


def file_encode_gui():
	encode_status.set("Error!")
	file_encode(file_to_encode.get(), file_to_encode_out.get() if encode_out_option.get() != 'clipboard' else '', password_encode.get() if password_encode_checkbox.get() else None)
	encode_status.set("Done.")


def file_decode_gui():
	decode_status.set("Error!")
	file_decode(file_to_decode.get() if decode_in_option.get() != 'clipboard' else '' , file_to_decode_out.get() , password_decode.get() if password_decode_checkbox.get() else None)
	decode_status.set("Done.")


def hide(widget, row, column):
	
	if widget in root.grid_slaves():
		widget.grid_remove()

	else:
		widget.grid(row=row, column=column)


file_to_decode = StringVar()
file_to_decode.set("Pick a file to decode")

#encoding
Label(text='encoding', font='Arial 14').grid(row=0,column=0)

file_to_encode = StringVar()
file_to_encode.set("Pick a file to encode")
file_to_encode_out = StringVar()
file_to_encode_out.set("File to save")
encode_out_option = StringVar()
encode_out_option.set('file')

Entry(textvariable = file_to_encode, font="Arial 10", width=25).grid(row=1,column=0)

Button(text='Pick  file', command=partial(file_select, file_to_encode)).grid(row=1, column=1)

Entry(textvariable = file_to_encode_out, font="Arial 10", width=25).grid(row=2,column=0)

Button(text='Pick  file', command=partial(file_save, file_to_encode_out)).grid(row=2, column=1)

Radiobutton(text='File', variable=encode_out_option, value='file', command=partial(file_to_encode_out.set, "Pick a file to save")).grid(row=2,column=2)

Radiobutton(text='Clipboard', variable=encode_out_option, value='clipboard', command=partial(file_to_encode_out.set, "Copy base64 to clipboard")).grid(row=2,column=3)



password_encode_checkbox = BooleanVar()

password_encode = StringVar()

pass_encode_entry = Entry(textvariable = password_encode)

Checkbutton(text='encrypt with password', variable=password_encode_checkbox, onvalue=1, offvalue=0, command=partial(hide, pass_encode_entry, 4, 0)).grid(row=3,column=0)



Button(text='Encode file to base64', command=file_encode_gui).grid(row=5,column=0)

encode_status = StringVar()
encode_status.set('')

Label(textvariable = encode_status).grid(row=6,column=0)


#decoding
Label(text='decoding', font='Arial 14').grid(row=7,column=0)

file_to_decode = StringVar()
file_to_decode.set("Pick a file to get base64")
file_to_decode_out = StringVar()
file_to_decode_out.set("File to save")
decode_in_option = StringVar()
decode_in_option.set('file')

Entry(textvariable = file_to_decode, font="Arial 10", width=25).grid(row=8,column=0)

Button(text='Pick  file', command=partial(file_select, file_to_decode)).grid(row=8, column=1)

Entry(textvariable = file_to_decode_out, font="Arial 10", width=25).grid(row=9,column=0)

Button(text='Pick  file', command=partial(file_save, file_to_decode_out)).grid(row=9, column=1)

Radiobutton(text='File', variable=decode_in_option, value='file', command=partial(file_to_decode.set, "Pick a file to get base64")).grid(row=8,column=2)

Radiobutton(text='Clipboard', variable=decode_in_option, value='clipboard', command=partial(file_to_decode.set, "Get base64 from clipboard")).grid(row=8,column=3)



password_decode_checkbox = BooleanVar()

password_decode = StringVar()

pass_decode_entry = Entry(textvariable = password_decode)

Checkbutton(text='decrypt with password', variable=password_decode_checkbox, onvalue=1, offvalue=0, command=partial(hide, pass_decode_entry, 11, 0)).grid(row=10,column=0)



Button(text='Decode base64 to file', command=file_decode_gui).grid(row=12,column=0)

decode_status = StringVar()
decode_status.set('')

Label(textvariable = decode_status).grid(row=13,column=0)


if __name__ == '__main__':
	root.mainloop()

