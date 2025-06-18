# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copier le fichier requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'app
COPY . .

# Exposer le port Streamlit
EXPOSE 8501

# Lancer l'app Streamlit
CMD ["streamlit", "run", "my_data_app.py", "--server.port=8501", "--server.enableCORS=false"]
