
from PIL import Image
import glob

images_path='C:/Users/Darvis/Desktop/source/image1.jpeg'
imag = Image.open(images_path)
print('{}'.format(imag.format))
print('size {}'.format(imag.size))
print('image mode:{}'.format(imag.mode))
imag.show()

#empty lists
image_list = []
resized_list = []

#append images to the list
for filename in glob.glob('C:/Users/Darvis/Desktop/source/*.jpeg'):
	print(filename)
	img=Image.open(filename)
	image_list.append(img)