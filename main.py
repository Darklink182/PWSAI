import cv2
import os

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Cascades
facecascade = cv2.CascadeClassifier("cascades/humancascade.xml")
catcascade = cv2.CascadeClassifier("cascades/catcascade.xml")

while True:
    d = input("\nTyp 1 voor webcam, 2 voor detectie van een foto\n> ")
    if d == "1":
        while True:

            ret, frame = webcam.read()

            # Kleurschaal
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Kijken voor mensen in beeld
            faces = facecascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Kijken voor katten in beeld
            cat = catcascade.detectMultiScale(
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
    if d == "2":
        arr = os.listdir('foto')
        print("Beschikbare bestanden:")

        for i in arr:
            print(f"- {i}")

        while True:
            y = input('\nWelke foto wilt u analyseren?\n> ')

            if y not in arr:
                if y == "bestanden":
                    for i in arr:
                        print(f"- {i}")

                if y != "bestanden":
                    print("Sorry, dit bestand kunnen we niet vinden in de foto map, zorg\nervoor dat de naam correct is, geen spaties bevat en dat u ook de\nextensie van het bestand heeft getypt.\nTyp 'bestanden' om elke beschikbare foto te zien")
                continue
            break

        frame = cv2.imread(f"foto\\{y}")

        scale_percent = 60  # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        faces = facecascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        cat = catcascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(75, 75)
        )

        for (i, (x, y, w, h)) in enumerate(faces):
            cv2.rectangle(resized, (x, y), (x + w, y + h), (220, 90, 230), 3)
            cv2.putText(resized, "Persoon - #{}".format(i + 1), (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 90, 230), 2)

        for (i, (x, y, w, h)) in enumerate(cat):
            cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(resized, "Kat - #{}".format(i + 1), (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

        cv2.imshow("Window", resized)
        cv2.waitKey(0)
    if d != "1":
        if d != "2":
            print("Dat is geen optie, probeer opnieuw\n")
            continue
