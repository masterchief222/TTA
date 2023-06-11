# Use the official Debian 10 as the base image
FROM python:slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Install the necessary packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     ca-certificates \
#     build-essential \
#     libncurses5-dev \
#     libgpm-dev \
#     && rm -rf /var/lib/apt/lists/*

# Set the TERM environment variable
ENV TERM=xterm

# Copy the Python script and any other required files to the working directory
COPY src/ .

# Copy the requirements.txt file to the working directory
COPY src/requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Define the command to run your Python script
CMD ["python3", "-i", "main.py"]
