import boto3
import botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET


s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, bucket_name, acl="public-read"):

    try:

        s3.upload_fileobj(
            file,
            Config.S3_BUCKET,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        return f"{Config.S3_LOCATION}{file.filename}"

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

# def upload_file_to_s3(file, bucket_name, acl="public-read"):

#     ## upload logic here
#     ## ...
#     ## ...
#     ## ...

#     return "{}{}".format(app.config["S3_LOCATION"], file.filename)
