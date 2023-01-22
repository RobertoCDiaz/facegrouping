import numpy as np
import cv2
import dlib
import os
import face_recognition
import shutil

def group_images_by_face(folder_path: str):
    """
    This function groups images in a given folder by faces and move them to different folders. The images that do not contain any face are moved to a different folder.

    Parameters:
    folder_path (str): The path to the folder containing the images to be grouped.
    """
    # Get face matching tolerance from .env
    tolerance = float(os.environ['TOLERANCE'])

    # Initialize the face detector and shape predictor
    face_detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor('/app/data/shape_predictor_68_face_landmarks.dat')
    
    # Initialize the face encoder
    face_encoder = dlib.face_recognition_model_v1('/app/data/dlib_face_recognition_resnet_model_v1.dat')
    
    # Create a dictionary to store the faces and their corresponding image paths
    faces = {}
    no_face_images = []
    
    # Iterate through all the images in the folder
    paths = os.listdir(folder_path)
    for img_idx, image_path in enumerate(paths):
        # Load the image
        image = cv2.imread(os.path.join(folder_path, image_path))
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        detected_faces = face_detector(gray, 1)
        
        # If no faces are detected, add the image to the no_face_images list
        if len(detected_faces) == 0:
            no_face_images.append(image_path)
        else:
            # Iterate through the detected faces
            for i, face_rect in enumerate(detected_faces):
                # Determine the facial landmarks for the face
                shape = shape_predictor(gray, face_rect)

                # Encode the face
                face_encoding = face_encoder.compute_face_descriptor(image, shape)

                # Compare the face to the faces in the dictionary
                match = False
                for known_face in faces:
                    # Compute the L2 distance between the face encodings
                    distance = face_recognition.face_distance(np.array([known_face]), np.array(face_encoding))

                    # If the distance is less than a threshold, consider it a match
                    if distance < tolerance:
                        match = True
                        faces[known_face].append(image_path)
                        break

                # If it's a new face, add it to the dictionary
                if not match:
                    faces[face_encoding] = [image_path]

        print('☑️ ' + str(img_idx) + '/' + str(len(paths)) + ': ' + image_path)

    print('Organizing images...')
    for i, face in enumerate(faces):
        folder_name = "/app/output/face_{}".format(i + 1)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        for image_path in faces[face]:
            shutil.copy(os.path.join(folder_path, image_path), folder_name)

    # separe images with no faces
    no_faces_folder = '/app/output/no_face'
    if not os.path.exists(no_faces_folder):
        os.mkdir(no_faces_folder)
    for image_path in no_face_images:
            shutil.copy(os.path.join(folder_path, image_path), no_faces_folder)

    print('✅ Face grouping done!')

if __name__ == '__main__':
    group_images_by_face("/app/input")
