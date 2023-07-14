# Use the base Python image
FROM python:3.11.4-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY .env.example ./
RUN cp .env.example .env
COPY . .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python3", "main.py"]