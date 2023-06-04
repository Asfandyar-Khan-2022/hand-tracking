# Dockerfile, image, Container
FROM python:3.7

ADD hand_tracking_with_lib.py  .
ADD hand_tracking_module.py  .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install opencv-python mediapipe

CMD ["python", "./hand_tracking_with_lib.py"]
