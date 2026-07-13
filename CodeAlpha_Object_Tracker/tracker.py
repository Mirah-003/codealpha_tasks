"""
Real-Time Object Detection & Multi-Object Tracking (MOT) Pipeline.
Utilizes state-of-the-art YOLOv8 architecture and ByteTrack/BoT-SORT algorithms via OpenCV.
"""
import argparse
import sys
import time
from typing import Optional, Union
import cv2
from ultralytics import YOLO


class RealTimeObjectTracker:
    """Orchestrates live video feed capture, YOLOv8 inference, bounding box overlay, and ID persistence."""

    def __init__(self, model_path: str = "yolov8n.pt", confidence: float = 0.5):
        """
        Initialize the object tracking pipeline.
        
        Args:
            model_path: Path or name of the YOLOv8 weights file (default: yolov8n.pt).
            confidence: Minimum confidence threshold for object detections.
        """
        self.model_path = model_path
        self.confidence = confidence
        try:
            self.model = YOLO(self.model_path)
        except Exception as e:
            print(f"Error initializing YOLOv8 model '{self.model_path}': {e}", file=sys.stderr)
            raise

    def run(self, source: Union[int, str] = 0, show_display: bool = True) -> None:
        """
        Executes real-time object tracking on webcam feed or video file.
        
        Args:
            source: Webcam device index (int, e.g., 0) or video file path (str).
            show_display: Whether to display the OpenCV window with bounding box overlay.
        """
        # Convert numeric strings to integers for camera indexing
        if isinstance(source, str) and source.isdigit():
            source = int(source)

        cap = cv2.VideoCapture(source)
        if not cap.isOpened():
            print(f"Error: Could not open video source: {source}", file=sys.stderr)
            return

        print(f"Tracking initiated on source: {source} | Press 'q' to terminate.")
        prev_time = time.time()

        try:
            while cap.isOpened():
                success, frame = cap.read()
                if not success:
                    print("End of video stream or failed to read frame.")
                    break

                # Calculate real-time Frames Per Second (FPS)
                current_time = time.time()
                fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
                prev_time = current_time

                # Execute tracking across consecutive frames (BoT-SORT / ByteTrack persistence)
                results = self.model.track(frame, persist=True, conf=self.confidence, verbose=False)
                annotated_frame = results[0].plot()

                # Overlay real-time FPS counter
                cv2.putText(
                    annotated_frame,
                    f"FPS: {int(fps)}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

                if show_display:
                    cv2.imshow("CodeAlpha Real-Time Object Tracker", annotated_frame)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        print("User terminated tracking session.")
                        break

        except KeyboardInterrupt:
            print("Tracking session interrupted by user.")
        finally:
            cap.release()
            if show_display:
                cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Real-Time YOLOv8 Object Detection & Tracking Pipeline")
    parser.add_argument("--source", default=0, help="Video source: camera index (0, 1) or path to video file (.mp4)")
    parser.add_argument("--model", default="yolov8n.pt", help="YOLOv8 model weights path (default: yolov8n.pt)")
    parser.add_argument("--conf", type=float, default=0.5, help="Confidence threshold (default: 0.5)")
    parser.add_argument("--no-display", action="store_true", help="Run in headless mode without GUI display")

    args = parser.parse_args()
    tracker = RealTimeObjectTracker(model_path=args.model, confidence=args.conf)
    tracker.run(source=args.source, show_display=not args.no_display)


if __name__ == "__main__":
    main()