# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GrantTracker
def print_table(headers, rows):
    col_widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0)) + 2 for i, h in enumerate(headers)]
    fmt = ' | '.join(f'{{:<{w}}}' for w in col_widths)
    print(fmt.format(*headers))
    print('-+-'.join('-' * w for w in col_widths))
    for row in rows:
        print(fmt.format(*row))
