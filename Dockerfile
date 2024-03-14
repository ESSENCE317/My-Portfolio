FROM python:3.9
WORKDIR /app
COPY . /app
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]