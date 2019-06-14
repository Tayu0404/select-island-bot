FROM python:3.6-stretch

RUN pip install \
	discord.py

WORKDIR /python/src/
COPY ./main.py .

CMD ["python" ,"./main.py"]
