# Live Object Detection & Tracking 🎥🔍

This project is built as **Task 3** for the **CodeAlpha Artificial Intelligence Internship**. 

It uses computer vision to capture live video from a webcam, identify objects in real-time, draw bounding boxes around them, and assign unique tracking IDs as they move across the frame.

## ✨ Innovative Features
* **Real-Time Processing:** Processes live webcam feeds instantly with minimal latency.
* **YOLOv8 Architecture:** Utilizes the state-of-the-art YOLOv8 model for highly accurate object detection.
* **Persistent Tracking:** Uses built-in tracking algorithms (BoT-SORT/ByteTrack) to assign memory and unique ID numbers to objects across consecutive frames.
* **Dynamic Annotation:** Automatically paints class labels, confidence scores, and tracking IDs directly onto the video feed.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Computer Vision:** OpenCV (`cv2`)
* **Machine Learning / AI:** Ultralytics (YOLOv8)

## 🚀 How to Run Locally

1. Clone the master repository and navigate to this specific task folder:
   ```bash
   cd CodeAlpha_Object_Tracker

2. Create and activate a Python Virtual Environment:
    python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required dependencies:
    pip install opencv-python ultralytics

4. Run the tracker (press 'q' to quit the video window):
   python tracker.py

   Developed by Hafsat Abdulhamid for the CodeAlpha Internship.    