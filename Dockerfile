FROM python:3.9-slim

WORKDIR /app

# Instalejam atkaribas reproducejami (vienadi katru reizi)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopejam visus projekta failus (izņemot tos, kas ir iekš .dockerignore)
COPY . .

CMD ["python", "app.py"]
