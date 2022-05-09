#
FROM python:3.10
ENV PYTHONBUFFERED=1
WORKDIR /usr/srs/app
COPY ./requirements.txt /usr/srs/app
RUN pip install --no-cache-dir --upgrade -r /usr/srs/app/requirements.txt
COPY ./ /usr/srs/app
#ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

