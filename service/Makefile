date = $(shell date)

.PHONY: migration
migration:
	alembic revision --autogenerate -m "$(date)"


.PHONY: migrate
migrate:
	alembic upgrade head