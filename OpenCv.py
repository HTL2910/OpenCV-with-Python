import OpenCv
import cv2


def show_image(image):
    cv2.imshow('Original Image', image)

def crop_image(image):
    cropped_image = image[0:100, 0:100]
    cv2.imshow('Cropped Image', cropped_image)
def resize_image(image):
    resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Resized Image', resized_image)

if __name__=="__main__":
    image = cv2.imread('chessboard.png')
    show_image(image)
    crop_image(image)
    resize_image(image)
    cv2.waitKey(0)  # Wait until any key is pressed
    cv2.destroyAllWindows()