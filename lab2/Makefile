ENV_FILE := "./environment.yaml"
APP_CONDA_ENV_NAME ?= "training_labs"

CDIR := ${CURDIR}
SHELL := $(shell which bash)

CONDA_BIN := $(shell which conda)
CONDA_ROOT := $(shell $(CONDA_BIN) info --base)
APP_CONDA_ENV_PREFIX := $(shell conda env list | grep $(APP_CONDA_ENV_NAME) | sort | awk '{print $$2}')
CONDA_ACTIVATE := source $(CONDA_ROOT)/etc/profile.d/conda.sh; conda activate $(APP_CONDA_ENV_NAME) && PATH=$(APP_CONDA_ENV_PREFIX)/bin:${PATH};

DOCKER_REPO_PATH := $(shell echo "$$DOCKER_REPO/")
DOCKER_USERNAME_PATH := $(shell echo "$$DOCKER_USERNAME/$(DOCKER_PROJECT_PATH)")
APP_DOCKER_IMAGE_NAME := continuumio/miniconda3:latest

ENV_BIN_DIR := $(APP_CONDA_ENV_PREFIX)/bin
ENV_LIB_DIR := $(APP_CONDA_ENV_PREFIX)/lib
ENV_PYTHON := $(ENV_BIN_DIR)/python
ENV_PIP := $(ENV_BIN_DIR)/pip

HTTP_HOST ?= "127.0.0.1"
HTTP_PORT ?= 8080

# Targets
environment:
	$(CONDA_BIN) remove -n $(APP_CONDA_ENV_NAME) --all -y --force-remove
	$(CONDA_BIN) env update -n $(APP_CONDA_ENV_NAME) -f $(ENV_FILE)

test:
	$(CONDA_ACTIVATE) python -m pytest tests/ --durations=0

run:
	$(CONDA_ACTIVATE) uvicorn app.server:app --host $(HTTP_HOST) --port $(HTTP_PORT)

package:
	docker build \
		-t training_labs_docker \
		-f ./deploy/docker/Dockerfile \
		--build-arg BASE_IMAGE=$(APP_DOCKER_IMAGE_NAME) \
		--build-arg http_proxy=$(http_proxy) \
		--build-arg https_proxy=$(https_proxy) \
		--build-arg no_proxy=$(no_proxy)\
		.

install:
	$(CONDA_BIN) env update -n $(APP_CONDA_ENV_NAME) -f $(ENV_FILE)
	$(CONDA_ACTIVATE) pip install \
		--upgrade -r requirements.txt

DOCKERSTACK_NAME ?= $(APP_CONDA_ENV_NAME)
DOCKERSTACK_APP_IMAGE_NAME ?= $(APP_DOCKER_IMAGE_NAME)

run-docker:
	docker swarm init || true
	APP_IMAGE_NAME=$(DOCKERSTACK_APP_IMAGE_NAME) docker stack deploy --compose-file=./deploy/docker/docker-compose.yaml $(DOCKERSTACK_NAME)

list-docker:
	docker stack ps $(DOCKERSTACK_NAME)

stop-docker:
	docker stack rm $(DOCKERSTACK_NAME)
