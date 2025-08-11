# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Pacotes de sistema para compilar psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Diretório do app (bate com o compose)
WORKDIR /code

# Instala as dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

EXPOSE 8000

# (no compose a gente já usa o comando com migrate + runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
