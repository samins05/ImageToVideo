import os
from PIL import Image
import cv2

current_path = os.getcwd()
img_dir = "images"

def get_average_dimension(folder):
    width = 0
    height = 0
    count = 0

    for img in os.listdir(folder):
        if img.endswith((".jpg", ".jpeg", ".png")):
            image = Image.open(os.path.join(folder, img))
            w,h = image.size
            width += w
            height +=h 
            count+=1

    width = width//count
    height = height//count
    return width,height

def resize_images(folder, width, height):
    for img_file in os.listdir(folder):
        if img_file.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(folder, img_file)
            img = Image.open(image_path)
            
            #resize image and save it with new dimensions
            resized_img = img.resize((width, height), Image.LANCZOS)
            resized_img.save(image_path, 'JPEG', quality=95)

def create_video(folder,name):
    video_filename = name+".mp4"
    img_arr = [i for i in os.listdir(folder) if i.endswith((".jpg", ".jpeg", ".png"))]

    first_img = cv2.imread(os.path.join(folder, img_arr[0]))
    h, w, z = first_img.shape # z is not used here 

    #create video writer object
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    
    #30 represents the fps
    vid_writer = cv2.VideoWriter(video_filename, codec, 30, (w, h))

    #iterate through image list and write them to the video
    for img in img_arr:
        loaded_img = cv2.imread(os.path.join(folder, img))
        for i in range(20):
            vid_writer.write(loaded_img)

    vid_writer.release()

create_video(img_dir,"story2")