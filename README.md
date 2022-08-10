# file-to-base64
Small gui programm to encode/decode any files to base64. Password encryption is optional.
![1](https://user-images.githubusercontent.com/110969821/183854202-1bfc92ff-18f2-4ff7-b4e3-22032499ac95.png)

**IMPORTANT NOTE:**
If you want to decrypt a file made in this program somewhere else then do not put a password on it and remove the first 15 bytes from the base64 file. They contain the file extension(I added this for ease of use).

**usage:**

go to the program dir

python -m pip install -r requirements.txt

python main.py

python file_encode.py "file1" "file2" "file3
"
will ask for password and create a ./encoded/ dir with file1.ecoded and file2.encoded

python file_decode.py "file1" "file2" "file3"

will ask for password and create a ./decoded/ dir with file1 and file2 with their file extensions that were before encoding

**build:**

pyinstaller --onefile --noconsole main.py


**features:** 

fast file encoding/decoding - drag and drop files to file_encode.py  / file_decode.py

copy encoded base64 string to clipboard (from gui or file_encode\decode.py with no args)

get base64 to decode from clipboard (from gui or file_encode\decode.py with no args)

password protect with cryptocode python module
