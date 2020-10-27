serve:
	./manage.py runserver

migrate:
	./manage.py migrate

migrations:
	./manage.py makemigrations $(app)

collectstatic:
	./manage.py collectstatic

app:
	./manage.py startapp $(name)

superuser:
	./manage.py createsuperuser --username $(name)