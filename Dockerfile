FROM python:3.8
LABEL MAINTAINER="mojtaba_nafez"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

# Installing requirements
ADD requirements/requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files


CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]
