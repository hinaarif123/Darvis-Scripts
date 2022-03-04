#!/usr/bin/env python
# coding: utf-8

# In[19]:


from PIL import Image
import glob


# In[21]:


images_path='C:/Users/Darvis/Desktop/source/1641546185.8228047.jpg'
dest_path='C:/Users/Darvis/Desktop/source/shape'
imag = Image.open('C:/Users/Darvis/Desktop/source/1641546185.8228047.jpg')
print('{}'.format(imag.format))
print('size {}'.format(imag.size))
print('image mode:{}'.format(imag.mode))
imag.show()


# In[ ]:


#empty lists
image_list = []
resized_list = []


# In[27]:


#append images to the list
for filename in glob.glob('C:/Users/Darvis/Desktop/source/1641546185.8228047.jpg'):
    print(filename)
    img=Image.open(filename)
    image_list.append(img)


# In[22]:


for image in image_list:
    imag=image.resize((900,900))
    new_image=imag.save(dest_path)
    new_image.show()

    resized_list.append(image)


# In[28]:


#for(i,new) in enumerate(resized_list):
    #new.save('{}{}{}'.format('C:/Users/Darvis/Desktop/source/shape',i+1,'.jpeg'))


# In[ ]:




