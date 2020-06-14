FROM amancevice/pandas:0.25.0

ENV PORT=${PORT}
ENV HOST=${HOST}

ADD . /code
WORKDIR /code


RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app/app.py"]