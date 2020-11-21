from flask import render_template
from base64 import b64encode

class RendereHelper():

    def __init__(self):
        self.text_based_types = [
            'text/css',    
            'text/csv',   
            'text/html',    
            'text/javascript',    
            'text/plain',    
            'text/xml'
        ]
        self.applocation_text_based_types = [
            'application/xml',    
            'application/json',   
            'application/javascript',    
            'application/xhtml+xml'
        ]

    def list_buckets(self, buckets):
        return render_template('index.html', 
                                title="List of S3 Buckets", 
                                buckets=buckets)
    
    def list_bucket_contents(self, bucket, files_and_folders):
        return render_template('bucket.html', 
                        title=f"List of {bucket} objects", 
                        bucket=bucket, 
                        files_and_folders=files_and_folders,
                        list=list)

    def list_folder_contents(self, bucket, folder, files_and_folders):
        return render_template('folder.html', 
                                title=f'Object list in {bucket}/{folder}', 
                                bucket=bucket, 
                                folder=folder, 
                                files_and_folders=files_and_folders)


    def show_file(self, bucket, file, info):
        return render_template('file.html', 
                                title=file, bucket=bucket, 
                                file=file, 
                                info=info,
                                b64encode=b64encode,
                                text_based_types=self.text_based_types,
                                applocation_text_based_types=self.applocation_text_based_types)

