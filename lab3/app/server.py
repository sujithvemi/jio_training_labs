from fastapi import FastAPI

from .lab.apis import routes

app = FastAPI()
app.include_router(routes.router)