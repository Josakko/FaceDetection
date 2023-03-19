import cv2
import tkinter as tk
import PIL.Image, PIL.ImageTk


face_cascade = cv2.CascadeClassifier("detector.xml")

def detect_faces():

    video_capture = cv2.VideoCapture(0)

    root = tk.Tk()
    
    window_width = 700
    window_hight = 600
    
    monitor_width = root.winfo_screenwidth()
    monitor_hight = root.winfo_screenheight()
    
    x = (monitor_width / 2) - (window_width / 2)
    y = (monitor_hight / 2) - (window_hight / 2)

    root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
    root.title("JK Face Detector")
    root.iconbitmap("JK.ico")
    root.resizable(False, False)
    root.config(bg="#dbdbdb")
    
    def stop_capture():
        nonlocal video_capture
        video_capture.release()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", stop_capture)

    canvas = tk.Canvas(root, width=640, height=480, bg="black")
    canvas.pack(pady=15)

    faces_label = tk.Label(root, text="Faces Detected: 0", font=("Arial", 14), bg="#dbdbdb")
    faces_label.pack(pady=10)

    while True:

        ret, frame = video_capture.read()

        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        faces_label.config(text=f"Faces Detected: {len(faces)}")

        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        image = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        canvas_image = PIL.ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=canvas_image)

        root.update()
        
detect_faces()