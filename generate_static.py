#!/usr/bin/env python3
"""
Скрипт для генерации статических HTML файлов для GitHub Pages.
Этот скрипт рендерит все шаблоны и сохраняет их как статические HTML файлы.
"""

import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Импортируем данные из моделей
import sys
sys.path.insert(0, str(Path(__file__).parent))

from app.models import DOCTORS, SERVICES, CLINIC_INFO


def generate_static_site():
    """Генерирует статический сайт из Jinja2 шаблонов."""
    
    # Пути
    base_dir = Path(__file__).parent
    templates_dir = base_dir / "app" / "templates"
    static_dir = base_dir / "static"
    output_dir = base_dir / "docs"
    
    # Создаем output директорию
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    
    # Настраиваем Jinja2
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    
    # Общий контекст для всех шаблонов
    base_context = {
        "clinic": CLINIC_INFO,
        "doctors": DOCTORS,
        "services": SERVICES,
    }
    
    # Страницы для генерации
    pages = [
        {
            "template": "index.html",
            "output": "index.html",
            "context": {
                **base_context,
                "doctors": DOCTORS[:3],  # Только 3 врача на главной
                "services": SERVICES[:4],  # Только 4 услуги на главной
            }
        },
        {
            "template": "services.html",
            "output": "services.html",
            "context": base_context
        },
        {
            "template": "doctors.html",
            "output": "doctors.html",
            "context": base_context
        },
        {
            "template": "contact.html",
            "output": "contact.html",
            "context": base_context
        },
        {
            "template": "appointment.html",
            "output": "appointment.html",
            "context": base_context
        },
    ]
    
    # Генерируем HTML файлы
    for page in pages:
        print(f"Генерация {page['output']}...")
        template = env.get_template(page["template"])
        html = template.render(**page["context"])
        
        output_path = output_dir / page["output"]
        output_path.write_text(html, encoding="utf-8")
    
    # Копируем статические файлы
    print("Копирование статических файлов...")
    static_output = output_dir / "static"
    if static_dir.exists():
        shutil.copytree(static_dir, static_output)
    
    # Создаем .nojekyll файл для GitHub Pages
    (output_dir / ".nojekyll").touch()
    
    # Создаем CNAME файл (если нужен кастомный домен)
    # (output_dir / "CNAME").write_text("your-domain.com")
    
    print(f"\n✅ Статический сайт успешно сгенерирован в папке '{output_dir}'")
    print(f"   Всего страниц: {len(pages)}")
    print("\nДля просмотра локально можно использовать:")
    print(f"   cd {output_dir} && python -m http.server 8080")


def main():
    """Главная функция."""
    print("=" * 50)
    print("🏥 Генератор статического сайта ВетКлиники")
    print("=" * 50)
    print()
    
    try:
        generate_static_site()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        raise


if __name__ == "__main__":
    main()
