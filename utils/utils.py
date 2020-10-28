import numpy as np
import cv2

#        8   12  16  20
#        |   |   |   |
#        7   11  15  19
#    4   |   |   |   |
#    |   6   10  14  18
#    3   |   |   |   |
#    |   5---9---13--17
#    2    \         /
#     \    \       /
#      1    \     /
#       \    \   /
#        ------0-

hand_keymap=[
    [0,1], [1,2], [2,3], [3,4],
    [0,5], [5,6], [6,7], [7,8],
    [0,9], [9,10], [10,11], [11,12],
    [0,13], [13,14], [14,15], [15,16],
    [0,17], [17,18], [18,19], [19,20],
]

def is_last_for_gesture(gesture, recoders):
    leng = len(recoders)
    count = 0
    limit = 3
    if gesture == '5':
        limit = leng - 1
    for i in range(-1, -leng-1, -1):
        if recoders[i] == gesture:
            count += 1
    assert count >= 1
    if gesture == '5':
        if count > limit:
            return True
        if count == 1:
            return False
        else:
            return None

    if count == limit:
        return False
    elif count > limit:
        return True
    else:
        return None

def draw_keypoints(frame, points):
    for map in hand_keymap:
        from_point, to_point = map
        frame = cv2.line(frame, (int(points[from_point][0]), int(points[from_point][1])), (int(points[to_point][0]), int(points[to_point][1])), (255,255,255), thickness=3)
    for point in points:
        frame = cv2.circle(frame, (int(point[0]), int(point[1])), 5, color=(255,255,255))
    return frame


def gestures_map_to_behaviors(frame, gesture):
    if gesture == '1':
        text = '1'

    elif gesture == '2':
        text = '2'

    elif gesture == '3':
        text = '3'

    elif gesture == '4':
        text = '4'

    elif gesture == '5':
        text = '5'

    elif gesture == '8':
        text = 'POINT'

    elif gesture == 'OK':
        text = 'OK'

    elif gesture == 'GOOD':
        text = 'GOOD'

    elif gesture == 'CATCH':
        text = 'CATCH'

    else:
        text = 'NONE'


    height, width, channels = frame.shape
    frame = cv2.putText(frame, text, (5, height - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0,0,0), thickness=5)

    return frame