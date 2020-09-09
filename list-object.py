from minio import Minio
from minio.error import ResponseError
import sys

#bucket='bucket01'
# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('localhost:9000',
                    access_key='serverkey',
                    secret_key='serversecret',
                    secure=False)

n = len(sys.argv) 
for i in range(1, n): 
#    print(sys.argv[i], end = " ") 

  objects = minioClient.list_objects(sys.argv[i],
                              recursive=True)
  for obj in objects:
      print( obj.object_name)

# run this like $ python list-object.py bucketName
