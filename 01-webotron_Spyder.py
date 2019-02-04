# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:46:38 2019
1
@author: Jim
"""

import boto3

session = boto3.Session(profile_name='pythonAutomation')

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)
    
    