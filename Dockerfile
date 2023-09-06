FROM python:3.11.4-alpine3.18@sha256:0a56f24afa1fc7f518aa690cb8c7be661225e40b157d9bb8c6ef402164d9faa7 as cache

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PAT
WORKDIR /home/app/
COPY requirements.txt /home/app/
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.4-alpine3.18@sha256:0a56f24afa1fc7f518aa690cb8c7be661225e40b157d9bb8c6ef402164d9faa7
COPY --from=cache /venv /venv
ENV PATH=/venv/bin:$PATH

COPY . .
EXPOSE 8080

ENTRYPOINT ["python3", "server.py"]

# Use an official Python runtime as a parent image
FROM python:3.x

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "server.py"]
