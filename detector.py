import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import time
import poseModule as pm
import mediapipe as mp

def main():
    pTime = 0
    cap = cv2.VideoCapture(2)
    detector = pm.PoseDetector()

    while(cap.isOpened()):
        success, img = cap.read()
        if success == False:
            break

        img, p_landmarks, p_connections = detector.findPose(img, False)        
        mp.solutions.drawing_utils.draw_landmarks(img, p_landmarks, p_connections) # draw points

        lmList = detector.getPosition(img)
        if(len(lmList) != 0):
            print(lmList) #prints (x, y) coordinates of all 33 BlazePose points

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        fps_int = int(fps)
        cv2.putText(img, str(fps_int), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3) #display FPS

        cv2.imshow("video", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()