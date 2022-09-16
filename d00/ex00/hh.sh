curl  https://api.hh.ru/vacancies?text=$1 | jq '.' > hh.json
