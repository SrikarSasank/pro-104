import cv2

img = cv2.imread("solar-system.jpg")

planets = img[120:360,400:500]


sun = "Sun"
mercury = "Mercury"
venus = "Venus"
earth = "Earth"
mars = "Mars"
jupiter = "Jupiter"
saturn = "Saturn"
uranus = "Uranus"
neptune = "Neptune"

cv2.putText(img,  
           sun,
           (80, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=3,  
           color=(0,0,255)
           )

cv2.putText(img,  
           mercury,
           (120, 190),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           venus,
           (200, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           earth,
           (290, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           mars,
           (390, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           jupiter,
           (450, 100),
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           saturn,
           (800, 140), 
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           uranus,
           (970, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           neptune,
           (1120, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.imshow("output",img)
cv2.waitKey(0)
