#!/bin/sh
curl -A 'api-test-agent' 'https://api.hh.ru/vacancies?search_field=name&text='$1 | jq '.' > hh.json