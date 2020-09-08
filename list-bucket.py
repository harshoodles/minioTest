from minio import Minio
from minio.error import ResponseError

#bucket='bucket01'
# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('localhost:9000',
                    access_key='serverkey',
                    secret_key='serversecret',
                    secure=False)

buckets = minioClient.list_buckets()

for bucket in buckets:
    print(bucket.name)


#run like this $ python list-object.py bucket01 test
