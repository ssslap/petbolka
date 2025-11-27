"""
Модели данных для ветеринарной клиники
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time


class Doctor(BaseModel):
    """Модель врача"""
    id: int
    name: str
    specialization: str
    photo: str
    resume: str
    experience_years: int


class Service(BaseModel):
    """Модель услуги"""
    id: int
    name: str
    description: str
    price: float
    duration_minutes: int


class ContactForm(BaseModel):
    """Модель формы обратной связи"""
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str


class AppointmentForm(BaseModel):
    """Модель формы записи на прием"""
    pet_name: str
    pet_type: str
    owner_name: str
    owner_email: EmailStr
    owner_phone: str
    doctor_id: int
    appointment_date: date
    appointment_time: time
    notes: Optional[str] = None


# Примеры данных врачей
DOCTORS = [
    Doctor(
        id=1,
        name="Әлиева Айгүл Серікқызы",
        specialization="Терапевт, хирург",
        photo="/static/images/doctor1.svg",
        resume="Қазақ ұлттық аграрлық университетін бітірген. Үй жануарларын емдеу және хирургия саласында 10 жылдан астам тәжірибесі бар.",
        experience_years=10
    ),
    Doctor(
        id=2,
        name="Сәрсенбаев Нұрлан Қайратұлы",
        specialization="Кардиолог, УЗИ-маманы",
        photo="/static/images/doctor2.svg",
        resume="Ветеринария ғылымдарының кандидаты. Жануарлардың жүрек-қан тамырлары жүйесінің ауруларын диагностикалау және емдеу саласының маманы.",
        experience_years=15
    ),
    Doctor(
        id=3,
        name="Тұрсынова Дана Маратқызы",
        specialization="Дерматолог, аллерголог",
        photo="/static/images/doctor3.svg",
        resume="Жануарлардың тері аурулары мен аллергия саласының маманы. Халықаралық конференцияларда біліктілігін үнемі арттырып отырады.",
        experience_years=8
    ),
    Doctor(
        id=4,
        name="Омаров Ерлан Бауыржанұлы",
        specialization="Стоматолог, офтальмолог",
        photo="/static/images/doctor4.svg",
        resume="Жануарлардың тіс және көз ауруларының маманы. Күрделі стоматологиялық операциялар жүргізеді.",
        experience_years=12
    ),
]

# Примеры данных услуг
SERVICES = [
    Service(
        id=1,
        name="Бастапқы тексеру",
        description="Жануарды толық тексеру, дәрігердің кеңесі, қажет болған жағдайда емдеу тағайындау.",
        price=5000.0,
        duration_minutes=30
    ),
    Service(
        id=2,
        name="Вакцинация",
        description="Негізгі жұқпалы аурулардан вакцинация, ветеринариялық паспорт беру.",
        price=7000.0,
        duration_minutes=20
    ),
    Service(
        id=3,
        name="УДЗ диагностикасы",
        description="Ішкі органдарды ультрадыбыстық зерттеу, маман қорытындысы.",
        price=12000.0,
        duration_minutes=45
    ),
    Service(
        id=4,
        name="Рентген",
        description="Цифрлық өңдеумен рентгенографиялық зерттеу.",
        price=8000.0,
        duration_minutes=30
    ),
    Service(
        id=5,
        name="Қан анализі",
        description="Жалпы және биохимиялық қан анализі, нәтижелерді талдау.",
        price=6000.0,
        duration_minutes=15
    ),
    Service(
        id=6,
        name="Стерилизация/кастрация",
        description="Жануарды стерилизациялау немесе кастрациялау операциясы.",
        price=15000.0,
        duration_minutes=60
    ),
    Service(
        id=7,
        name="Тіс тазалау",
        description="Наркоз астында кәсіби ультрадыбыстық тіс тазалау.",
        price=12000.0,
        duration_minutes=45
    ),
    Service(
        id=8,
        name="Тырнақ қию",
        description="Иттер мен мысықтарға тырнақ қию.",
        price=1500.0,
        duration_minutes=15
    ),
    Service(
        id=9,
        name="Чиптеу",
        description="Жануарды сәйкестендіру үшін микрочип орнату, деректер базасына тіркеу.",
        price=5000.0,
        duration_minutes=10
    ),
    Service(
        id=10,
        name="Үйге шақыру",
        description="Жануарды тексеру және емдеу үшін дәрігердің үйге келуі.",
        price=10000.0,
        duration_minutes=60
    ),
]

# Информация о клинике
CLINIC_INFO = {
    "name": "«Дені сау үй жануары» ветклиникасы",
    "address": "Астана қ., Бокейханова 13/1",
    "phone": "+7 (727) 123-45-67",
    "email": "info@vetclinic.kz",
    "working_hours": "Дс-Жм: 9:00-21:00, Сб-Жс: 10:00-18:00",
    "description": "Тәжірибелі мамандар мен заманауи жабдықтары бар қазіргі заманғы ветеринариялық клиника. Біз 15 жылдан астам уақыт бойы сіздің үй жануарларыңыздың денсаулығына қамқорлық жасаймыз.",
    "currency": "₸"
}
