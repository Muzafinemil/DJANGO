FROM python:3.11.3

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY . /opt/app

WORKDIR /opt/app/project1

CMD ["python", "manage еу.py", "runserver", "0:8000"]