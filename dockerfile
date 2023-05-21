FROM python:3.10.9
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python3 ./api.py
EXPOSE 5555