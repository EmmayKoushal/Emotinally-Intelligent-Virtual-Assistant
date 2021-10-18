from deepface import DeepFace
import cv2
import face_recognition
import time

emotions = []
cap = cv2.VideoCapture(0)
i = 0
while (i < 5):
    isTrue, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    predictions = DeepFace.analyze(img)
    print(predictions['dominant_emotion'])
    faceLoc = face_recognition.face_locations(img)[0]
    cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)
    text = predictions['dominant_emotion']
    emotions.append(predictions['dominant_emotion'])
    font = cv2.FONT_HERSHEY_COMPLEX

    cv2.putText(img, text, (0, 50), font, 1, (0,0,255),2, cv2.LINE_4)
    cv2.imshow('pic',cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    i += 1
    # time.sleep(1)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break


cap.release()
cv2.destroyAllWindows()
