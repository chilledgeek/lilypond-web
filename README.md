| Code quality checks  | Status |
| ------------- |:-------------:|
| CodeFactor      |  [![Codefactor](https://www.codefactor.io/repository/github/chilledgeek/lilypond-web/badge?style=plastic)](https://www.codefactor.io/repository/github/chilledgeek/lilypond-web) |
| CircleCI |  [![CircleCI](https://circleci.com/gh/chilledgeek/lilypond-web.svg?style=svg)](https://circleci.com/gh/chilledgeek/lilypond-web)|
| Codecov | [![codecov](https://codecov.io/gh/chilledgeek/lilypond-web/branch/master/graph/badge.svg)](https://codecov.io/gh/chilledgeek/lilypond-web)|

# Lilypond Web Service
- Lightweight service that runs simple webpage to access Lilypond functionalities
- Based on docker image base [chilledgeek/lilypond-docker](https://hub.docker.com/r/chilledgeek/lilypond-docker)
- Source code is published on [github](https://www.github.com/chilledgeek/lilypond-web), while the corresponding docker image is published on [docker hub](https://hub.docker.com/r/chilledgeek/lilypond-web)
- Default port is set to 8080

# How to use
- Ensure docker is installed and available (locally or on server that will host this, etc, kubernetes cluster)
- Pull docker image: ```docker pull chilledgeek/lilypond-web```
- To run locally:
  - Linux:
    - Run service: ```sudo docker run chilledgeek/lilypond-web --network="host"```
    - Find the port:
      - ```docker container ps``` (get the NAME of running container (e.g. 3278cbd341f0)
      - ```docker container inspect 3278cbd341f0 | grep IPAddress```
    - Access the IPAddress using any browser (port 8080))
  - Mac:
    - There seems to be known issues in [running docker on a mac](https://docs.docker.com/docker-for-mac/networking/), so a different command line needs to be used:
      - ```docker run -p 8080:8080 chilledgeek/lilypond-web```
      - Access the IPAddress using any browser (port 8080))

- Paste in some Lilypond code, e.g. here is 
[a sample lilypond code](https://github.com/chilledgeek/lilypond-web/blob/master/test/common/harry_potter_intro.ly) 
to generate the score for the intro part of Harry Potter's theme song

