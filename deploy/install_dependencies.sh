#!/bin/bash

cd /home/ec2-user/anuj-test && python3 -m virtualenv env
source /home/ec2-user/anuj-test/env/bin/activate

###
#in virtualenv
###

pip install -r /home/ec2-user/anuj-test/requirements.txt
sqlite3 database.db < /home/ec2-user/anuj-test/database.sql
