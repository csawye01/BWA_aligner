FROM python:3

EXPOSE 8000

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /usr/src/app

# Run the app
CMD ["./run.py"]