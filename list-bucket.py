from minio import Minio
from minio.error import ResponseError

#bucket='bucket01'
# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)

buckets = minioClient.list_buckets()

for bucket in buckets:
    print(bucket.name)


#run like this $ python list-object.py bucket01 test
