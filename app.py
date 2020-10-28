import cv2
from utils.initialize_models import models_init
from utils import hand_track_utils as htutils
from utils.utils import gestures_map_to_behaviors, draw_keypoints

def main():
    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        hasFrame, frame = capture.read()
    else:
        hasFrame = False
    detector = models_init()
    while hasFrame:
        points, _ = detector(frame.copy())
        gesture = Noneq
        if points is not None:
            gesture = htutils.recog_gesture(points)
            synthesized_img = draw_keypoints(frame, points)
        synthesized_img = gestures_map_to_behaviors(frame, gesture)
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