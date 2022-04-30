import cv2

cam = cv2.VideoCapture(0)

while (True):
    red, cap = cam.read()
    cap = cv2.flip(cap, 1)
    cv2.imshow('membuka kamera',cap)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()



