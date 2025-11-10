# base image 
FROM python:3.11-slim

# Working directory

WORKDIR /app

# copy the directory

COPY requirements.txt .

# instruction 
RUN pip install -r requirements.txt

#  copy rest of this things
COPY . .

# expose application port

EXPOSE 8000

# command to start fast api

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
