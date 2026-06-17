# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GrantTracker
import json, os, uuid, datetime as dt
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any

@dataclass
class Grant:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = ""
    deadline: dt.date = None
    budget: float = 0.0
    status: str = "draft"
    documents: List[str] = field(default_factory=list)

class GrantTracker:
    def __init__(self, db_file="grants.json"):
        self.db_file = db_file
        self.grants: Dict[str, Grant] = {}
        self._load()

    def _load(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file) as f:
                    data = json.load(f)
                    for gid, d in data.items():
                        g = Grant(**d)
                        self.grants[g.id] = g
            except Exception:
                pass

    def _save(self):
        try:
            with open(self.db_file, "w") as f:
                json.dump({gid: asdict(g) for gid, g in self.grants.items()}, f, indent=2)
        except Exception:
            pass

    def add_grant(self, name: str, deadline: dt.date, budget: float = 0.0):
        grant = Grant(name=name, deadline=deadline, budget=budget)
        self.grants[grant.id] = grant
        self._save()
        return grant

    def get_all(self) -> List[Dict[str, Any]]:
        return [asdict(g) for g in sorted(self.grants.values(), key=lambda x: x.deadline or dt.max_date)]

# Демонстрационные данные и точка входа
if __name__ == "__main__":
    tracker = GrantTracker()
    d1, d2, d3 = dt.date(2025, 6, 1), dt.date(2025, 7, 15), dt.date(2025, 8, 1)
    t.add_grant("AI Research", d1, 50000.0).documents.append("proposal.pdf")
    t.add_grant("Green Energy", d2, 120000.0)
    t.add_grant("Education Fund", d3, 75000.0)
    print(json.dumps(t.get_all(), indent=2))
