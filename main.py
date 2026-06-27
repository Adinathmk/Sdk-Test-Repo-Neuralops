import neuralops
import os
from dotenv import load_dotenv

# Load variables from .env into os.environ
load_dotenv()

#  Initialize NeuralOps FIRST
neuralops.init(
    api_key=os.environ.get("NEURALOPS_API_KEY", "test-api-key"),
    ingest_url="http://localhost/api/v1/ingest/logs", 
    service_name="fastapi-testbed",
    environment="development",
)


from fastapi import FastAPI
import logging
from app.core.config import setup_logging
from app.api.orders import router as orders_router

# Initialize standard logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="E-commerce Orders API", description="Testbed for observability SDK")

# Include routers
app.include_router(orders_router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the standard FastAPI service...")

@app.get("/")
def root():
    return {
        "message": "Welcome to the E-commerce Orders API testbed",
        "docs_url": "/docs",
        "health_check": "/health"
    }

@app.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "ok"}
