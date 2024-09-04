import boto3
# import json
# iam = boto3.client('iam')
s3 = boto3.client('s3')

response = s3.delete_bucket(
    Bucket='testbucketfromboto3',
)

# response = iam.list_roles()

# print(response)

# for role in response["Roles"]:
#     print(f"Role Name - {role['RoleName']}")
#     print(f"Create Date - {role['CreateDate']}")
#     print(f"Assume Role Document - {role['AssumeRolePolicyDocument']}")



# #stop instance
# response = ec2.stop_instances(
#     InstanceIds=[
#         'i-024ba25773f076d46',
#     ],
# )

# print(response)

# #Start instance
# response = ec2.start_instances(
#     InstanceIds=[
#         'i-024ba25773f076d46',
#     ],
# )

# print(response)


# # describe specific instance

# response = ec2.describe_instances(
#     InstanceIds=[
#         'i-00d524f841258fc73',
#     ],
# )

# print(response)