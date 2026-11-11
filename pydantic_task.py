# have to build pydantic model for api request and response
from pydantic import BaseModel, Field, computed_field

# api request
class Requestbody(BaseModel):
    product_name: str = Field(min_length=10, max_length=100)
    price: float = Field(gt=0)
    total_stock: int = Field(gt=0)

product1 = {'product_name':'Johnsons baby lotion', 'price': 17.9, 'total_stock': 20}
product = Requestbody(**product1)
print("create_product:", product.model_dump())

# api response
class Responsebody(BaseModel):
    id: int
    product_name: str
    price: float
    total_stock: int
    
    @computed_field
    @property
    def message(self)->str:
        if self.total_stock > 0:
            return "product created successfully"
        return "product is out of stock"

def product_response(product: Responsebody):
    responsebody={
        'id': '101',
        'product_name': product.product_name,
        'price': product.price,
        'total_stock': product.total_stock,
        'message': product.message
    }
    print("response created: ", responsebody)

response_dict1 = {
    'id': '101',
    'product_name': product.product_name,
    'price': product.price,
    'total_stock': product.total_stock
}
p_response = Responsebody(**response_dict1)
product_response(p_response)