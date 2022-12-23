import cv2 
image = cv2.imread('elmalar.jpg')
originalResim=image.copy()
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
low_apple_red = (160,153,153)
high_apple_red = (180,255,255)
low_apple_raw = (0,150,150)
high_apple_raw = (15,255,255)
mask_red = cv2.inRange(image_hsv,low_apple_red,high_apple_red)
mask_raw = cv2.inRange(image_hsv,low_apple_raw,high_apple_raw)
mask = mask_red+mask_raw
cnts,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
number=0
for i,c in enumerate(cnts):
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if r>34:
        number+=1
        cv2.circle(image,(int(x),int(y)),int(r),(255,0,0),2)
        cv2.putText(image,"${}".format(number),(int(x)-10,int(y)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(200,0,0),2)
    else:continue
cv2.imshow("OriginalElma",originalResim)
cv2.imshow("CerceveliElma",image)
cv2.imshow("HSV Format",image_hsv)
cv2.imshow("MaskeliResim",mask)
cv2.waitKey(0)



