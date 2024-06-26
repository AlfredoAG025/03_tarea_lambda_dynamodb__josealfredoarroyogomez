from fastapi import FastAPI
from products.router import router as products_router
from mangum import Mangum

app = FastAPI(
    title="Products Microservice",
    version="1.0.0",
)

handler = Mangum(app)

app.include_router(router=products_router, prefix="/api")
