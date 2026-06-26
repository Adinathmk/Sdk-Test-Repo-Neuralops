from fastapi import APIRouter, BackgroundTasks
import logging
import uuid
from app.schemas.order import OrderCheckoutRequest, OrderResponse
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["Orders"])
logger = logging.getLogger(__name__)

@router.post("/checkout")
def checkout(request: OrderCheckoutRequest):
    logger.info("Received POST /orders/checkout request")
    
    # This will crash with ZeroDivisionError
    final_amount = order_service.process_checkout(request.customer_id, request.items)
    
    order_id = str(uuid.uuid4())
    return {"order_id": order_id, "total_amount": final_amount, "status": "completed"}

@router.get("/{order_id}")
def get_order(order_id: str):
    logger.info(f"Received GET /orders/{order_id} request")
    
    order = order_service.fetch_order(order_id)
    
    # This will crash with AttributeError because order is None
    logger.info("Order retrieved, mapping to response...")
    response = OrderResponse(
        order_id=order_id,
        total_amount=order.total_amount, # Crashes here
        status=order.status
    )
    return response

@router.post("/background-sync")
def background_sync(order_id: str, background_tasks: BackgroundTasks):
    logger.info(f"Received POST /orders/background-sync for order {order_id}")
    background_tasks.add_task(order_service.sync_order_to_warehouse, order_id)
    return {"message": "Sync started in background", "order_id": order_id}
