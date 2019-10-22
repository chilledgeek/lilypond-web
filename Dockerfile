FROM python:3.8.0-slim-buster
MAINTAINER E Chow <chilledgeek@gmail.com>

USER root

WORKDIR /

RUN mkdir /workdir
RUN chmod -R 777 /workdir

RUN apt-get update && apt-get install bzip2

ADD http://download.linuxaudio.org/lilypond/binaries/linux-64/lilypond-2.18.2-1.linux-64.sh ./

RUN chmod +x lilypond-2.18.2-1.linux-64.sh
RUN ./lilypond-2.18.2-1.linux-64.sh --batch --prefix /lilypond

RUN rm -rf lilypond-2.18.2-1.linux-64.sh

RUN echo "{" >> /test.ly
RUN echo "\\\version \"2.18.2\"" >> /test.ly
RUN echo "\\\time 2/4" >> /test.ly
RUN echo "\\\clef bass" >> /test.ly
RUN echo "c4 c g g a a g2" >> /test.ly
RUN echo "}" >> /test.ly

