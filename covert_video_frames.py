import cv2
import time
import os
import moviepy
from moviepy.editor import *
import os
import natsort
from natsort import natsorted
import cv2
import time
count = 0
index = 0
step_size=20
video = cv2.VideoCapture("C:/Users/Darvis/Desktop/Database/Datasets/hanover/Camera 34/19-March/Combined Trimmed Video/Combined_Video.mp4")
output_folder="C:/Users/Darvis/Desktop/Database/Datasets/hanover/Camera 34/19-March/frames"
folder_file_count = 500
file_count = 0
folder_count = 1
path = output_folder
os.mkdir(path+str(folder_count)+"/")
path = path+str(folder_count)+"/"
prefix= time.time()
    # Loop through video frame by frame
while True:
      ret, frame = video.read()
      if not ret:
          break
        # Save every step_size frames
      if count % step_size == 0:
          cv2.imwrite(f'{path}/{time.time()}.jpg', frame)
          index += 1
          if file_count == folder_file_count:
                    file_count = 0
                    folder_count +=1
                    path_make = output_folder + '%s' % folder_count+'/'
                    os.mkdir(path_make)
                    path = path_make
          file_count +=1
      count += 1
video.release()
cv2.destroyAllWindows()