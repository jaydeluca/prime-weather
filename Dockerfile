FROM python:3.9.7-alpine3.14
WORKDIR /app
ENV FLASK_ENV=dev
ENV JSON_LOGGING=true
ADD . /app
RUN pip install -e .
EXPOSE 5000
CMD ["python", "wsgi.py"]