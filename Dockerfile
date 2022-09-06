FROM python:3.10

ADD /requirements.txt /talana-docker/requirements.txt

RUN set -ex \
    && apt-get update -y \
    && apt-get install -y \
        binutils \
        libproj-dev \
        gdal-bin \
        libzip-dev \
        libxml2-dev \
        libpng-dev \
        libwebp-dev \
        wget \
        llvm \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --default-timeout=100 -r /talana-docker/requirements.txt

ADD / /talana-docker
WORKDIR /talana-docker

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# CMD ["gunicorn", "--bind", ":80001", "--workers", "3", "--env", "DJANGO_SETTINGS_MODULE=talana.settings.docker", "talana.wsgi_docker:application"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]