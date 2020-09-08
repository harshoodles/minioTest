from minio import Minio
from minio.error import ResponseError
import sys

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('localhost:9000',
                    access_key='serverkey',
                    secret_key='serversecret',
                    secure=False)
n = len(sys.argv) 
for i in range(1, n):
# Get a full object
 try:
      minioClient.fget_object('bucket01', sys.argv[i], '/home/harsh/snap/%s' %sys.argv[i] )
 except ResponseError as err:
      print(err)
      print('Hello  "%s"' %sys.argv[i] )

# run like this $ python file-downloader.py Selection_011.png
