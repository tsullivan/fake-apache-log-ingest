# fake-apache-log-ingest
This is the repo for fake apache log ingest

## Setup
Install Python dependency
```
pip3 install faker
```

Run the script
```
python3 ./generate_logs.py | \
ES_USERNAME=my_es_user \
ES_PASSWORD=my_es_password \
ES_HOST="localhost:9200" \
ES_CA_CERT=/Users/you/get/the/picture \
~/bin/filebeat/filebeat -c filebeat.yml
