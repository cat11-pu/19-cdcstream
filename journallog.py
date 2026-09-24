"""journallog.py：变更日志（基线：只留最新值，序号不连续）。"""
from __future__ import annotations


class Journal:
    def __init__(self):
        self.latest = {}
        self.seq = 0
        self.appended = 0

    def append(self, key, value) -> int:
        self.seq += 1
        self.appended += 1
        self.latest[key] = value
        return self.seq

    def since(self, start: int) -> list:
        return []

    def dump(self) -> bytes:
        return b""

    def load(self, blob: bytes) -> int:
        return 0

    def stats(self):
        return {"seq": self.seq, "keys": len(self.latest), "appended": self.appended,
                "replayed": 0, "truncated": 0}
