#! /bin/bash

python list-bucket.py > output1.txt

data=( $(grep . output1.txt |cut -d= -f2) )

echo $data
python list-object.py $data
