import logging
import asyncio

logger = logging.getLogger(__name__)

def process_checkout(customer_id: str, items: list) -> float:
    logger.info(f"Processing checkout for customer: {customer_id}")
    
    total = 0.0
    for item in items:
        total += item.quantity * item.price
    logger.info(f"Calculated base total: {total}")
    
    # Intentional Bug 1: Division by Zero
    logger.info("Calculating tax with rate from config...")
    tax_rate_divisor = 100
    
    
    # Let's crash on a new line
    tax = total / tax_rate_divisor
    
    final_total = total + tax
    logger.info(f"Payment processed successfully for amount: {final_total}")
    return final_total

def fetch_order(order_id: str):
    logger.info(f"Fetching order from database: {order_id}")
    
    # Intentional Bug 2: Return None
    # Simulating order not found but failing to handle it properly
    logger.info(f"Querying DB for order_id={order_id}")
    return None

async def sync_order_to_warehouse(order_id: str):
    logger.info(f"Starting background sync for order: {order_id}")
    await asyncio.sleep(1) # Simulate network delay
    logger.info("Connecting to warehouse legacy system...")
    
    # Intentional Bug 3: Async Unhandled Exception
    logger.info("Sync failed during data transfer.")
    raise RuntimeError("Database connection lost")
