ENV_FILE := "./environment.yaml"
APP_CONDA_ENV_NAME ?= "training_labs"

CDIR := ${CURDIR}
SHELL := $(shell which bash)

CONDA_BIN := $(shell which conda)
CONDA_ROOT := $(shell $(CONDA_BIN) info --base)
APP_CONDA_ENV_PREFIX := $(shell conda env list | grep $(APP_CONDA_ENV_NAME) | sort | awk '{print $$2}')
CONDA_ACTIVATE := source $(CONDA_ROOT)/etc/profile.d/conda.sh; conda activate $(APP_CONDA_ENV_NAME) && PATH=$(APP_CONDA_ENV_PREFIX)/bin:${PATH};

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


