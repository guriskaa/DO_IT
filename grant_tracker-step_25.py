# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GrantTracker
def parse_date(date_str):
    """Парсит дату в формате YYYY-MM-DD или DD.MM.YYYY, возвращает datetime.date."""
    import re
    if not date_str:
        raise ValueError("Дата не указана")
    
    cleaned = date_str.strip()
    
    # Проверяем на некорректные форматы
    if len(cleaned) != 10 or not re.match(r'^\d{4}[-.]?\d{2}[-.]?\d{2}$', cleaned):
        raise ValueError(f"Неверный формат даты: '{cleaned}'. Ожидайте YYYY-MM-DD или DD.MM.YYYY")
    
    # Пытаемся интерпретировать как ISO (YYYY-MM-DD) или европейский (DD.MM.YYYY)
    parts = cleaned.split('-') if '-' in cleaned else cleaned.split('.')
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    
    # Валидация диапазонов
    if not (1 <= year <= 9999):
        raise ValueError(f"Недопустимый год: {year}")
    if not (1 <= month <= 12):
        raise ValueError(f"Месяц должен быть от 1 до 12, получено: {month}")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Учёт високосных годов для февраля
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    
    if not (1 <= day <= days_in_month[month - 1]):
        raise ValueError(f"Неверный день для месяца {month}: {day}. Максимум: {days_in_month[month-1]}")
    
    # В Python datetime.date автоматически обрабатывает високосные годы, но мы уже проверили
    return date(year, month, day)
