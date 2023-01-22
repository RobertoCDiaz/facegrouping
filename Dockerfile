FROM python:3.9-slim

ENV INPUT_DIR "/app/input"
ENV OUTPUT_DIR "/app/output"
ENV TOLERANCE 0.5

RUN apt-get update && apt-get install -y cmake

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","/app/src/main.py"]
