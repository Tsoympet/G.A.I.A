FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    portaudio19-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "launcher.py"]