import os
from PIL import Image
import pytesseract
# # print(pytesseract.get_languages(config=''))


if __name__ == "__main__":
    root = r"C:\Users\郑尉欣\Desktop"
    for file in os.listdir(root):
        if file.startswith("tar"):
            print(pytesseract.image_to_string(Image.open(
                os.path.join(root, file)), lang='chi_sim+eng'))
