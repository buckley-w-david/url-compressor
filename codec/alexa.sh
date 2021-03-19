#!/usr/bin/bash
wget 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
unzip top-1m.csv.zip
echo -e "id,url\n$(cat top-1m.csv)" > top-1m.csv
# sed -i 's/\([0-9][0-9]*\),\(.*\)/\1,https:\/\/\2/g' top-1m.csv
