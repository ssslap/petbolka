"""
Маршруты (routes) для ветеринарной клиники
"""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from datetime import date, time

from .models import DOCTORS, SERVICES, CLINIC_INFO, ContactForm, AppointmentForm

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Главная страница"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "clinic": CLINIC_INFO,
            "services": SERVICES[:4],  # Показываем только 4 услуги на главной
            "doctors": DOCTORS[:3],    # Показываем только 3 врачей на главной
        }
    )


@router.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    """Страница услуг"""
    return templates.TemplateResponse(
        "services.html",
        {
            "request": request,
            "clinic": CLINIC_INFO,
            "services": SERVICES,
        }
    )


@router.get("/doctors", response_class=HTMLResponse)
async def doctors(request: Request):
    """Страница врачей"""
    return templates.TemplateResponse(
        "doctors.html",
        {
            "request": request,
            "clinic": CLINIC_INFO,
            "doctors": DOCTORS,
        }
    )


@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Страница контактов"""
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "clinic": CLINIC_INFO,
        }
    )


@router.get("/appointment", response_class=HTMLResponse)
async def appointment(request: Request):
    """Страница записи на прием"""
    return templates.TemplateResponse(
        "appointment.html",
        {
            "request": request,
            "clinic": CLINIC_INFO,
            "doctors": DOCTORS,
            "services": SERVICES,
        }
    )


# API эндпоинты для обработки форм (для разработки)
@router.post("/api/contact")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    phone: Optional[str] = Form(None),
    message: str = Form(...)
):
    """Обработка формы обратной связи"""
    # В реальном приложении здесь была бы отправка email или сохранение в БД
    return {
        "status": "success",
        "message": "Ваше сообщение отправлено! Мы свяжемся с вами в ближайшее время."
    }


@router.post("/api/appointment")
async def submit_appointment(
    pet_name: str = Form(...),
    pet_type: str = Form(...),
    owner_name: str = Form(...),
    owner_email: str = Form(...),
    owner_phone: str = Form(...),
    doctor_id: int = Form(...),
    appointment_date: str = Form(...),
    appointment_time: str = Form(...),
    notes: Optional[str] = Form(None)
):
    """Обработка формы записи на прием"""
    # В реальном приложении здесь была бы запись в БД
    doctor = next((d for d in DOCTORS if d.id == doctor_id), None)
    doctor_name = doctor.name if doctor else "Не указан"
    
    return {
        "status": "success",
        "message": f"Вы записаны на прием к врачу {doctor_name} на {appointment_date} в {appointment_time}."
    }


# API для получения данных (JSON)
@router.get("/api/doctors")
async def get_doctors():
    """Получить список врачей"""
    return {"doctors": [d.model_dump() for d in DOCTORS]}


@router.get("/api/services")
async def get_services():
    """Получить список услуг"""
    return {"services": [s.model_dump() for s in SERVICES]}


@router.get("/api/clinic")
async def get_clinic_info():
    """Получить информацию о клинике"""
    return {"clinic": CLINIC_INFO}
