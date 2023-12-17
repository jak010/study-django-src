POETRY_BIN=/opt/homebrew/bin/poetry

PYTHON=$(POETRY_BIN) run python

run.local:
	$(PYTHON) ./manage.py runserver --settings=config.settings.dev

django.migrations:
	$(PYTHON) ./manage.py makemigrations

django.migrate:
	$(PYTHON) ./manage.py migrate

django.test:
	$(PYTHON) ./manage.py test
