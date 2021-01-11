import cv2
import time

video = cv2.VideoCapture(0)
first_frame = None


while True:
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 250, cv2.THRESH_BINARY)[1]
    thres_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (contours,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#    print(contours)
    for contour in contours:
        #print(cv2.contourArea(contour))
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, z) = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x,y), (x + w, z+y), (0, 255, 0), 3)

    cv2.imshow( 'Capturing', gray_frame)
    cv2.imshow('Difference', delta_frame)
    cv2.imshow('Threshold', thresh_frame)
    cv2.imshow('Detection', frame)
    key_pressed = cv2.waitKey(10)

    if key_pressed == ord('q'):
        break


cv2.destroyAllWindows()
video.release()
