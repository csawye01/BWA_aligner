FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /BWA_aligner

CMD ["python", "/BWA_aligner/project/views.py"]