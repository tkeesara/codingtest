#!/bin/bash

# Build Docker image
docker build -t geography-questions-api .

# Run Docker container
docker run -d -p 5000:5000 geography-questions-api
