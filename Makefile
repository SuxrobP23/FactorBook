extract:
	pybabel extract --input-dirs=. -o locales/messages.pot
init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
update:
	pybabel update -d locales -D messages -i locales/messages.pot
compile:
	pybabel compile -d locales -D messages

up:
	docker compose up
down:
	docker compose down
rmi:
	docker rmi factorbook23-bot:latest
web_admin:
	uvicorn web.app:app --host=localhost --port=8000

