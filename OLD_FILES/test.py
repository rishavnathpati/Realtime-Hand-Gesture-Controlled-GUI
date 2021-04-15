import cv2

url = "http://192.168.136.209:8080/video"

cap = cv2.VideoCapture(url)
while True:
    flag, frame = cap.read()
    try:
        cv2.imshow('camera ip', frame)
    except:
        cap.release()
        raise

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()