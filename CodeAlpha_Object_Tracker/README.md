# 🎥 Real-Time YOLOv8 Object Detection & Tracking (`CodeAlpha Task 3`)

[![Ultralytics YOLOv8](https://img.shields.io/badge/YOLOv8-State__of__the__Art_Vision-0052FF?style=for-the-badge&logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

> **CodeAlpha Applied AI & Vision Internship Showcase**  
> A modular, real-time computer vision pipeline utilizing **YOLOv8** (`yolov8n.pt`) and **OpenCV** to perform instantaneous object detection and assign persistent Multi-Object Tracking (MOT) IDs across live video streams.

---

## 💡 The Engineering Problem & Solution

Standard object detection models independently process frames without memory, causing detected objects to flicker or change identification numbers (`Class 0 -> Person`) across every individual frame. This makes downstream spatial analytics (e.g., counting foot traffic, tracking vehicles across intersections) impossible without complex re-identification logic.

**Task 3 (`CodeAlpha_Object_Tracker`)** solves this by wrapping **Ultralytics YOLOv8** inside an object-oriented, persistent tracking pipeline (`RealTimeObjectTracker`). By activating built-in **ByteTrack / BoT-SORT** algorithms (`model.track(persist=True)`), the system assigns unique, permanent identification IDs (`ID: #1`, `ID: #2`) to moving objects while rendering live bounding boxes, class labels, and real-time **Frames Per Second (FPS)** overlays.

---

## 🏗️ Technical Highlights & Features

* **Modular Object-Oriented Architecture (`tracker.py`):** Encapsulated inside `RealTimeObjectTracker` with clean CLI argument parsing (`argparse`) to support dynamic switching between webcam device indices (`--source 0`), local MP4 video files (`--source highway.mp4`), and headless execution (`--no-display`).
* **Persistent MOT Tracking IDs:** Leverages memory-aware motion prediction (`persist=True`) to maintain object trajectory consistency across occlusions and high-speed motion.
* **Low-Latency FPS Telemetry:** Computes frame-to-frame delta timestamps (`1 / (current_time - prev_time)`) and paints green real-time FPS performance metrics directly onto the OpenCV video buffer.

---

## 🛠️ Tech Stack & Structure

```
CodeAlpha_Object_Tracker/
├── tracker.py            # Object-oriented YOLOv8 tracking class & CLI entrypoint
├── requirements.txt      # Minimal dependencies (ultralytics, opencv-python)
└── yolov8n.pt            # Pre-trained YOLOv8 Nano PyTorch weights (6.5 MB)
```

---

## 🚀 Local Quickstart & Usage

### 1. Setup Virtual Environment
```bash
cd CodeAlpha_Object_Tracker
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Live Webcam Tracking
```bash
python tracker.py --source 0 --conf 0.5
```
*(Press `q` inside the video window or `Ctrl+C` in the terminal to cleanly terminate the session).*

### 3. Track Objects from a Video File
```bash
python tracker.py --source /path/to/video.mp4 --conf 0.6
```

### 4. Run in Headless / Server Mode (No GUI Window)
```bash
python tracker.py --source /path/to/video.mp4 --no-display
```