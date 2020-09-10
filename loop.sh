#! /bin/bash

#python list-bucket.py > output1.txt

#data=( $(grep . output1.txt |cut -d= -f2) )

UPLOAD_TO_TARGET=$1

python3 list-object.py bucket01 > output2.txt

filename=output2.txt
while read -r line; do
    name="$line"
  python3 file-downloader.py $name

done < "$filename"

if [ $UPLOAD_TO_TARGET = "true" ]
then

filename=output2.txt
while read -r line; do
    name="$line"
  python3 file-uploader.py $name

done < "$filename"
echo "Uploaded in Target MinIO"

else

	echo "Downloaded Successfully!!"
fi
