# COVerAGE-DB API

A web API for querying the COVerAGE-DB: a global demographic database of COVID-19 cases and deaths.

## Steps to deploy database and API

- Create `./backend/.env` file with the template from `./backend/.env.template`. For now (not secret at this moment), fill with these (be sure to look at the template in case this hasn't been updated):

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

### ** All of the code below needs to be run from the root of the repo **

- Deposit `inputDB.csv` inside `./input_data` and run `awk 'NR>1' ./input_data/inputDB.csv > ./input_data/tmp.csv && mv ./input_data/tmp.csv ./input_data/inputDB.csv` on it. That will remove the first line of the CSV file.

- Change it's encoding with `iconv -c -t utf8 ./input_data/inputDB.csv > ./input_data/inputDB.utf8.csv` inside `input_data/`

- Create the folder where PostgreSQL will save the data: `mkdir ./postgres_data`

- Build with `docker-compose up -d --build` and then `docker-compose up`. For the data to be successfuly imported, wait for the `***** Database migration successful ****`. It should after the line `coveragedb_api-server-1  | Create Date: 2021-10-30 16:49:10.949972`.

- In a separate shell (leave the docker container running), confirm the database has been created with `docker-compose exec db psql -h localhost -U postgres --dbname=postgres -c "select * from coveragedb limit 5;"`. You should see something like this:

```
   Country   | Region |     Code      |    Date    | Sex | Age | AgeInt | Metric | Measure | Value | Short 
-------------+--------+---------------+------------+-----+-----+--------+--------+---------+-------+-------
 1           | All    | EE_01.12.2020 | 01.12.2020 | m   | 80  |      5 | Count  | Tests   |  4001 | EE
 Afghanistan | All    | AF01.07.2020  | 01.07.2020 | b   | 0   |     10 | Count  | Cases   |   169 | AF
 Afghanistan | All    | AF01.07.2020  | 01.07.2020 | b   | 10  |     10 | Count  | Cases   |  1525 | AF
 Afghanistan | All    | AF01.07.2020  | 01.07.2020 | b   | 20  |     10 | Count  | Cases   |  7948 | AF
 Afghanistan | All    | AF01.07.2020  | 01.07.2020 | b   | 30  |     10 | Count  | Cases   |  7592 | AF
(5 rows)
```
