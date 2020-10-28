# hand-parser

## Introduction
This is an implementation of [mediapipe](https://github.com/google/mediapipe) in python and using finger state to predict hand gestures. You can read the detail about the approach used in this project in [here](https://github.com/Prasad9/Classify-HandGesturePose). The difference is that I don't handle the finger state by using a trained network, I just do some math calculating.
## Dependencies
`opencv-python >= 4.0`

`TensorFlow2.0(GPU is unnecessary)`

`PyTorch-GPU >= 1.1`

`Numpy`

`Pillow`
## Usage
1. Install required dependencies.
2. run `python app.py`
## Custom
- You can base on the points detected by `mediapipe` to predict or config the label

  e.g:  The `"CATCH"` label is predicted using the distance between the index and the thumb finger while the others using the angle to be predicted. 
  
- Read more in `utils/hand_track_utils.py` and the paper(https://github.com/Prasad9/Classify-HandGesturePose), you will make it clear soon.
## Demo
![Demo](demo.gif)
## License
`Apache License 2.0`
