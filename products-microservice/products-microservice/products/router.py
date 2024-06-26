from fastapi import APIRouter, status

from products.schemas import Product
from products.service import get_all_products, get_product_by_id, insert_product, update_product, delete_product

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", status_code=status.HTTP_200_OK)
def index():
    message = f'products retrieved!'

    products = get_all_products()
    if products == []:
        message = f'there are no products in db!'
    return {
        'status': status.HTTP_200_OK,
        'message': message,
        'data': products,
    }


@router.get("/{id}", status_code=status.HTTP_200_OK)
def show(id: str):
    message = f'product with id: "{id}" founded!'

    product = get_product_by_id(id)
    return {
        'status': status.HTTP_200_OK,
        'message': message,
        'data': product,
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def store(data: Product):
    id = insert_product(data)
    return {
        'status': status.HTTP_201_CREATED,
        'message': f'new product with id: {id} created!',
        'data': id,
    }


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(id: str, data: Product):
    product = update_product(id, data)
    return {
        'status': status.HTTP_200_OK,
        'message': f'product with id "{id} updated!"',
        'data': {
            'old_data': data,
            'new_data': product,
        },
    }


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy(id: str):
    if (delete_product(id)):
        return {
            'status': status.HTTP_200_OK,
            'message': f'product with id "{id} deleted!"',
            'data': None,
        }
