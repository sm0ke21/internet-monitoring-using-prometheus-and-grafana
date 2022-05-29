#!/bin/bash
file=$(mktemp)
./speedtest --server-id=${SERVERID} --accept-gdpr --accept-license > $file
python extract.py $file ${PROJECTNAME}