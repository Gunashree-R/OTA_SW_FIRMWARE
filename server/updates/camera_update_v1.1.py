# Laptop Camera OTA Update Demo
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open laptop camera.")
else:
    print("📷 Laptop camera opened. Capturing image...")
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("laptop_image.jpg", frame)
        print("✅ Image captured and saved as laptop_image.jpg")
    else:
        print("❌ Failed to capture image.")

cap.release()
