FROM chilledgeek/lilypond-docker
LABEL maintainer="chilledgeek@gmail.com"

USER root

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

USER 1001

EXPOSE 8080

ENTRYPOINT ["python", "run.py"]

