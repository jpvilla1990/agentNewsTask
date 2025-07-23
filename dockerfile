FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install uv
RUN uv sync

CMD ["bash", "service/run_app.sh"]