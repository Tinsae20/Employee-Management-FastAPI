from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import employee_routes

app = FastAPI()

# Moutnt the static files directory
app.mount("/static", StaticFiles(directory="./fast-api-project/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="./fast-api-project/templates")

# Include routers
app.include_router(employee_routes.router) # type: ignore

