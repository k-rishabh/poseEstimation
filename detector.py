import cv2
import time
import poseModule as pm
import mediapipe as mp
import argparse
import pyrealsense2 as rs

def main():
    pipe = rs.pipeline()
    cfg = rs.config() # Build config object and request pose data
    cfg.enable_stream(rs.stream.pose)
    pipe.start(cfg) # Start streaming with requested config

    pTime = 0
    cap = cv2.VideoCapture()
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
        cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3 (255, 0, 0), 3) #display FPS

        cv2.imshow("video", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()