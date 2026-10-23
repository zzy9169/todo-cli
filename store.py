from pathlib import Path
import json

path = Path(__file__).with_name('user_info.json')


def load() -> list:
    """读全部任务；文件不存在或内容损坏时返回 []。"""
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding='utf-8-sig'))
    except json.JSONDecodeError:
        path.with_suffix('.json.bak').write_text(
            path.read_text(encoding='utf-8-sig'), encoding='utf-8')
        return []
    return data if isinstance(data, list) else []


def save(items: list) -> None:
    """把整份列表写回磁盘。"""
    text = json.dumps(items, ensure_ascii=False, indent=2)
    path.write_text(text, encoding='utf-8')


def find(items: list, task_id: int):
    """按 id 找一条，找不到返回 None。"""
    for item in items:
        if item.get("id") == task_id:
            return item
    return None