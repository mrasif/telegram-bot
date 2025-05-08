FROM python:3.8

LABEL maintainer="Asif Mohammad Mollah<https://mrasif.in>"

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
