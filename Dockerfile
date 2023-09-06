FROM python:3.11.4-alpine3.18@sha256:0a56f24afa1fc7f518aa690cb8c7be661225e40b157d9bb8c6ef402164d9faa7 as cache

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PAT
WORKDIR /home/app/
COPY requirements.txt /home/app/
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.4-alpine3.18@sha256:0a56f24afa1fc7f518aa690cb8c7be661225e40b157d9bb8c6ef402164d9faa7
COPY --from=cache /venv /venv
ENV PATH=/venv/bin:$PATH

COPY . .
EXPOSE 8080

ENTRYPOINT ["python3", "server.py"]

