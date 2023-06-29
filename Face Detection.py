#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import the necessary libraries
import numpy as np
import cv2 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Trying Face Detection for single face image..

# In[13]:


#  Loading the image to be tested
test_image = cv2.imread('C:\\Users\\kolli\\Downloads\\WhatsApp Image 2023-06-22 at 1.19.01 PM.jpeg')

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
haar_cascade_face = cv2.CascadeClassifier('C:/Users/kolli/anaconda3/ANACONDA/haarcascade_frontalface_alt2.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#convert image to RGB and show image
plt.imshow(convertToRGB(test_image))
def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        
    return image_copy


# ### Trying face detection for multiple face image..

# In[14]:


#  Loading the image to be tested
test_image = cv2.imread('C:\\Users\\kolli\\Downloads\\WhatsApp Image 2023-06-22 at 6.16.43 PM.jpeg')

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
haar_cascade_face = cv2.CascadeClassifier('C:/Users/kolli/anaconda3/ANACONDA/haarcascade_frontalface_alt2.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#convert image to RGB and show image
plt.imshow(convertToRGB(test_image))
def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        
    return image_copy


# ### Trying Face Detection for group image

# In[9]:


#  Loading the image to be tested
test_image = cv2.imread('C:\\Users\\kolli\\Downloads\\WhatsApp Image 2023-06-24 at 11.58.38 AM.jpeg')

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
haar_cascade_face = cv2.CascadeClassifier('C:/Users/kolli/anaconda3/ANACONDA/haarcascade_frontalface_alt2.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#convert image to RGB and show image
plt.imshow(convertToRGB(test_image))
def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        
    return image_copy


# In[ ]:




