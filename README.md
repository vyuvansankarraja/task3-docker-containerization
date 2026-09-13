FROM python:3.12-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .

RUN pip install --no-cache-dir --no-compile -r requirements.txt \
    && pip uninstall -y pip setuptools \
    && find /usr/local/lib/python3.12 -type d -name '__pycache__' -prune -exec rm -rf {} + \
    && find /usr/local/lib/python3.12 -type f -name '*.pyc' -delete

COPY app.py .

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://127.0.0.1:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
