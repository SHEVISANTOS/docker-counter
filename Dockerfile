# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /code

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Tell Docker this container listens on port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
