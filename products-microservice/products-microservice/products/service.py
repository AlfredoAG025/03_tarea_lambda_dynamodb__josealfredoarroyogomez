from fastapi import HTTPException, status

from database import products_table


from products.schemas import Product


def get_all_products():
    try:
        response = products_table.scan()
        products = response.get('Items', [])

        products = sorted(products, key=lambda x: x['creation_date'])
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_product_by_id(id: str):
    try:
        response = products_table.get_item(Key={'id': id})
        if 'Item' not in response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'product with id: "{id}" not founded!')
        product = response.get('Item', None)
        return product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def insert_product(data: Product):
    id = None
    try:
        response = products_table.put_item(
            Item=data.model_dump()
        )
        id = data.id
        return id
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def update_product(id: str, data: Product):
    try:
        product = get_product_by_id(id)

        response = products_table.update_item(
            Key={'id': id},
            UpdateExpression='set #name=:n, description=:d, price=:p',
            ExpressionAttributeNames={'#name': 'name'},
            ExpressionAttributeValues={
                ':n': data.name,
                ':d': data.description,
                ':p': data.price,
            },
            ReturnValues="UPDATED_NEW"
        )
        return response['Attributes']
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def delete_product(id: str):
    try:
        product = get_product_by_id(id)
        products_table.delete_item(Key={'id': id})
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
