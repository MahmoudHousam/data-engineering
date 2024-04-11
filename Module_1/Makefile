DATA_PATH = c:/ZoomCamp/data-engineering/module_1/mimiciii_data
DATA_URL = https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet

docker_network:
	docker network create pg-network


postgres:
	docker run -it \
	-e POSTGRES_USER="root" \
	-e POSTGRES_PASSWORD="root" \
	-e POSTGRES_DB="mimiciii" \
	-v $(DATA_PATH):/var/lib/postgresql/data \
	-p 5430:5432 \
	--network pg-network \
	--name pg-database \
	--rm -d \
	postgres:13

postgres_down:
	docker stop pg-database

pgadmin:
	docker run -it \
	-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
	-e PGADMIN_DEFAULT_PASSWORD="root" \
	-p 8080:80 \
	--network pg-network \
	--name pg-admin4 \
	--rm -d \
	dpage/pgadmin4


pgadmin_down:
	docker stop pg-admin4


psql_connect:
	pgcli \
	-h localhost \
	-p 5430 \
	-u root \
	-d mimiciii 


data_ingestion:
	docker run -it \
	--network=pg-network \
	data_ingest \
	--user=root \
	--password=root \
	--host=pg-database \
	--port=5432 \
	--db=mimiciii \
	--table_name=patient_admission_to_icu
	--url=$(DATA_URL)

data_ingestion_down:
	docker stop data_ingest


apply_gcp_plan:
	terraform plan -out "gcp_terraform_plan" && \
	terraform show -json "gcp_terraform_plan" | jq > gcp_terraform_plan.json && \
	terraform apply "gcp_terraform_plan" \


destroy_gcp_plan:
	terraform destroy


format_terraform:
	terraform fmt