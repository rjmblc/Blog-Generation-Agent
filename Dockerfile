FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.12.9 /uv /uvx /bin/

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install dependencies first for Docker layer caching
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

# Copy application
COPY app.py .
COPY langgraph.json .
COPY src ./src

# Make virtual environment available
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]