# Benjamin Ramirez
# Reading through a directory of images and formatting them for input into conv net

import os
from PIL import Image
import numpy as np
import PIL
#  Image.resize(size, resample=0)
# iterating through directory files, answer by ghostdog74
# http://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python


# modelled after cv-tricks.com tutorial on training a classifier for cats and dogs,
# using PIL instead of OpenCV
def load_train_images(train_path, image_size, classes):
    images = []
    labels = []
    # ids = []
    # cls = []

    # begin reading the images from training path
    for folder in classes:
        index = classes.index(folder)
        path = os.path.join(train_path, folder+'/')
        print(path)
        image_files = get_images(path)

        for file in image_files:
            # load image file -> resize -> convert to greyscale
            image = Image.open(file)
            image = image.resize((image_size, image_size))
            image = image.convert(mode="L")
            images.append(image)
            # save the label as a one-hot vector corresponding to the class index
            label = np.zeros(len(classes))
            label[index] = 1.0
            labels.append(label)

    images = (np.array(image) for image in images)
    labels = np.array(labels)

    print(image for image in images)
    print(labels)

def get_images(path):
    image_files = []
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            image_files.append(os.path.join(path, file))
    return image_files

def add_flipped_images(images):
    new_images = images
    for x in range(len(images)):
        flipped_image = images[x].transpose(Image.FLIP_LEFT_RIGHT)
        print(flipped_image)
        new_images.append(flipped_image)
    return new_images

def add_top_bot_flip(images):
    new_images = images
    for x in range(len(images)):
        top_bot_flip_image = images[x].transpose(Image.FLIP_TOP_BOTTOM)
        print(top_bot_flip_image)
        new_images.append(top_bot_flip_image)
    return new_images

def save_images(images):
    for x in range(len(images)):
        # print(image.info)
        images[x].save("./images/grey/"+str(x)+".png", "PNG")

if __name__ == "__main__":
    image_directory = "./images"
    load_train_images(train_path=image_directory,
                      image_size=128,
                      classes=['stewie_griffin_GoogleSearch'])

