#! /bin/bash

#python list-bucket.py > output1.txt

#data=( $(grep . output1.txt |cut -d= -f2) )


python list-object.py bucket01 > output2.txt

filename=output2.txt
while read -r line; do
    name="$line"
  python file-downloader.py $name

done < "$filename"

filename=output2.txt
while read -r line; do
    name="$line"
  python file-uploader.py $name

done < "$filename"

