# Dockerfile
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the code and install dependencies
COPY . /app
RUN pip install fastapi uvicorn pydantic google-api-python-client google-auth-httplib2 google-auth-oauthlib apiclient

# Expose the port and run the server
EXPOSE 8080
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
