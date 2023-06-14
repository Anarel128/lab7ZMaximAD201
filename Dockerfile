FROM python:3.9.7

WORKDIR /lab5

COPY --chown=lab5:lab5 . .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]




#SHELL ["/bin/bash", "-c"]


#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

#RUN pip install --upgrade pip

#RUN apt update && apt -qy install gcc

#RUN useradd -rms /bin/bash lab5 && chmod 777 /opt /run
#USER lab5