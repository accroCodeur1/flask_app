# Étape de construction
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --user -r requirements.txt

# Étape d'exécution
FROM python:3.9-slim

WORKDIR /app

# Copier depuis le builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Assurer que les scripts dans .local sont utilisables
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]