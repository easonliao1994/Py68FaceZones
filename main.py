import dlib
import cv2

img = dlib.load_rgb_image("res/lena.jpg")
img_cv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
 
detector = dlib.get_frontal_face_detector()
faces = detector(img)
 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
 
for face in faces:
    landmarks = predictor(img, face)
 
    print(f'landmarks: {landmarks.num_parts}')
    print(f'{landmarks.parts()}')
 
    for i in range(landmarks.num_parts):
        point = landmarks.part(i)
        cv2.circle(img_cv, (point.x, point.y), 2, (0, 0, 255), -1)  # Draw red dot

cv2.imwrite("res/lena_landmarks.jpg", img_cv)  # Save the image