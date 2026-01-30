FROM tiangolo/uvicorn-gunicorn-fastapi

WORKDIR /src

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./apikeys.txt .
COPY ./main.py .
COPY ./mail.py .
COPY ./variables.py .
COPY ./security.py .
COPY ./models.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]