import   cv2
image= cv2.imread(r"C:\Users\owais.khan\Pictures\img_small.png")
if image is None:
    print(' nothing no image ')
else:
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray_image
    blur= cv2.GaussianBlur(inverted, (21, 21),0)
    inverted_blur=255-blur
    sketch= cv2.divide(gray_image, inverted_blur, scale=256.0)
    cv2.imwrite("sketch_image.jpg",sketch)
    cv2.imshow("Sketch Image", sketch)
    cv2.waitkey(10)
    cv2.destroyAllWindows()
