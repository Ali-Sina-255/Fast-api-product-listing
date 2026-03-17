from fastapi import APIRouter, Depends
from sqlalchemy import select  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from apps.config.db import get_session
from apps.models.models import Product, ProductSchema

router = APIRouter()


# =========================
# HOME
# =========================
@router.get("/")
async def home():
    return {"message": "API is running"}


# =========================
# GET ALL PRODUCTS
# =========================
@router.get("/products")
async def get_all_products(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


# =========================
# GET SINGLE PRODUCT
# =========================
@router.get("/products/{id}")
async def get_product(id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Product).where(Product.id == id))
    product = result.scalar_one_or_none()

    if not product:
        return {"message": "Product not found"}

    return product


# =========================
# CREATE PRODUCT
# =========================
@router.post("/products")
async def create_product(
    product: ProductSchema, db: AsyncSession = Depends(get_session)
):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


# =========================
# UPDATE PRODUCT
# =========================
@router.put("/products/{id}")
async def update_product(
    id: int, updated_product: ProductSchema, db: AsyncSession = Depends(get_session)
):
    result = await db.execute(select(Product).where(Product.id == id))
    product = result.scalar_one_or_none()

    if not product:
        return {"message": "Product not found"}

    for key, value in updated_product.model_dump().items():
        setattr(product, key, value)

    await db.commit()
    await db.refresh(product)

    return product


# =========================
# DELETE PRODUCT
# =========================
@router.delete("/products/{id}")
async def delete_product(id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Product).where(Product.id == id))
    product = result.scalar_one_or_none()

    if not product:
        return {"message": "Product not found"}

    await db.delete(product)
    await db.commit()

    return {"message": "Product deleted"}
