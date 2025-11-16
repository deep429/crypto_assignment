from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Crypto MCP Server", version="1.0")
app.include_router(router)
