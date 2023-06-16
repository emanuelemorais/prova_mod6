import cv2
import datetime
from ultralytics import YOLO

input_video = cv2.VideoCapture('./assets/arsene.mp4')


if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    

width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_name = "output_{}.mp4".format(current_time)
output_video = cv2.VideoWriter( output_file_name ,cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))

face_cascade = cv2.CascadeClassifier(filename=f"{cv2.data.haarcascades}/haarcascade_frontalface_default.xml")

while True:
   
    ret, frame = input_video.read()

    if not ret:
        break
    
    
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
    image=gray, 
    scaleFactor=1.05,
    minNeighbors=20 )
    x, y, w, h = faces[0]
    
    cv2.rectangle(
            img=frame,
            pt1=(x, y),
            pt2=(x+w, y+h),
            color=(0,0,255),
            thickness=3
            )

   
    cv2.imshow('Video Playback', frame)
    output_video.write(frame)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    

output_video.release()
input_video.release()
cv2.destroyAllWindows()