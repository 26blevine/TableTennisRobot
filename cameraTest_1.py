import opencv as cv2

cap = cv2.VideoCapture(0)

frame = cap.read()

cv2.imshow("test", frame)
