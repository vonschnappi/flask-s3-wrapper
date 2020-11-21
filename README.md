# Flask wrapper for S3

This Flask app allows you to list buckets, folders, get info about files and download them.

## Motivation for this app

This Flask S3 wrapper was born out of the idea that some clients or employees need access to content in S3 buckets, but cannot be given access to AWS console for whatever reason.

There are plenty desktop based S3 wrappers out there, but I felt that a web based one would be easier to implement and work with.

## Stack
These are the technologies and packages used in this app:
### Python3
* Flask for web server
* Jinja for templating
* Boto3 for S3 actions

### Web Dev
* HTML + CSS + JS
* Jquery
* [Pagination.js](https://pagination.js.org/) - for paginating large lists of objects, files and folders.
* [Font Awesome](https://fontawesome.com/)

## AWS Credentials for Boto3
This app was developed with admin creds so it had all the necessary permissions to list, view and download files and folders from various buckets. You will have to pass valid AWS credentials to this app to allow it to list buckets and view and download files and folders. The level of and granularity of permissions is up to you.

To learn more about passing credentials to the Boto3 client, see [Boto3 Crednetials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html). Boto3 client init takes place in [helpers/aws/s3_helper.py](helpers/aws/s3_helper.py).

## Running the Application Locally
1. Make sure that you have valid AWS credentials in your environment, or that you have passed such credentials to the Boto3 client.
2. Initialize a Python virtual environment: `python3 -m venv .`
3. Install the necessary pip packages: `pip install -r requirements.txt`
4. Run the app: `python3 app.py`

## Deploying the Application
Deploying the application to the cloud for testing or production purposes is solely the responsiblity of whoever clones or forks this repo. Please see [licence](/LICENSE.txt).

When you run this app locally, it will shoot out the following warning:
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
DON'T DEPLOY THE APP LIKE THAT TO YOU PRODUCTION ENVIRONMENT! Read Flask's docs on [how to properly deploy a Flask App](https://flask.palletsprojects.com/en/master/deploying/).

## WIP
There are still a few things missing in this app that I would like to add. I'll do my best to add them soon:
1. Search
2. Breadcrumbs
3. Better error handling
4. Logging

If you have any ideas, feel free to open an issue.
