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


# condax packages
COPY _tools_condax.txt .
ENV CONDAX_HIDE_EXITCODE=1
ENV CONDAX_LOG=${HOME}/.local/logs/condax_install_log.txt
# condax: install programs in each conda environment
RUN mkdir -p ~/.config/condax
RUN echo "use_lockfiles: false" > ~/.mambarc
RUN echo "prefix_dir: ~/.local/share/condax/envs" > ~/.config/condax/config.yaml
RUN mkdir -p ~/.local/logs
RUN while read -r _tool; do \
        echo "Installing ${_tool}" | tee -a "$CONDAX_LOG"; \
        condaxSuccess=$("$HOME"/.local/bin/condax install -c conda-forge -c bioconda --force "$_tool" 2>&1 | tee -a "$CONDAX_LOG"); \
        if [ ! condaxSuccess ]; then \
            echo "condax retrying... $_tool" | tee -a "$CONDAX_LOG"; \
            "$HOME"/.local/bin/condax remove "$_tool" | tee -a "$CONDAX_LOG"; \
            "$HOME"/.local/bin/condax install -c conda-forge -c bioconda --force "$_tool" 2>&1 | tee -a "$CONDAX_LOG"; \
        fi \
    done < _tools_condax.txt
RUN "$HOME"/.local/bin/micromamba clean --all --yes --force-pkgs-dirs
