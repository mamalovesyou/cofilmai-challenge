FROM python:3.10-slim as base

# Install tools
RUN apt update 
RUN apt install -y build-essential \
    pkg-config \
    libpq-dev \
    libopenblas-dev \
    gfortran \
    git \
    wget \
    ffmpeg \
    flac

WORKDIR /code

RUN pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN playwright install-deps
RUN playwright install chromium

COPY ./prisma /code/prisma

RUN prisma generate

FROM base as api

COPY ./services/trends /code/trends

WORKDIR /code/trends

FROM base as tiktok-worker

COPY ./workers/tiktok /code/tiktok

WORKDIR /code/tiktok

CMD ["python3", "main.py"]