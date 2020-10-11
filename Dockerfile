FROM python:3.6.1-alpine
WORKDIR /app
ENV FLASK_ENV=dev
ENV JSON_LOGGING=true
ADD . /app
RUN pip install -e .
EXPOSE 5000
CMD ["python", "wsgi.py"]