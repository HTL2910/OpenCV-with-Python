
import cv2
import numpy as np
color=(200,100,200)

def show_image(image):
    cv2.imshow('Original Image', image)

def crop_image(image):
    cropped_image = image[0:100, 0:100]
    cv2.imshow('Cropped Image', cropped_image)
def resize_image(image):
    resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Resized Image', resized_image)
def draw(image):
    cv2.line(image,(100,50),(50,200),color=color)
    cv2.rectangle(image,(400,400),(500,500),color)
    cv2.circle(image,(500,500),50,color)

    cv2.imshow('draw',image)

def add_text(image):
    font=cv2.FONT_HERSHEY_COMPLEX
    font_scale=1
    text="Hi Python"
    cv2.putText(image,text,(500,500),font,font_scale,color,1)
    cv2.imshow('text image',image)

def rotate_image(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotate by 45 degrees
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    cv2.imshow('rotate',rotated_image)

def scaling_image(image):
    scaled_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('scale image',scaled_image)

def translate_image(image):
    (h, w) = image.shape[:2]
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])  # Translate by 50 pixels in x and y directions
    translated_image = cv2.warpAffine(image, translation_matrix, (w, h))
    cv2.imshow('translate image',translated_image)
if __name__=="__main__":
    image = cv2.imread('chessboard.png')
    # show_image(image)
    # crop_image(image)
    # resize_image(image)
    # draw(image)
    # add_text(image)
    # rotate_image(image)
    # scaling_image(image)

    # translate_image(image)
    
    cv2.waitKey(0)  # Wait until any key is pressed
    cv2.destroyAllWindows()