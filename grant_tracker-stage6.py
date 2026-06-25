# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GrantTracker
def filter_grants(status=None, category=None, tags=None):
    filtered = []
    for grant in grants:
        if status and grant['status'] != status: continue
        if category and grant.get('category') != category: continue
        if tags:
            grant_tags = set(grant.get('tags', [])).intersection(set(tags))
            if not grant_tags: continue
        filtered.append(grant)
    return filtered

def search_grants(query):
    results = []
    query_lower = query.lower()
    for grant in grants:
        text = f"{grant['title']} {grant.get('description', '')} {' '.join(grant.get('tags', []))}".lower()
        if query_lower in text: results.append(grant)
    return results
