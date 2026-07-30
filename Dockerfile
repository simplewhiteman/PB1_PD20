FROM python:3.9-slim

WORKDIR /app

#Instalejam atkaribas reproducejami (vienadi katru reizi)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Kopejam tikai to, kas vajadzigs lietotnes darbibai
COPY app.py

CMD ["python", "app.py"]