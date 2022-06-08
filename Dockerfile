FROM python:3
LABEL author="Prajwal"
WORKDIR /
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3" ]
CMD ["main.py"]