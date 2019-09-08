import boto3
import sys


ec2=boto3.client("ec2",region_name=ap-south-1,aws_access_key_id=AKIAV3BUFEV3L7V5I3PL,aws_secret_access_key=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)
filter=[
	{
	"Name":"tag:Linux",
	"Value":"Linux"
	}
	]
instances=ec2.instances.filter(Filters=filter)
for instance in instances:
	instance.start()
