FROM ubuntu:latest
RUN apt-get update && apt-get install python3-pip -y

# Set the working directory
WORKDIR /app

# Copy the script into the working directory
COPY username_checker.py .

CMD python username_checker.py
