FROM python:3.6.1-alpine
WORKDIR /app
ENV FLASK_ENV=dev
ADD . /app
RUN pip install -e .
CMD ["python", "wsgi.py"]