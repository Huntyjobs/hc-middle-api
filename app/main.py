import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from settings import Settings
from api.routes.catalog import catalog_router

settings = Settings()

app = FastAPI(
	title="HC-Middle API",
    description="API for Technical Test ",
    version="0.0.1",
	root_path=settings.ROOT_PATH,
	redoc_url=None,
)

app.include_router(catalog_router)

@app.get("/", include_in_schema=False)
async def root():
    return {"Hello": "HC-Middle API"}

@app.get("/hc-middle/openapi.json", include_in_schema=False)
async def root():
    return RedirectResponse("/openapi.json")

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
