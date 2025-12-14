FROM python:3.12-slim
WORKDIR /TaximeterProject
COPY . /TaximeterProject
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]