# Makefile for 2030.5 gridappsd example

VENV_NAME = venv
PYTHON = $(VENV_NAME)/Scripts/python.exe
PIP = $(VENV_NAME)/Scripts/pip.exe

.PHONY: all venv install run-server run-client clean

all: venv install

venv:
	python -m venv $(VENV_NAME)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install gridappsd

run-server:
	$(PYTHON) src/server.py

run-client:
	$(PYTHON) src/client.py

clean:
	rmdir /S /Q $(VENV_NAME)
