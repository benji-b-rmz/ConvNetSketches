# Benjamin Ramirez
# Reading through a directory of images and formatting them for input into conv net

import os
from os import listdir
from os.path import isfile,join

# iterating through directory files, answer by ghostdog74
# http://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
def get_images(dirname):
    image_files = []

    for file in os.listdir("./images/" + dirname):
        # print(file)
        if file.endswith(".jpg"):
            # print(os.path.join("./images/"+dirname, file))
            image_files.append(os.path.join("./images/"+dirname, file))

    return image_files


if __name__ == "__main__":
    image_directory = "stewie_griffin_GoogleSearch"
    print(get_images(image_directory))

