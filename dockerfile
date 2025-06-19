FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Créer un utilisateur non root
RUN useradd -m appuser
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "my_data_app.py", "--server.port=8501", "--server.enableCORS=false"]
