import cv2
import os
from PIL import Image 


os.chdir(".//roseimages")
#chdir means change directory it tells computer that the computer should be in this folder 
path = ".//roseimages"


mean_width = 0
mean_height = 0

num_of_images = len(os.listdir('.'))
#listdir is a function to give all the files and folders that exist in the directory - telling computer to go to current directory and list all the folders in the folder
# . the dot takes it back to roses bit

for i in os.listdir("."):
    if i.endswith('.png') or i.endswith(".jpg")or i.endswith(".jpeg"):
        img = Image.open(os.path.join(i))
        width,height = img.size
        #img is the variable where you are loading the image , the size is a property that will provide us the width and height
        mean_width += width
        mean_height += height

mean_height //= num_of_images
mean_width //= num_of_images
# width and height of all the images should be the same
print(mean_width,mean_height)

for i in os.listdir('.'):   
    if i.endswith('.png') or i.endswith('.jpg')or i.endswith('.jpeg'):
        img = Image.open(os.path.join(i))
        img_resized = img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
        img_resized.save(i,'JPEG',quality=96)
        print(img_resized.size)
    # LANCZOS is used when you resize , your specifying the resizing  ( it specifies the resizing)


def videoGenerator():
    video_name = "rosesvideo.avi"
    os.chdir("C:\\Study\\coding - jetlearn\\advanced python\\open cv\\homework\\class 7 homework - roses\\roseimages")
    # os.chdir("C:\\Study\\coding - jetlearn\\advanced python\\open cv\\class7\\family")
    print(os.listdir("."))
    roses = []


    for i in os.listdir("."):   
        if i.endswith('.png') or i.endswith('.jpg')or i.endswith('.jpeg'):
            roses.append(i)
    print("list:" , roses)


    frame = cv2.imread(os.path.join(".",roses[0]))
    height,width,layers = frame.shape
    #shape is a property for an image  which gives us the height width and layers
    # the dot represents the folder , we are taking the folder and joining it to the images one by one s roses [0]is the first image
    #we are joining the name of the image file

    video = cv2.VideoWriter(video_name,0,1,(width,height))
    #the 0 is used for the format (fourcc is for formatting) 0 is for default
    # and 1 is used for frame per second which means 1 frame per second

    for image in roses:
        video.write(cv2.imread(os.path.join('.',image)))
# write is function to add your images to your videowriter
#imread is too read all the images video.release()
#video.write means writing the video
videoGenerator()
