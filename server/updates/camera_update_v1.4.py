import cv2
import time

# Open default laptop camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open laptop camera.")
else:
    print("🎥 Laptop camera opened. Recording 5-second video (v1.4)...")

    # Get video properties
    fps = 20.0   # frames per second
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define codec and create VideoWriter object
    # Both of these work, depending on OpenCV version:
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # type: ignore

    out = cv2.VideoWriter("laptop_video_v1.4.avi", fourcc, fps, (frame_width, frame_height))

    start_time = time.time()
    while int(time.time() - start_time) < 5:  # Record for 5 seconds
        ret, frame = cap.read()
        if ret:
            out.write(frame)  # save frame to video
        else:
            print("❌ Failed to capture frame.")
            break

    # Release everything
    cap.release()
    out.release()
    print("✅ Saved laptop_video_v1.4.avi (5 sec video)")
