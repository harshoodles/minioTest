#! /bin/bash

a=1

while [ $a -lt 10 ]
do
  python3 list-object.py bucket01 > output2.txt

  filename=output2.txt
  while read -r line; do
      name="$line"
    python3 file-downloader.py "$name"

  done < "$filename"

  filename=output2.txt
  while read -r line; do
      name="$line"
    python3 file-uploader.py "$name"

  done < "$filename"

done
