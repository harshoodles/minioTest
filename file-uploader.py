# Import MinIO library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
import sys
# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('localhost:9001',
                    access_key='2ndserverkey',
                    secret_key='2ndserversecret',
                    secure=False)

# Make a bucket with the make_bucket API call.
try:
       minioClient.make_bucket("targetbucket")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise
n = len(sys.argv) 
for i in range(1, n):
# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
 try:
       minioClient.fput_object('targetbucket', sys.argv[i], './minIO/%s' %sys.argv[i])
 except ResponseError as err:
       print(err)
