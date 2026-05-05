# Dockerfile for the paradise-brady-email-bot Railway service.
# Build context = repo root (which contains _shared/ and paradise-brady-email-bot/).
FROM python:3.11-slim

WORKDIR /app

# Install python deps first for Docker layer caching.
COPY paradise-brady-email-bot/requirements.txt /tmp/req.txt
RUN pip install --no-cache-dir -r /tmp/req.txt

# Mirror the local Desktop layout in /app/p/email/<bot>/ so run.py's
#   SHARED_ROOT = Path(__file__).resolve().parents[2] / "_shared"
# resolves to /app/p/_shared inside the container.
RUN mkdir -p /app/p/email
COPY _shared /app/p/_shared
COPY paradise-brady-email-bot /app/p/email/paradise-brady-email-bot

WORKDIR /app/p/email/paradise-brady-email-bot

# Persistent state lives on a Railway volume mounted at /app/state.
# cron_runner.py copies the image-bundled seed DB into here on first run.
ENV STATE_DIR=/app/state
RUN mkdir -p /app/state

CMD ["python", "cron_runner.py"]
