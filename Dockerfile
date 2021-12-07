# base python docker image
FROM python:3.9.5-buster


# import code
ADD . /code

# Change dir
WORKDIR /code

# install lib
RUN pip install flask
RUN pip install redis

# Open the port for flask
EXPOSE 5001

# Running python file
CMD python main.py
