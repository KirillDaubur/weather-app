#!/bin/bash

if [ -z "$S3_BUCKET_NAME" ]; then
  echo "Error: BUCKET_NAME is not set. Make sure it's defined in the .env file."
  exit 1
fi

awslocal s3 mb s3://$S3_BUCKET_NAME