from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json
from typing import cast
from database import supabase, SUPABASE_BUCKET, SUPABASE_URL
from models import EmployeeCreate, EmployeeUpdate
from forms import as_form

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_employees(request: Request):
    employees = []
    try:
        response = supabase.table('employees').select('*').eq('is_active', True).execute()
        if isinstance(response, str):
            response = json.loads(response)
            employees = response.get('data', [])
    except Exception as e:
        print("Error fetching employees:", e)
    print(employees)
    return templates.TemplateResponse("index.html", {"request": request, "employees": employees})

@router.get("/add", response_class=HTMLResponse)
async def add_employee_form(request: Request):
    return templates.TemplateResponse("add_employee.html", {"request": request})

@router.post("/add")
async def add_employee(
    request: Request,
    employee: EmployeeCreate = Depends(EmployeeCreate.as_form),# type: ignore[attr-defined]
    image: UploadFile = File(None)
):
    image_url = None
    if image and image.filename != "":
        image_filename = f"{employee.first_name}_{employee.last_name}_{image.filename}"
        file_content = await image.read()
        response = supabase.storage.from_(cast(str,SUPABASE_BUCKET)).upload(image_filename, file_content)
        
        if getattr(response, "status_code", None) == 200:
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{image_filename}"

    supabase.table('employees').insert({
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'salary': employee.salary,
        'image_url': image_url
    }).execute()

    return RedirectResponse("/", status_code=303)