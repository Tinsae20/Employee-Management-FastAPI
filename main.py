from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import employee_routes, auth_routes
from auth import auth_middleware

app = FastAPI()

# Moutnt the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# auth middleware
app.middleware('http')(auth_middleware)

# Include routers
app.include_router(employee_routes.router)
app.include_router(auth_routes.router)


