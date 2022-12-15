  
import cv2
def nothing(x):
    pass

cv2.namedWindow( "result" )
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('minb', 'result', 0, 255, nothing)
cv2.createTrackbar('ming', 'result', 0, 255, nothing)
cv2.createTrackbar('minr', 'result', 0, 255, nothing)
cv2.createTrackbar('maxb', 'result', 0, 255, nothing)
cv2.createTrackbar('maxg', 'result', 0, 255, nothing)
cv2.createTrackbar('maxr', 'result', 0, 255, nothing)

while True:
    frame = cv2.imread('C:/edu/mod2/crossroads/images/0ea00dd4-cde9-420c-b02b-0db992b93de2.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    minb = cv2.getTrackbarPos('minb', 'result')
    ming = cv2.getTrackbarPos('ming', 'result')
    minr = cv2.getTrackbarPos('minr', 'result')
    maxb = cv2.getTrackbarPos('maxb', 'result')
    maxg = cv2.getTrackbarPos('maxg', 'result')
    maxr = cv2.getTrackbarPos('maxr', 'result')

   #Подбор значений
    mask = cv2.inRange(hsv,(minb,ming,minr),(maxb,maxg,maxr))
    #mask = cv2.inRange(hsv,(0,163,60),(255,255,255))

    cv2.imshow('mask', mask)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result1', result)
 
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
