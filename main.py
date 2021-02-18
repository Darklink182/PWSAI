import cv2

webcam = cv2.VideoCapture(0)

# Cascades
faceCascade = cv2.CascadeClassifier("humancascade.xml")
catCascace = cv2.CascadeClassifier("catcascade.xml")

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

    # Kijken voor katten in beeld
    cat = catCascace.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(75, 75)
    )

    # Tekenen
    for (i, (x, y, w, h)) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (220, 90, 230), 3)
        cv2.putText(frame, "Persoon - #{}".format(i + 1), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 90, 230), 2)

    for (i, (x, y, w, h)) in enumerate(cat):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, "Kat - #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # Resultaat
    cv2.imshow('Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Beeldend
webcam.release()
cv2.destroyAllWindows()
