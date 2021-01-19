import cv2
import pandas
from datetime import datetime

df = pandas.DataFrame(columns = ['Start Time', 'End Time'])

video = cv2.VideoCapture(0)
first_frame = None
status_list = []
status_list.append(0)
times = []

while True:
    check, frame = video.read()
    status = 0

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
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, z) = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x,y), (x + w, z+y), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]
    
    if status_list[-1] != status_list [-2]:
        print('Change from status ' + str(status_list[-2]) + ' to status: ' + str(status_list[-1]) + ' at: ' + str(datetime.now()))
        times.append(datetime.now())

    cv2.imshow('Capturing', gray_frame)
    cv2.imshow('Difference', delta_frame)
    cv2.imshow('Threshold', thresh_frame)
    cv2.imshow('Detection', frame)
    key_pressed = cv2.waitKey(10)

    if key_pressed == ord('q'):
        if status == 1:
            print('End Time: ' + str((datetime.now())))
            times.append(datetime.now())
        break


print(status_list)
print(times)

for activity in range(0, len(times), 2):
    df = df.append({'Start Time':times[activity], 'End Time': times[activity+1]}, ignore_index = True)

df.to_csv('Times.csv')
cv2.destroyAllWindows()
video.release()
