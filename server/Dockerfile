FROM python:3.11

WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt