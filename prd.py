TEMPLATE = """# PRD: {title}

**Автор:** {author}
**Дата:** {date}
**Версия:** {version}

## 1. Проблема
{problem}

## 2. Целевая аудитория
{audience}

## 3. Цели и метрики успеха
{goals}

## 4. Функциональные требования
{features}

## 5. Нефункциональные требования
{nonfunctional}

## 6. User Stories
{stories}

## 7. Out of scope
{out_of_scope}

## 8. Риски
{risks}

## 9. Таймлайн
{timeline}
"""

def generate(**kwargs):
    defaults = {
        "title": "Название фичи",
        "author": "Product Owner",
        "date": "2025-01-01",
        "version": "1.0",
        "problem": "- Опишите проблему",
        "audience": "- Кто пользователи",
        "goals": "- Метрика: цель",
        "features": "- [ ] Фича 1",
        "nonfunctional": "- Производительность, безопасность",
        "stories": "- As a …, I want …, so that …",
        "out_of_scope": "- Что НЕ делаем",
        "risks": "- Риск 1",
        "timeline": "- Q1: дизайн\n- Q2: разработка",
    }
    defaults.update(kwargs)
    return TEMPLATE.format(**defaults)
