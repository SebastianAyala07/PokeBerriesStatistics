FROM ubuntu

ADD . /python-docker
WORKDIR /python-docker

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN python3 -m pip install -r requeriments.txt
ENV FLASK_APP="entrypoint:app"
ENV BASE_BERRY_ENDPOINT_URL="https://pokeapi.co/api/v2/berry/"
ENV FLASK_ENV="development"
ENV APP_SETTINGS_MODULE="config.default.Development"


CMD [ "flask", "run", "--host=0.0.0.0"]
