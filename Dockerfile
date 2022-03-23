FROM hl8469/preonboarding:base-image-1.0.0

COPY . /

EXPOSE 8000

RUN python download_model.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
