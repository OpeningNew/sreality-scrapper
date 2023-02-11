FROM python:3.11-bullseye

WORKDIR /app
COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run"]
