import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_contours(image, method):
    wyszarone = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if(method == 'roznica_pixeli'):
        zblurowane = cv2.GaussianBlur(wyszarone, (5, 5), 0)
        krawedzie = cv2.Canny(zblurowane, 30, 150)
        kontury, _ = cv2.findContours(krawedzie, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    elif(method == 'prog_gradientu'):
        grad_x = cv2.Sobel(wyszarone, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(wyszarone, cv2.CV_64F, 0, 1, ksize=3)
        gradient = cv2.magnitude(grad_x, grad_y)
        _, krawedzie = cv2.threshold(gradient, 30, 255, cv2.THRESH_BINARY)
        kontury, _ = cv2.findContours(krawedzie.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return kontury

def draw_contours(image, kontury):
    wynik = image.copy()
    cv2.drawContours(wynik, kontury, -1, (0, 255, 0), 2)
    return wynik

def present_photo(image_path):
    image = cv2.imread(image_path)
    kontury_pixele = find_contours(image, 'roznica_pixeli')
    kontury_gradient = find_contours(image, 'prog_gradientu')
    wynik_pixele = draw_contours(image, kontury_pixele)
    wynik_gradient = draw_contours(image, kontury_gradient)
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Origynalne')
    plt.subplot(1, 3, 2) 
    plt.imshow(cv2.cvtColor(wynik_pixele, cv2.COLOR_BGR2RGB))
    plt.title('Różnica pikseli')
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(wynik_gradient, cv2.COLOR_BGR2RGB))
    plt.title('Prog gradientu')
    plt.show()

images_paths = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg']
for image_path in images_paths:
    present_photo(image_path)