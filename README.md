# Group Photos by Faces

A Python script that groups images in a given folder by faces and move them to different folders based on facial recognition. The images that do not contain any face are moved to a different folder. The script uses dlib's pre-trained models for facial detection, landmark prediction and face encoding. This can be useful for organizing a large collection of images, especially if they are not named or labeled in a consistent way.

## Python dependencies

- numpy
- opencv-python
- dlib
- face_recognition
- shutil

## Docker dependencies

- Docker
- docker-compose

## Install and configuration

1. Clone this repo and `cd` into it
```bash
git clone 
cd facegrouping
```

2. Open the `.env` file with your favorite text editor and set the images source folder and the directory you want to use as output for the program. If you want to change the face matching threshold, you can do it by modifying the value of the tolerance.
```bash
 # Images source
INPUT_DIR=/app/input
# Output directory
OUTPUT_DIR=/app/ouput
# The lower, the more strict the face matching will be
TOLERANCE=0.5 
```

## Usage

### Using Docker
Once everythin is set up, run the following command from the root directory.
```bash
docker-compose up
```

The images that contain faces will be moved to different subfolders inside the output folder, each subfolder with a specific face, and the images that do not contain faces will be moved to a folder named "no_face" inside the output folder.
