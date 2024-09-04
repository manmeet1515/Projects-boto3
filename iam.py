import boto3
import boto3.session
iam = boto3.client('iam')

response = iam.list_roles()

# print(response)

for role in response["Roles"]:
    print(f"Role Name - {role['RoleName']}")
    print(f"Create Date - {role['CreateDate']}")
    print(f"Assume Role Document - {role['AssumeRolePolicyDocument']}")

response = iam.list_users()
print(response)
for user in iam.list_users()["Users"]:
    print(f"User Name is - {user['UserName']}")
    print(f"User Id is - {user['UserId']}")

