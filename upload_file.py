#!/usr/bin/env python3
import os.path
import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('./cfnlambda', 'vijeshec2cfn', 'cfnlambda')