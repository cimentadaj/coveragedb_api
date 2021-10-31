# COVerAGE-DB API

A web API for querying the COVerAGE-DB: a global demographic database of COVID-19 cases and deaths.


- Deposit `inputDB.csv` inside `input_data` and run `awk 'NR>1' inputDB.csv > tmp.csv && mv tmp.csv inputDB.csv` on it. That will remove the first line of the CSV file.

- Change it's encoding with `iconv -c -t utf8 inputDB.csv > inputDB.utf8.csv` inside `input_data`
