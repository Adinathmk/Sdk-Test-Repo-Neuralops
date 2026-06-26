from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCheckoutRequest(BaseModel):
    customer_id: str
    items: List[OrderItem]

class OrderResponse(BaseModel):
    order_id: str
    total_amount: float
    status: str
