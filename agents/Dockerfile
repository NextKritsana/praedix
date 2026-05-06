FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Paperclip and other essentials
RUN pip install --no-cache-dir \
    google-generativeai \
    openai \
    langchain \
    chromadb \
    redis \
    psycopg2-binary \
    python-dotenv \
    requests

COPY . .

# Keep the container running for debugging and execution
CMD ["tail", "-f", "/dev/null"]
