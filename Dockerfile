ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python -m venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

RUN apt-get update -y && \
    apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY ./src /code/

RUN mkdir -p /code

WORKDIR /code

ARG PROJECT_NAME="home"

RUN printf "#!/bin/bash\n\n" > ./paracode_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracode_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracode_runner.sh && \
    printf "python manage.py vendor_pull\n" >> ./paracode_runner.sh && \
    printf "python manage.py collectstatic --no-input\n" >> ./paracode_runner.sh && \    
    printf "gunicorn -w 3 -b \"[::]:\${RUN_PORT}\" ${PROJECT_NAME}.wsgi:application\n" >> ./paracode_runner.sh

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x ./paracode_runner.sh 

CMD ["/bin/bash", "./paracode_runner.sh"]


  
