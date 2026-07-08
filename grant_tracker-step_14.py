# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GrantTracker
def generate_summary(grants):
    """Генерирует краткую сводку по текущим данным."""
    if not grants:
        return "Нет данных для отображения."

    total_budget = sum(g['budget'] for g in grants)
    deadline_grants = [g for g in grants if g.get('deadline') and g['deadline'] < datetime.now().date()]
    pending_grants = [g for g in grants if g['status'] == 'pending']

    status_counts = {}
    for g in grants:
        s = g['status']
        status_counts[s] = status_counts.get(s, 0) + 1

    summary_lines = [f"Сводка GrantTracker:"]
    summary_lines.append(f"- Всего заявок: {len(grants)}")
    summary_lines.append(f"- Статусы: {', '.join(f'{s}: {c}' for s, c in status_counts.items())}")
    summary_lines.append(f"- Общий бюджет: {total_budget} руб.")
    if deadline_grants:
        deadline_str = ', '.join(g['deadline'].strftime('%d.%m.%Y') for g in deadline_grants)
        summary_lines.append(f"- Дедлайны приближаются ({len(deadline_grants)}): {deadline_str}")
    else:
        summary_lines.append("- Все дедлайны в норме.")

    return '\n'.join(summary_lines)
