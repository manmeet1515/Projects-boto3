import boto3
ec2 = boto3.client('ec2')


# #stop instance
response = ec2.stop_instances(
    InstanceIds=[
        'i-024ba25773f076d46',
    ],
)

print(response)

# #Start instance
response = ec2.start_instances(
    InstanceIds=[
        'i-024ba25773f076d46',
    ],
)

print(response)


# # describe specific instance

response = ec2.describe_instances(
    InstanceIds=[
        'i-00d524f841258fc73',
    ],
)

print(response)