import dlib
import cv2
import numpy as np
import os

def check_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

def check_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_image(file_name):
    file_path = f"res/{file_name}.jpg"
    check_file(file_path)
    img = dlib.load_rgb_image(file_path)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

def detect_faces(img):
    detector = dlib.get_frontal_face_detector()
    return detector(img)

def get_landmarks(img, face):
    predictor_path = "shape_predictor_68_face_landmarks.dat"
    check_file(predictor_path)
    predictor = dlib.shape_predictor(predictor_path)
    return predictor(img, face)

def draw_landmarks(img, landmarks):
    for i in range(landmarks.num_parts):
        point = landmarks.part(i)
        cv2.circle(img, (point.x, point.y), 2, (0, 0, 255), -1)  # Draw red dot
        cv2.putText(img, str(i), (point.x, point.y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

def save_image(img, file_name):
    cv2.imwrite(f"res/result/{file_name}.jpg", img)  # Save the image


def cubic_bezier(P0, P1, P2, P3, t):
    """計算三次貝塞爾曲線上的一個點"""
    x = (1-t)**3 * P0[0] + 3*(1-t)**2 * t * P1[0] + 3*(1-t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1-t)**3 * P0[1] + 3*(1-t)**2 * t * P1[1] + 3*(1-t) * t**2 * P2[1] + t**3 * P3[1]
    return (int(x), int(y))

def draw_cubic_bezier(img, P0, P1, P2, P3, color=(0, 255, 0), thickness=2):
    """在圖像上繪製三次貝賽爾曲線"""
    last_point = P0
    for t in np.linspace(0, 1, num=100):
        point = cubic_bezier(P0, P1, P2, P3, t)
        point = (int(point[0]), int(point[1]))
        cv2.line(img, last_point, point, color, thickness)
        last_point = point

def draw_path_to_img(control_points, img):
    for i in range(0, len(control_points) - 3, 4):
    # Make sure we have enough points
        if i + 3 < len(control_points):
            P0 = control_points[i]
            P1 = control_points[i + 1]
            P2 = control_points[i + 2]
            P3 = control_points[i + 3]
            draw_cubic_bezier(img, P0, P1, P2, P3, color=(0, 255, 0), thickness=2)

def get_adjusted_landmarks(method, landmarks):
    arr_points = []
    if method == 'left':
        arr_points.append(((landmarks.part(39).x + 20, landmarks.part(39).y + 40)))
        arr_points.append(((landmarks.part(40).x, landmarks.part(40).y + 40)))
        arr_points.append(((landmarks.part(41).x, landmarks.part(41).y + 40)))
        arr_points.append(((landmarks.part(36).x, landmarks.part(36).y + 40)))
        arr_points.append(((landmarks.part(36).x, landmarks.part(36).y + 40)))
        arr_points.append(((landmarks.part(17).x - 10, landmarks.part(17).y)))
        arr_points.append(((landmarks.part(0).x + 10, landmarks.part(0).y)))
        arr_points.append(((landmarks.part(1).x + 10, landmarks.part(1).y)))
        arr_points.append(((landmarks.part(1).x + 10, landmarks.part(1).y)))
        arr_points.append(((landmarks.part(2).x + 10, landmarks.part(2).y)))
        arr_points.append(((landmarks.part(3).x + 10, landmarks.part(3).y)))
        arr_points.append(((landmarks.part(4).x + 10, landmarks.part(4).y)))
        arr_points.append(((landmarks.part(4).x + 10, landmarks.part(4).y)))
        arr_points.append(((landmarks.part(5).x + 10, landmarks.part(5).y)))
        arr_points.append(((landmarks.part(48).x - 20, landmarks.part(48).y)))
        arr_points.append(((landmarks.part(39).x + 20, landmarks.part(39).y + 40)))
    elif method == 'right':
        arr_points.append(((landmarks.part(42).x - 20, landmarks.part(42).y + 40)))
        arr_points.append(((landmarks.part(47).x, landmarks.part(47).y + 40)))
        arr_points.append(((landmarks.part(46).x, landmarks.part(46).y + 40)))
        arr_points.append(((landmarks.part(45).x, landmarks.part(45).y + 40)))
        arr_points.append(((landmarks.part(45).x, landmarks.part(45).y + 40)))
        arr_points.append(((landmarks.part(26).x + 10, landmarks.part(26).y)))
        arr_points.append(((landmarks.part(16).x - 10, landmarks.part(16).y)))
        arr_points.append(((landmarks.part(15).x - 10, landmarks.part(15).y)))
        arr_points.append(((landmarks.part(15).x - 10, landmarks.part(15).y)))
        arr_points.append(((landmarks.part(14).x - 10, landmarks.part(14).y)))
        arr_points.append(((landmarks.part(13).x - 10, landmarks.part(13).y)))
        arr_points.append(((landmarks.part(12).x - 10, landmarks.part(12).y)))
        arr_points.append(((landmarks.part(12).x - 10, landmarks.part(12).y)))
        arr_points.append(((landmarks.part(11).x - 10, landmarks.part(11).y)))
        arr_points.append(((landmarks.part(54).x + 20, landmarks.part(54).y)))
        arr_points.append(((landmarks.part(42).x - 20, landmarks.part(42).y + 40)))
    return arr_points

def main():
    check_directory("res")
    check_directory("res/result")
    file_name = 'test'
    try:
        img = load_image(file_name)
        img_left = load_image(file_name)
        img_right = load_image(file_name)

        faces = detect_faces(img)
        if len(faces) == 0:
            raise ValueError("No faces detected in the image.")

        for face in faces:
            # Draw 68 landmarks.
            landmarks = get_landmarks(img, face)
            draw_landmarks(img, landmarks)
            save_image(img, f'{file_name}_landmarks')

            # Draw the left cheek area.
            draw_path_to_img(get_adjusted_landmarks('left', landmarks), img_left)

            # Draw the right cheek area onto the left cheek area.
            draw_path_to_img(get_adjusted_landmarks('right', landmarks), img_left)
            save_image(img_left, f'{file_name}_full')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()