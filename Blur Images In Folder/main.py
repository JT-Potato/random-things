from PIL import ImageFilter, Image
import os

#Initial setup
path = input("Path of folder of images to blur: ")
#Iterate through each image in folder
for filename in os.listdir(path):
    if filename.endswith(".png"):
        print(os.path.join(path, filename)) #Our progress log (upgrade soon)
        image = Image.open(os.path.join(path, filename))
        
        image = image.filter(ImageFilter.GaussianBlur(1))
        image.save(os.path.join(path, filename))
        print("Image saved")