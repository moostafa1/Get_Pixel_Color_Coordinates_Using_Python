import cv2

img_name = "baboon.jpg"
img = cv2.imread(img_name)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#y, x, _ = img.shape
# color = str(img[0:x, 0:y])
get_pixel_color = 0


def pixel_color(event, x, y, flags, param):
    global get_pixel_color, imgHSV

    colorsH = imgHSV[y,x,0]
    colorsS = imgHSV[y,x,1]
    colorsV = imgHSV[y,x,2]
    colors = imgHSV[y,x]

    c ='(' + str(colorsH) + ', ' + str(colorsS) + ', ' + str(colorsV) + ')'
    axis = '(' + str(x) + ', ' + str(y) + ')'
    print('\n')
    #print("Red: ",colorsR)
    #print("Green: ",colorsG)
    #print("Blue: ",colorsB)

    #print("BRG Format: ",colors)
    print("HSV Format: ", c)
    print("axis: ", axis)
    print("Coordinates of pixel: X: ",x,"Y: ",y)
    marker = '.'

    if event == cv2.EVENT_LBUTTONDOWN:
        get_pixel_color = 1
        img = cv2.imread(img_name)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #cv2.circle(img, (x,y), 3, (0,0,0), -1)

        cv2.putText(imgHSV, marker, (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
        cv2.putText(imgHSV, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)
        cv2.putText(imgHSV, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)


    elif event == cv2.EVENT_MOUSEMOVE:
        if get_pixel_color==1:
            img = cv2.imread(img_name)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            #cv2.circle(img, (x,y), 3, (0,0,0), -1)

            cv2.putText(imgHSV, marker, (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 3)
            cv2.putText(imgHSV, c, (20,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)
            cv2.putText(imgHSV, axis, (300,480),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)

    elif event==cv2.EVENT_LBUTTONUP:
        get_pixel_color = 0


cv2.namedWindow('Pixel Color')
cv2.setMouseCallback('Pixel Color',pixel_color)


while True:
    cv2.imshow("Pixel Color", imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

# print(img.shape)     # (512, 512, 3)
