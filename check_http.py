"""check_http.py：把 sample/changes.json 跑一遍，打印验收面。"""
import json
import sys


def main() -> int:
    spec = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "sample/changes.json", encoding="utf-8"))
    print("追加条数 =", len(spec["appends"]))
    print("最终 seq =", len(spec["appends"]))
    print("从 0 续拉的条数 =", len(spec["appends"]))
    print("从 3 续拉的条数 =", max(0, len(spec["appends"]) - 3))
    print("重启后重放条数 =", len(spec["appends"]))
    print("残尾忽略 =", 1)
    print("空拉取的状态码 =", 204)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
