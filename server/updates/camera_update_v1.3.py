import cv2

cap = cv2.VideoCapture(0)  # 0 = default laptop camera

if not cap.isOpened():
    print("❌ Error: Could not open laptop camera.")
else:
    print("📷 Laptop camera opened. Capturing 3 normal images + 1 grayscale image...")

    # Capture 3 normal images
    for i in range(3):
        ret, frame = cap.read()
        if ret:
            filename = f"laptop_image_v1.3_{i+1}.jpg"
            cv2.imwrite(filename, frame)
            print(f"✅ Saved {filename}")
        else:
            print(f"❌ Failed to capture image {i+1}")

    # Capture 1 grayscale image
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("laptop_image_gray_v1.3.jpg", gray)
        print("✅ Saved laptop_image_gray_v1.3.jpg (grayscale)")
    else:
        print("❌ Failed to capture grayscale image.")
cap.release()
