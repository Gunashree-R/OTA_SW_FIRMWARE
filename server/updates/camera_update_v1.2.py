import cv2

cap = cv2.VideoCapture(0)  # 0 = default laptop camera

if not cap.isOpened():
    print("❌ Error: Could not open laptop camera.")
else:
    print("📷 Laptop camera opened. Capturing 5 images...")
    for i in range(5):
        ret, frame = cap.read()
        if ret:
            filename = f"laptop_image_{i+1}.jpg"
            cv2.imwrite(filename, frame)
            print(f"✅ Saved {filename}")
        else:
            print(f"❌ Failed to capture image {i+1}")
cap.release()
