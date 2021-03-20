import boto3
import pandas as pd


class ImportData:

    key_list = None

    def __init__(self, bucket, prefix, file_extension=".csv", aws_access_key_id=None, aws_secret_access_key=None, verify=True):
        self.bucket = bucket
        self.prefix = prefix
        self.file_extension = file_extension
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.verify = verify

    def retrieve_objects(self):
        client = boto3.client('s3',
                              aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key,
                              verify=self.verify
                              )

        objects = client.list_objects(Bucket=self.bucket,
                                      Prefix=self.prefix)

        if objects['ResponseMetadata']['HTTPStatusCode'] == 200:

            self.key_list = [obj['Key'] for obj in objects['Contents'] if obj['Key'].endswith(self.file_extension)]

        else:
            raise Exception

        return self

    def return_dataframe(self):
        df_list = []
        for key in self.key_list:
            temp_df = pd.read_csv("s3://" + self.bucket + "/" + key, low_memory=False)
            df_list.append(temp_df)

        return pd.concat(df_list)



#
#
# def import_data(bucket_name, prefix, file_extension, aws_access_key_id=None, aws_secret_access_key=None,verify=True):
#     client = boto3.client('s3',
#                           aws_access_key_id=aws_access_key_id,
#                           aws_secret_access_key=aws_secret_access_key,
#                           verify=verify
#                           )
#     bucket = client.get_bucket(bucket_name)
#     bucket.objects.filter(prefix=prefix)
