#Code for stopping the instances

import boto3
#Enter the region your instances are in. Include only the region without specifying Availability zone; e.g. 'us-east-1'
region = 'us-west-2'
#Enter your instances here: ex. ['x-xxxxx', 'xxxxxxxxxxx']
instances = ['i-084b647o238377e5']
"""
event – AWS Lambda uses this parameter to pass in event data to the handler. This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type.

context – AWS Lambda uses this parameter to provide runtime information to your handler. This parameter is of the LambdaContext type.
"""
def lambda_handlers(event, context):
	ec2 = boto3.client('ec2', region_name=region)
	ec2.stop_instances(InstanceIds=instances)
	print 'stopped your instances: ' + str(instances)


#Code for starting the instances
import boto3
#Enter the region your instances are in. Include only the region without specifying Availability zone; e.g. 'us-east-1'
region = 'us-west-2'
#Enter your instances here: ex. ['x-xxxxx', 'xxxxxxxxxxx']
instances = ['i-084b647o238377e5']

def lambda_handlers(event, context):
	ec2 = boto3.client('ec2', region_name=region)
	ec2.start_instances(InstanceIds=instances)
	print 'stopped your instances: ' + str(instances)

==========================================================================
1.Go to cloud watch , under rule section 
a.click on create rule
b.select scheduler
c.under scheduler click on cron expression
d.on same page right hand side under Target section in lambda function select your function