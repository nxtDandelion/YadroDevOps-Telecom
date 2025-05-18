FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

WORKDIR /app

COPY main.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]