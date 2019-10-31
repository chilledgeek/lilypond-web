FROM python:3.8.0-slim-buster
LABEL maintainer="chilledgeek@gmail.com"

USER root

WORKDIR /

COPY . /

RUN mkdir -p /workdir
RUN chmod -R 777 /workdir

RUN apt-get update && apt-get install -y --no-install-recommends bzip2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ADD http://download.linuxaudio.org/lilypond/binaries/linux-64/lilypond-2.18.2-1.linux-64.sh ./

RUN chmod +x lilypond-2.18.2-1.linux-64.sh
RUN ./lilypond-2.18.2-1.linux-64.sh --batch --prefix /lilypond

RUN rm -rf lilypond-2.18.2-1.linux-64.sh

RUN pip install -r requirements.txt

USER 1001

EXPOSE 8080

ENTRYPOINT ["python", "run.py"]

