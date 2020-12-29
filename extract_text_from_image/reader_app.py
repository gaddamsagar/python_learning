#!"D:\Learning\py37venv\Scripts\python.exe"
import sys
import pytesseract
from os import listdir
from datetime import datetime

def read_image(file_name):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_string(file_name)
    return data

images_directory = sys.argv[1]
output_directory = sys.argv[2]
# print(directory)

files = listdir(images_directory)

time_now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
output_file = output_directory+'\out_'+time_now+'.txt'
with open(output_file, 'w') as output_writer:
    for i in files:
        if 'jpeg' in i.lower() or 'png' in i.lower() or 'jpg' in i.lower():
            file_name = i
            image_path = images_directory + '\\' + file_name
            data = read_image(image_path)
            if 'google' in data.lower():
                print(image_path+':'+file_name.split('_')[0])
                output_writer.write(image_path+':'+file_name.split('_')[0])


#usage : python reader_app.py <images_directory> <output_directory>