# Use python base image
FROM python:3.9-slim

# set the working directory

WORKDIR /app

# copy Files
COPY app/ /app/

# INSTALL the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#  Run the application
CMD ["python", "app.py"]