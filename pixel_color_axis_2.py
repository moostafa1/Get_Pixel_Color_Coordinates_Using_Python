import cv2

get_pixel_color = 0

img_name = "baboon.jpg"
img = cv2.imread(img_name)


def mouseRGB(event,x,y,flags,param):
    global get_pixel_color, c, axis, img


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


    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        get_pixel_color = 1

        img = cv2.imread(img_name)
        cv2.putText(img, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
        cv2.putText(img, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)

    elif event == cv2.EVENT_MOUSEMOVE:
        if get_pixel_color == 1:
            img = cv2.imread(img_name)
            cv2.putText(img, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
            cv2.putText(img, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        get_pixel_color = 0


# Read an image, a window and bind the function to window

img = cv2.imread(img_name)
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#if esc pressed, finish.
cv2.destroyAllWindows()
