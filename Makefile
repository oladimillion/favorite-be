PORT = 7000
CD=cd src &&

start:
	@echo "starting development server"
	$(CD) python3 manage.py runserver $(PORT)

install: 
	@echo "installing all dependencies"
	$(CD) pip3 install -r requirements.txt
	
seed: 
	@echo "seeding data"
	$(CD) python3 manage.py import_from_csv_file

migrate:
	@echo "migrating into the db"
	$(CD) python3 manage.py migrate

migrations: 
	@echo "creating migrations"
	$(CD) python3 manage.py makemigrations

pytest: 
	@echo "testing..."
	py.test src/api  

test: 
	@echo "testing..."
	$(CD) python3 manage.py test

seed-category: 
	@echo "testing..."
	$(CD) python3 manage.py category

dumpdata:
	@echo "dumpdata db data"
	$(CD) python3 manage.py dumpdata api --indent 4 > db.json 

loaddata:
	@echo "loading db.json data into the db"
	$(CD) python3 manage.py loaddata db.json 

freeze:
	@echo "updating requirements.txt"
	$(CD) rm -f requirements.txt
	$(CD) pip3 freeze >> requirements.txt

action:
	@echo "executing command"
	$(CD) python3 manage.py $(ARGS)
