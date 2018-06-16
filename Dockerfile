FROM kennethreitz/pipenv
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app/
COPY . /app
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000