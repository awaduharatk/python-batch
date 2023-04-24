FROM python:3.9-buster as python-base

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip setuptools

WORKDIR /workspace


FROM python-base as initial
# python env
ENV PYTHONUTF8=1 \
PYTHONPATH="/workspace/python-app/python_app:$PYTHONPATH" \
PYTHONPYCACHEPREFIX=/tmp/pycache \
POETRY_VERSION=1.2.1 \
POETRY_HOME=/opt/poetry \
PYSETUP_PATH="/opt/pysetup" \
LIB_PATH="./python-app" \
PYTEST_ADDOPTS="-p no:cacheprovider"

# install poetry
RUN curl -sSL https://install.python-poetry.org | python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


FROM initial as development
# tools
RUN apt-get install -y vim less
RUN echo "alias ll='ls -la --color'" >> /root/.bashrc
WORKDIR $PYSETUP_PATH

# library install
COPY ["${LIB_PATH}/pyproject.toml", "${LIB_PATH}/poetry.lock", "./"]
RUN poetry install


FROM initial as production
COPY ["./python-app/", "/src/python-app/"]
WORKDIR /src/python-app/
RUN poetry install --no-dev
# TODO
ENV PYTHONPATH="/src/python-app/python_app:$PYTHONPATH"
ENTRYPOINT [ "python" ]