# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GrantTracker
@dataclass
class GrantTag:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = ""

def add_tag(grant: Grant, tag_name: str) -> Optional[GrantTag]:
    for t in grant.tags:
        if t.name == tag_name:
            return None
    new_tag = GrantTag(name=tag_name)
    grant.tags.append(new_tag)
    return new_tag

def remove_tag(grant: Grant, tag_name: str) -> Optional[GrantTag]:
    for i, t in enumerate(grant.tags):
        if t.name == tag_name:
            removed = grant.tags.pop(i)
            return removed
    return None
