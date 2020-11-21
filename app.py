from flask import Flask, render_template, url_for, request, send_file
from helpers.aws.s3_helper import S3Helper
from helpers.template.render_helper import RendereHelper
s3_helper = S3Helper()
rndr_helper = RendereHelper()

app = Flask(__name__)

@app.route('/')
@app.route('/', defaults={'path': ''})
def index():
    buckets = s3_helper.get_buckets()
    return rndr_helper.list_buckets(buckets)

@app.route('/bucket/<bucket>')
def list_bucket(bucket):
    files_and_folders = s3_helper.get_bucket_objects(bucket)
    print(files_and_folders)
    return rndr_helper.list_bucket_contents(bucket, files_and_folders)

@app.route('/bucket/<path:path>')
def show_object(path):
    bucket, obj, contents = "", "", ""
    split_path = path.split('/', 1)
    bucket = split_path[0]
    if path.endswith('/'):
        obj = "".join(split_path[1].rsplit('/', 1))
        files_and_folders = s3_helper.get_folder_contents(bucket, obj)
        return rndr_helper.list_folder_contents(bucket, obj, files_and_folders)
    else:
        obj = split_path[1]
        obj_info = s3_helper.get_single_bucket_object(bucket, obj)
        return rndr_helper.show_file(bucket, obj, obj_info)

@app.route('/download/<path:path>')
def download_file(path):
    bucket, obj, = "", ""
    split_path = path.split('/', 1)
    bucket = split_path[0]
    obj = split_path[1]
    file_name = obj.split('/')[-1]
    file_data = s3_helper.download_object(bucket, obj)
    return send_file(
        file_data,
        as_attachment = True,
        attachment_filename=file_name,
    )

if __name__ == "__main__":
    app.run()