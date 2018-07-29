#!/bin/bash

cd /home/ec2-user/anuj-test
source env/bin/activate

###
#in virtualenv
###

python portal.py > /dev/null 2>&1 &