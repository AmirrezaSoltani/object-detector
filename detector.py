import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO("yolo11n.pt")  # Using yolo11n.pt for a larger model and better accuracy
# model = YOLO("yolo8n.pt")   

# Path to the video file
video_path = "IMG_7870.mp4"  
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

slow_factor = 1.1  #to slow down the video (2 means 2x slower)
new_fps = fps / slow_factor  

out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), new_fps, (frame_width, frame_height))

# Set to store unique objects
unique_objects = set()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)
    
    # Draw the detection results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            label = model.names[cls]
            unique_objects.add(label)
            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Write the frame to output video
    out.write(frame)
    
    # Display the frame
    cv2.imshow("SRH Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Convert set to list
unique_objects_list = list(unique_objects)


# Generate a final frame with detected objects
final_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8) 
text_y = 50  

cv2.putText(final_frame, "Detected Objects:", (50, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
text_y += 40

for obj in unique_objects_list:
    cv2.putText(final_frame, f"- {obj}", (50, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    text_y += 40

# Show this frame for 10 seconds (fps * 10 frames)
for _ in range(int(fps * 10)):
    out.write(final_frame)
    cv2.imshow("YOLO Object Detection", final_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Objects Detected:", unique_objects_list)

cap.release()
out.release()
cv2.destroyAllWindows()