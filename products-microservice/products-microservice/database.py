import boto3

dynamodb = boto3.resource('dynamodb')

products_table = dynamodb.Table('ProductsTable')
