import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    instance_ids = ['i-0123456789abcdef0']  # replace with your instance ID

    response = ec2.stop_instances(
        InstanceIds=instance_ids
    )

    return {
        'statusCode': 200,
        'body': f'Stopped instance(s): {instance_ids}'
    }


