from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    # id: int
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attribute=True)

    id: int
