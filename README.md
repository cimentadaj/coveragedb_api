# COVerAGE-DB API

A web API for querying the COVerAGE-DB: a global demographic database of COVID-19 cases and deaths.

## Steps to deploy database and API

- Create `backend/.env` file with the template from `backend/.env.template`. For now (not secret at this moment), fill with these (be sure to look at the template in case this hasn't been updated):

```
# Project
PROJECT_NAME=coveragedb_api
PROJECT_VERSION=0.0.0

# Database
SECRET_KEY=secret
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres
```

- Deposit `inputDB.csv` inside `input_data` and run `awk 'NR>1' inputDB.csv > tmp.csv && mv tmp.csv inputDB.csv` on it. That will remove the first line of the CSV file.

- Change it's encoding with `iconv -c -t utf8 inputDB.csv > inputDB.utf8.csv` inside `input_data/`

- Create the folder where PostgreSQL will save the data: `mkdir ./postgres_data`

- Build with `docker-compose up -d --build` and then `docker-compose up`
