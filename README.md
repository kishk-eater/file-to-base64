# file-to-base64
Small gui programm to encode/decode any files to base64. Password encryption is optional.
![1](https://user-images.githubusercontent.com/110969821/183854202-1bfc92ff-18f2-4ff7-b4e3-22032499ac95.png)

usage:
go to the program dir

python -m pip install -r requirements.txt
python main.py

build:
pyinstaller --onefile --noconsole main.py


features: 

multiple file encoding/decoding - drag and drop files to file_encode.py / file_decode.py

copy encoded base64 string to clipboard (from gui)

get base64 to decode from clipboard (from gui)

password protect with cryptocode python module

IMPORTANT NOTE:
If you want to decrypt a file made in this program somewhere else then do not put a password on it and remove the first 15 bytes from the base64 file. They contain the file extension(I added this for ease of use).
