import cv2

img_name = "baboon.jpg"
img = cv2.imread(img_name)

#y, x, _ = img.shape
# color = str(img[0:x, 0:y])
get_pixel_color = 0


def pixel_color(event, x, y, flags, param):
    global get_pixel_color, img

    colorsB = img[y,x,0]
    colorsG = img[y,x,1]
    colorsR = img[y,x,2]
    colors = img[y,x]

    c ='(' + str(colorsR) + ',' + str(colorsG) + ',' + str(colorsB) + ')'
    axis = '(' + str(x) + ',' + str(y) + ')'
    #print("Red: ",colorsR)
    #print("Green: ",colorsG)
    #print("Blue: ",colorsB)

    #print("BRG Format: ",colors)
    print("RGB Format: ", c)
    print("axis: ", axis)
    print("Coordinates of pixel: X: ",x,"Y: ",y)
    marker = '.'

    if event == cv2.EVENT_LBUTTONDOWN:
        get_pixel_color = 1
        img = cv2.imread(img_name)
        #cv2.circle(img, (x,y), 3, (0,0,0), -1)

        cv2.putText(img, marker, (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
        cv2.putText(img, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)
        cv2.putText(img, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)


    elif event == cv2.EVENT_MOUSEMOVE:
        if get_pixel_color==1:
            img = cv2.imread(img_name)
            #cv2.circle(img, (x,y), 3, (0,0,0), -1)

            cv2.putText(img, marker, (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
            cv2.putText(img, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)
            cv2.putText(img, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)

    elif event==cv2.EVENT_LBUTTONUP:
        get_pixel_color = 0


cv2.namedWindow('Pixel Color')
cv2.setMouseCallback('Pixel Color',pixel_color)


while True:
    cv2.imshow("Pixel Color", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

# print(img.shape)     # (512, 512, 3)
