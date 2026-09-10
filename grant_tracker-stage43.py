# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GrantTracker
def paginate_records(records, page_size=10, current_page=1):
    """Compact pagination helper: returns (items, total_pages, current_page)."""
    if page_size < 1:
        page_size = 1
    total_pages = max(1, (len(records) + page_size - 1) // page_size)
    current_page = max(1, min(current_page, total_pages))
    start = (current_page - 1) * page_size
    end = start + page_size
    return records[start:end], total_pages, current_page
