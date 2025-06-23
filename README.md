# hand-tracking
Real-time hand tracking using MediaPipe and OpenCV with landmark detection and FPS display

This project detects and tracks hands in real-time using MediaPipe's hand landmark model combined with OpenCV for video capture and rendering. It identifies key landmarks on the hand, highlights the thumb tips with circles, and draws a line between two thumbs if both hands are detected. The FPS (frames per second) is also displayed on the video feed.

## Reference Image

The file `MediaPipe Hands - Hand Landmark Model.png` is included in the repository for reference purposes only. It illustrates the landmark index IDs and their corresponding anatomical positions as defined by the MediaPipe Hands model. While it is not required for the functionality of the program, the image serves as a helpful visual guide for understanding which ID corresponds to which part of the hand, such as `WRIST`, `THUMB_TIP`, `INDEX_FINGER_MCP`, and so on.

## Dependencies

This project requires the following Python packages. It is recommended to install them in a virtual environment using the `requirements.txt` file included in the repository.
