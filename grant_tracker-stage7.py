# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GrantTracker
def sort_grants(grants, key='deadline'):
    reverse = False
    if key == 'priority':
        def _sort_priority(item): return -item['priority']
    elif key == 'name':
        def _sort_name(item): return item['name'].lower()
    else:
        def _sort_deadline(item): return item.get('deadline', float('inf')) if isinstance(item['deadline'], str) else item['deadline']
    
    sorted_grants = sorted(grants, key=_sort_deadline if key == 'deadline' else (_sort_priority if key == 'priority' else _sort_name), reverse=reverse)
    return sorted_grants
