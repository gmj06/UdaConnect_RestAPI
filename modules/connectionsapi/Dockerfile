FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# FROM python:3.7-alpine
# RUN mkdir /backend
# WORKDIR /backend
# COPY requirements.txt /backend/requirements.txt
# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt
# COPY . .
