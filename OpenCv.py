import OpenCv
import cv2

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
if __name__=="__main__":
    image = cv2.imread('chessboard.png')
    # show_image(image)
    # crop_image(image)
    # resize_image(image)
    # draw(image)
    # add_text(image)

    
    cv2.waitKey(0)  # Wait until any key is pressed
    cv2.destroyAllWindows()