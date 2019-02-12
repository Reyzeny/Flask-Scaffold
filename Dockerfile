from python:3

WORKDIR /backend
COPY . .

RUN pip --no-cache-dir install -r req.txt

EXPOSE 5000

# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade
CMD gunicorn --bind 0.0.0.0:5000 entry:app