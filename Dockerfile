FROM pytorch/pytorch

RUN pip install --no-cache-dir "python-doctr[torch]"

RUN apt-get update -y && apt-get -y install python3-opencv 

COPY image_extractor.py .
COPY preload.py .
RUN python3 preload.py

CMD [ "python", "-u", "image_extractor.py" ]