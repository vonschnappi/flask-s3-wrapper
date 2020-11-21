import boto3
import io

class S3Helper():
    def __init__(self):
        self.client = boto3.client('s3')

    def __is_upper_folder(self, obj):
        count = 0
        for c in obj:
            if c == '/':
                count += 1
            if count > 1:
                return False
        return True

    def get_buckets(self):
        buckets = self.client.list_buckets()['Buckets']
        return [bucket['Name'] for bucket in buckets]
    
    def get_bucket_objects(self, bucket):
        folder_file_mapping = {'folders': [], 'files': []}
        objects = None
        try:
            objects = self.client.list_objects_v2(Bucket=bucket)['Contents']
        except Exception as e:
            return objects
        for obj in objects:
            if obj['Key'].endswith('/') and self.__is_upper_folder(obj['Key']):
                folder_file_mapping['folders'].append(obj['Key'])
            elif '/' not in obj['Key']:
                folder_file_mapping['files'].append(obj['Key'])
        return folder_file_mapping

    def get_folder_contents(self, bucket, prefix):
        folder_file_mapping = {'folders': [], 'files': []}
        folder_contents = None
        try:
            folder_contents = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)['Contents']
        except Exception as e:
            return folder_contents
        for obj in folder_contents:
            if obj['Key'].endswith('/') and obj['Key'] != prefix + '/':
                folder_file_mapping['folders'].append(obj['Key'].split('/')[1] + '/')
            elif obj['Key'] == prefix + '/' + obj['Key'].split('/')[-1] and obj['Key'] != prefix + '/':
                folder_file_mapping['files'].append(obj['Key'].split('/')[-1])
        return folder_file_mapping

    def get_single_bucket_object(self, bucket, key):
        obj = None
        try:
            obj = self.client.get_object(Bucket=bucket, Key=key)
        except Exception as e:
            return obj
        return obj
    
    def download_object(self, bucket, key):
        b = io.BytesIO()
        print('Downloading', bucket, key)
        obj = self.client.get_object(Bucket=bucket, Key=key)
        data = obj['Body'].read()
        b.write(data)
        b.seek(0)
        return b
        

