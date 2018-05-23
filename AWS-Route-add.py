import boto3

client = boto3.client("ec2")

##The below lines will replace the route in the specfied route table##

c2=client.replace_route(

    RouteTableId='string',
    DestinationCidrBlock='string',
#    GatewayId='vgw-efce10f1',
)


##The below lines will print out the route table after the changes are made##

response = client.describe_route_tables(
    RouteTableIds=[
        'string',
    ],
)

print(response)
