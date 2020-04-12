FROM python:3.8

WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

ENV FLASK_ENV=development
CMD ["flask", "run", "--host", "0.0.0.0"]
