# Simple Django App

The purpose of this repo is to showcase how quick and easy it is to set up a Django+DRF app. It's also a good way to see the basics of a Django app for future development. I will try to update this from time to time when Django/DRF makes changes, or when newer build technologies come out (e.g. Pipfile)

## What's included

I've included a basic Dockerfile to allow more portable testing. In reality, you can do everything by running the normal commands without using the different `make` targets (see section below).

This simple [Django](https://www.djangoproject.com/) project is meant to be for a REST API, with an admin backend. That's why this is using Django and [Django Rest Framework](http://www.django-rest-framework.org/).

## Dev Setup

You should have Docker installed (`brew cask install docker` on macOS).
This is the easiest way to set everything up.

Run `make docker` to set up the Docker container. Run this whenever you change something in the Pipfile.

Run `make migrate` to do the initial setup of the database.

Run `make migrations` to create migrations (e.g. when you change the model).

Run `make run` to run the development server.

Run `make interactive` to get to the Django shell.

Run `make superuser` to setup the superuser account (username is `admin`).

