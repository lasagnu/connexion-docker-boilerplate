# connexion-docker-boilerplate
docker-centric boilerplate for development of flask open-api based web applications using connexion

# run application in container

docker-compose -f docker.compose.yml up

# run tests in container

docker-compose -f docker.compose.tests.yml run --rm tests

# linting - run black and isort in container

docker-compose -f docker.compose.linters.yml up

