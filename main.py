import cv2

webcam = cv2.VideoCapture(0)

# Cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret, frame = webcam.read()

    # Kleurschaal
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Kijken voor mensen in beeld
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    length = len(faces)

    print("{0} gezicht(en) in beeld".format(len(faces)))

    # Tekenen
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Resultaat
    cv2.imshow('Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Beeldend
webcam.release()
cv2.destroyAllWindows()
