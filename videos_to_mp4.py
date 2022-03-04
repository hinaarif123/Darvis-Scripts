import subprocess
import os

src = 'C:/Users/Darvis/Desktop/Database/Datasets/action_recognition/wibo_bed_cleaning/week_ending_18.02.22/ipad_footage/Session 2 - Allie Actor/Trimmed videos/Allie/clean_2_accessory_rails_under_lying_surface'
dst = 'C:/Users/Darvis/Desktop/Database/Datasets/action_recognition/wibo_bed_cleaning/week_ending_18.02.22/ipad_footage/Session 2 - Allie Actor/Trimmed videos/Allie'

for root, dirs, filenames in os.walk(src, topdown=False):
    #print(filenames)
    for filename in filenames:
        print('[INFO] 1',filename)
        try:
            _format = ''
            if ".flv" in filename.lower():
                _format=".flv"
            if ".mp4" in filename.lower():
                _format=".mp4"
            if ".avi" in filename.lower():
                _format=".avi"
            if ".mov" in filename.lower():
                _format=".mov"

            inputfile = os.path.join(root, filename)
            print('[INFO] 1',inputfile)
            outputfile = os.path.join(dst, filename.lower().replace(_format, ".mp4"))
            subprocess.call(['ffmpeg', '-i', inputfile, outputfile])  
        except:
            print("An exception occurred")