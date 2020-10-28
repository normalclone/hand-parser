from config import handTrackConfig as htconf
from networks.hand_tracker import HandTracker

def models_init():
    HandDet = HandTracker(
    htconf.PALM_MODEL_PATH,
    htconf.LANDMARK_MODEL_PATH,
    htconf.ANCHORS_PATH,
    box_shift=0.2,
    box_enlarge=1.3)

    return HandDet