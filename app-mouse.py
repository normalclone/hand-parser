import cv2
from utils.initialize_models import models_init
from utils import hand_track_utils as htutils
from utils.utils import gestures_map_to_behaviors, draw_keypoints
from pynput.mouse import Controller, Button
from utils.hand_track_utils import *
mouse = Controller()
action_recog = []
def main():
    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        hasFrame, frame = capture.read()
    else:
        hasFrame = False
    detector = models_init()
    scale = 2.5
    while hasFrame:
        points, _ = detector(frame.copy())
        gesture = None
        if points is not None:
            gesture = htutils.recog_gesture(points)
            synthesized_img = draw_keypoints(frame, points)
            synthesized_img = gestures_map_to_behaviors(frame, gesture)

            action_recog.insert(0, [gesture, points])

            if len(action_recog) == 5:
                action_recog.pop(len(action_recog) - 1)
            if len(action_recog) > 1:
                mouse.move(action_recog[1][1][8][0] * scale - action_recog[0][1][8][0] * scale, action_recog[0][1][8][1] * scale - action_recog[1][1][8][1] * scale)
            if gesture == "2":
                mouse.click(Button.left, 1)


        if synthesized_img is None:
            break
        cv2.imshow("handTrack", synthesized_img)
        hasFrame, frame = capture.read()
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()