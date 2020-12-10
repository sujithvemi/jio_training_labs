ARG BASE_IMAGE="continuumio/miniconda3:latest"
FROM ${BASE_IMAGE}

ARG http_proxy
ARG https_proxy
ARG no_proxy

ARG app_location='/usr/src/app'
ARG APP_CONDA_ENV_NAME='training_labs'
ENV APP_CONDA_ENV_NAME=$APP_CONDA_ENV_NAME
ENV CONDA_BIN='/opt/conda/bin/conda'
ENV PIP_NO_CACHE_DIR=1

WORKDIR ${app_location}

RUN export http_proxy=$http_proxy && export https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && export HTTPS_PROXY=$https_proxy && export NO_PROXY=$no_proxy \
    && apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog make jq build-essential \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

ADD ./requirements*.txt ${app_location}/
ADD ./environment*.yaml ${app_location}/
ADD ./Makefile* ${app_location}/
ADD ./VERSION ${app_location}
ADD ./factorial.py ${app_location}

ADD app ${app_location}/app

RUN export http_proxy=$http_proxy && export https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && export HTTPS_PROXY=$https_proxy && export NO_PROXY=$no_proxy \
    && $CONDA_BIN env update -n $APP_CONDA_ENV_NAME -f ${app_location}/environment.yaml \
    && $CONDA_BIN clean --yes --all
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

RUN $CONDA_BIN init
RUN export http_proxy=$http_proxy && export https_proxy=$https_proxy && no_proxy=$no_proxy \
    && export HTTP_PROXY=$http_proxy && export HTTPS_PROXY=$https_proxy && export NO_PROXY=$no_proxy \
    && make install \
    && $CONDA_BIN clean --yes --all
    && unset http_proxy && unset https_proxy && unset no_proxy \
    && unset HTTP_PROXY && unset HTTPS_PROXY && unset NO_PROXY

ARG HTTP_HOST='127.0.0.1'
ARG HTTP_PORT=8080

EXPOSE ${HTTP_PORT}
CMD make run
