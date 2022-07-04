import cv2
def click_event(event, x, y, flags, params):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX; fontSize = 2
        point = '.'; text = '  (' + str(x) + ', ' + str(y) + ')'
        color = (255, 0, 0); thickness=6

        cv2.putText(img, point, (x,y), font, fontSize, color, thickness)
        cv2.putText(img, text, (x,y), font, 0.5, color, 1)
        cv2.imshow('image', img)

    if event==cv2.EVENT_RBUTTONDOWN:
        img = cv2.imread('lena_color.tiff', 1)
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', click_event)


img_name = "baboon.jpg"
img = cv2.imread(img_name)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()
