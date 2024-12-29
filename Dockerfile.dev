FROM python:latest

LABEL version="1.0"
LABEL description="Development environment\
 for my github.com/shi-mo/aoj project."

WORKDIR /workspace

RUN useradd -ms /bin/bash dev
RUN chown -R dev:dev /workspace
RUN chmod u=rwx,g=rx,o=rx /workspace

# Basic C/C++ environment
RUN apt-get update \
 && apt-get install -y \
    g++ \
 && rm -rf /var/lib/apt/lists/*

# Python environment
RUN pip install -U pip \
 && pip install --no-cache-dir pyyaml requests

# Ruby environment
RUN apt-get update \
 && apt-get install -y ruby-full \
 && rm -rf /var/lib/apt/lists/*
RUN gem install --clear-sources mechanize

# D language environment (dmd)
ENV URI_D_APT_REPOS="https://master.dl.sourceforge.net/project/d-apt/files/d-apt.list"
RUN wget $URI_D_APT_REPOS -O /etc/apt/sources.list.d/d-apt.list \
 && apt update --allow-insecure-repositories \
 && apt -y --allow-unauthenticated install --reinstall d-apt-keyring \
 && apt update \
 && apt-get install -y \
    dmd-compiler \
    dmd-tools \
    dmd-doc

USER dev

CMD [ "/bin/bash" ]