FROM python:3.10-slim-buster AS base
WORKDIR /app

ENV PYTHONPATH /app
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ---- Dependencies ----
FROM base AS dependencies
RUN apt update && \
    apt install --no-install-recommends -y gcc libsasl2-dev libldap2-dev libev-dev default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

# ---- Release ----
FROM base AS release

RUN apt update && \
    apt install --no-install-recommends -y libidn11  libev4 libffi6 libgmp10 libgnutls30 libhogweed4 default-libmysqlclient-dev \
                                          libldap-2.4-2 libnettle6 libp11-kit0 libsasl2-dev libtasn1-6 \
                                          redis-tools && \
    rm -rf /var/lib/apt/lists/*

COPY --from=dependencies /app/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache
RUN pip install -r requirements.txt && rm -rf /root/.cache

COPY /src /app/

RUN python inference.py
