import pytesseract
from os import listdir


def read_image(file_name):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_string(file_name)
    return data

directory = r'C:\Users\ADMIN\Pictures\temp'
files = listdir(directory)

print(files)
for i in files:
    if 'jpeg' in i.lower() or 'png' in i.lower():
        file_name = i
        image_path = directory+'\\'+file_name
        data = read_image(image_path)
        if 'google' in data.lower():
            print(image_path+':'+file_name.split('_')[0])
