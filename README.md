# Group Photos by Faces

## Dependencies

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
Once everythin is set up, run the following command from the root directory.
```bash
docker-compose up
```
