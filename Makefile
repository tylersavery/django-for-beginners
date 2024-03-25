run:
	python manage.py runserver

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

import_fixtures:
	python manage.py loaddata ./fixtures/*.json