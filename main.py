import dlib
 
img = dlib.load_rgb_image("res/lena.jpg")
 
detector = dlib.get_frontal_face_detector()
faces = detector(img)
 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
 
for face in faces:
    landmarks = predictor(img, face)
 
    print(f'landmarks: {landmarks.num_parts}')
    print(f'{landmarks.parts()}')
 
    # for part in landmarks.parts():
        # Todo draw points into image
