
DOCKER = docker
DOCKER_RUN = $(DOCKER) run --rm -v $$PWD:/app

.PHONY: docker
docker:
	$(DOCKER) build -t simple-django-app .

.PHONY: run
run:
	$(DOCKER_RUN) -it -p 8000:8000 simple-django-app:latest

.PHONY: migrate
migrate:
	$(DOCKER_RUN) simple-django-app:latest python3 manage.py migrate

.PHONY: migrations
migrations:
	$(DOCKER_RUN) simple-django-app:latest python3 manage.py makemigrations simpleapp

.PHONY: interactive
interactive:
	$(DOCKER_RUN) -it simple-django-app:latest python3 manage.py shell

.PHONY: superuser
superuser:
	$(DOCKER_RUN) -it simple-django-app:latest python3 manage.py createsuperuser --email admin@example.com --username admin

.PHONY: bash
bash:
	$(DOCKER_RUN) -it simple-django-app:latest /bin/bash
