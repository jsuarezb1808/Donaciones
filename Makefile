start_db:
	docker compose up -d

stop_db:
	docker compose down

open_db:
	mysql -u user --password db --host 127.0.0.1 --port 3306