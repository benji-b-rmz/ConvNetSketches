# Benjamin Ramirez
# Reading through a directory of images and formatting them for input into conv net

import os
from PIL import Image
import PIL
#  Image.resize(size, resample=0)
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

def resize_images(image_list, size=64):
    resized_images = []
    for image in image_list:
        img = Image.open(image)
        r_img = img.resize((size,size))
        resized_images.append(r_img)
    # print(resized_images)
    return resized_images

def image_to_greyscale(image_list):
    grey_images = []
    for image in image_list:
        grey_image = image.convert(mode="L")
        grey_images.append(grey_image)
    # print(grey_images)
    return grey_images

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
    image_directory = "stewie_griffin_GoogleSearch"
    save_images(add_top_bot_flip(add_flipped_images(image_to_greyscale(resize_images(get_images(image_directory))))))


