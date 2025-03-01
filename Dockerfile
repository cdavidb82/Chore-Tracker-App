FROM python:3.9-slim

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Set the DISPLAY environment variable
ENV DISPLAY=:99

# Start Xvfb
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & exec python chore_tracker.py"]