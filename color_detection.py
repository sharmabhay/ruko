import cv2
import numpy as np
import pandas as pd
import argparse

# creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

# reading the image with opencv
img = cv2.imread(img_path)

# declaring global variables (used later on)
clicked = False
r = g = b = xpos = ypos = 0
clicked_img = (r, g, b)

# reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# function to calculate minimum Euclidean Distance from all colors and get the most matching color
def getMatchingColor(red, green, blue):
    minimum = float("inf")
    cname = "Color"
    for i in range(0, len(csv)):
        distance = np.sqrt((red - int(csv.loc[i, "R"])) ** 2 + (green - int(csv.loc[i, "G"])) ** 2 + (
                    blue - int(csv.loc[i, "B"])) ** 2)
        if distance < minimum:
            minimum = distance
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def drawFunction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        r = int(r)
        g = int(g)
        b = int(b)


cv2.namedWindow('image')
cv2.setMouseCallback('image', drawFunction)

while True:
    cv2.imshow("image", img)
    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # creating text string to display(Color name and RGB values)
        text = getMatchingColor(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # for very light colors, display text in black color
        if r + g + b >= 500:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # break the loop when user hits 'esc' or 'ctrl + c' key
    if cv2.waitKey(50) and 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
