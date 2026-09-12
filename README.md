# Stage 1: Build dependencies
FROM python:3.12-alpine AS builder

WORKDIR /build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


# Stage 2: Small production image
FROM python:3.12-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup \
    && adduser -S appuser -G appgroup

# Copy only the virtual environment
COPY --from=builder /opt/venv /opt/venv

# Copy application
COPY app.py .

ENV PATH="/opt/venv/bin:$PATH"

# Run as non-root user
USER appuser

EXPOSE 5000

# Container health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://127.0.0.1:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
