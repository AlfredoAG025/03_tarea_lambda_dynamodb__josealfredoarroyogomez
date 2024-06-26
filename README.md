# 03_tarea_lambda_dynamodb

## Endpoints

**base_url=https://sgie9f8kh4.execute-api.us-east-1.amazonaws.com/Prod/api/**

### GET: /products

Get all products

### GET: /products/{id:str}

Get one product by id

### POST: /products/

Store one product

#### Body

{
    name: str,
    description: str,
    price: float
}

### PUT: /products/{id:str}

Updates one product

#### Body

{
    name: str,
    description: str,
    price: float
}

### DELETE: /products/{id:str}

deletes one product by id
