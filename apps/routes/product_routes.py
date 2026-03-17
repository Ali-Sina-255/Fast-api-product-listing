from fastapi import APIRouter

from apps.models.models import Product, ProductSchema

router = APIRouter()


@router.get("/")
def home():
    return {"message": "API is running"}


products = [
    Product(
        id=1, name="Phone", description="for test in this time", price=400, quantity=2
    ),
    Product(
        id=2,
        name="Phone2",
        description="for test in this time 2",
        price=400,
        quantity=2,
    ),
    Product(
        id=3,
        name="Phone3",
        description="for test in this time 3",
        price=400,
        quantity=2,
    ),
    Product(
        id=4,
        name="Phone4",
        description="for test in this time 4",
        price=400,
        quantity=2,
    ),
]


@router.get("/products")
def get_all_products():
    return products


# @router.get("/products/{id}")
# def get_product(id: int):
#     for product in products:
#         if product.id == id:
#             return {
#                 "id": product.id,
#                 "name": product.name,
#                 "description": product.description,
#                 "price": product.price,
#                 "qty": product.quantity,
#             }
#     return {"message": "Product not found"}


@router.get("/products/{id}")
def get_product(id: int):
    product = next((p for p in products if p.id == id), None)

    if product:
        return product

    return {"message": "Product not found"}


@router.post("/products")
def create_product(product: ProductSchema):
    new_product = Product(
        id=len(products) + 1,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
    )

    products.append(new_product)

    return new_product.__dict__


# @router.put("/products/{id}")
# def update_product(id: int, updated_product: Product):
#     for index, product in enumerate(products):
#         if product.id == id:
#             products[index] = updated_product
#             return updated_product

#     return {"message": "Product not found"}


@router.put("/products/{id}")
def update_product(id: int, updated_product: Product):

    product = next((p for p in products if p.id == id), None)

    if not product:
        return {"message": "Product not found"}

    product.name = updated_product.name
    product.description = updated_product.description
    product.price = updated_product.price
    product.quantity = updated_product.quantity

    return product


@router.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            deleted_product = products.pop(index)
            return {"message": "Product deleted", "product": deleted_product}

    return {"message": "Product not found"}
