import cv2
import time

video = cv2.VideoCapture(0)
first_frame = None


while True:
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if first_frame is None:
        first_frame = gray_frame

    cv2.imshow( 'Capturing', gray_frame)
    key_pressed = cv2.waitKey(10)

    if key_pressed == ord('q'):
        break


cv2.destroyAllWindows()
video.release()
