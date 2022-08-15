import boto3
import json

s3_client = boto3.client('s3')
elb_client = boto3.client('elbv2')


def lambda_handler(event, context):
	lb_list= elb_client.describe_load_balancers(PageSize=400)
	for lb in lb_list["LoadBalancers"]:
		arn = lb["LoadBalancerArn"]
		access_log_enabled = elb_client.describe_load_balancer_attributes(LoadBalancerArn=arn)["Attributes"][0]["Value"]
		if access_log_enabled == 'false':
			name = lb["LoadBalancerName"]
			print(name.lower()+ "access logs disabled ")

