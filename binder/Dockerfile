FROM ubuntu:jammy


# install the notebook package
RUN  apt-get -qq update && apt-get install --yes --no-install-recommends git python3-pip python3-venv && \
     pip install --no-cache --upgrade pip && \
     pip install --no-cache jupyterlab pipx


ENV SHELL=/bin/bash

# create user with a home directory
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}


# pipx: install programs in each virtual environment
COPY _tools_pipx.txt .
RUN while read -r tool; do \
      /usr/local/bin/pipx install --pip-args='--no-cache' "$tool"; \
    done < _tools_pipx.txt
