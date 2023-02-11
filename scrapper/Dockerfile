FROM ubuntu:22.04

WORKDIR /app
COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y python3.11 python3-pip
RUN python3.11 -m pip install --upgrade pip setuptools wheel
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

COPY . .

CMD ["scrapy", "crawl", "sreality"]
