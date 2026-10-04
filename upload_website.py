import boto3

bucket_name = "rutuja-static-website-2026-103"
region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)

s3.upload_file(
    "index.html",
    bucket_name,
    "index.html",
    ExtraArgs={"ContentType": "text/html"}
)

s3.upload_file(
    "style.css",
    bucket_name,
    "style.css",
    ExtraArgs={"ContentType": "text/css"}
)

s3.upload_file(
    "script.js",
    bucket_name,
    "script.js",
    ExtraArgs={"ContentType": "application/javascript"}
)

print("Website files uploaded successfully!")