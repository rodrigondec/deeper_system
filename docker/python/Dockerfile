FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./setup.py /app/setup.py
COPY ./README.md /app/README.md
RUN pip install -e ".[testing]"

COPY ./docker/python/start-dev.sh /start-dev.sh
RUN sed -i 's/\r//' /start-dev.sh
RUN chmod +x /start-dev.sh
