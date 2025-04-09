# YOLO Object Detection and Tracking 

## 📌 Overview
This project implements **real-time object detection and tracking** using the **YOLOv8 model** . The program processes a video file, detects objects, tracks them across frames, and generates an output video with annotated object IDs.

## 🎯 Features
✅ **YOLOv8 Object Detection** – Detects objects in each frame of the video.  
✅ **Unique Object Identification** – Assigns and maintains consistent object IDs.  
✅ **Slowed-Down Playback** – Reduces video speed for better visualization.  
✅ **Final Object Summary** – Displays detected objects for 10 seconds at the end of the video.  

## 📂 Project Structure
```
📁 project-directory/
│── detector.py  # Main script for object detection & tracking
│── requirements.txt          # List of dependencies
│── README.md                 # Project documentation
│── input_video.mp4           # Sample input video (replace with your own)
│── output_video.mp4          # Processed video with detected & tracked objects
```

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AmirrezaSoltani/object-detector.git
   cd object-detector
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLO Weights** (optional, if not installed automatically)
   ```bash
   from ultralytics import YOLO
   YOLO("yolov11n.pt")
   ```

## 🏃‍♂️ Usage
1. **Run the Object Detection & Tracking Script:**
   ```bash
   python yolo_kalman_tracking.py
   ```
2. The script will:
   - Load `input_video.mp4`
   - Detect and track objects across frames
   - Display real-time video output with tracked object IDs
   - Save processed video as `output_video.mp4`
   - Print a list of unique detected objects

## 🎥 Example Output
- **Detected Objects:**
  ```
  ['couch', 'boat', 'traffic light', 'car', 'keyboard', 'microwave',
   'person', 'cell phone', 'potted plant', 'cake', 'laptop', 'bench',
   'bed', 'oven', 'umbrella', 'clock', 'chair', 'tv', 'dining table', 'toilet']
  ```
- **Final 10-second screen with detected object names.**

## 🔧 Possible Enhancements
🔹 Implement **DeepSORT** for even better tracking accuracy.  
🔹 Support **live webcam detection** instead of a video file.  

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to **fork this repo** and submit a pull request if you'd like to improve the code!

---

🚀 **Now, you can easily detect and track objects across video frames!**😊
