FROM python:3.10-slim

WORKDIR /app

# We create our env file for the database path
RUN echo "SQLALCHEMY_DATABASE_URL=sqlite:///blog.data" > /app/.env

COPY blog.data requirements.txt Makefile ./

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY blog blog

EXPOSE 8000

CMD ["uvicorn", "blog.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]