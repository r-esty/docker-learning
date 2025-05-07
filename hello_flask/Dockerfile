# Stage 1: Build
FROM python:3.8-alpine AS build

WORKDIR /app

# Install build dependencies and clean up after installation to keep the image light
RUN apk update && apk add --no-cache \
    gcc \
    python3-dev \
    mariadb-dev \
    pkgconfig && \
    rm -rf /var/cache/apk/*  # Remove apk cache to save space

COPY . .

# Install Python dependencies without caching to save space
RUN pip install --no-cache-dir flask mysqlclient

# Stage 2: Final image
FROM python:3.8-alpine

WORKDIR /app

# Copy the app from the build stage (only the necessary files)
COPY --from=build /app /app

# Expose the port on which the Flask app will run
EXPOSE 5002

# Start the Flask app when the container runs
CMD ["python", "app.py"]
