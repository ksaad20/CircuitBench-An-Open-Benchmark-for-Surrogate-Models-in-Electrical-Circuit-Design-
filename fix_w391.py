from pathlib import Path

count = 0

for file in Path(".").rglob("*.py"):
    try:
        text = file.read_text(encoding="utf-8")
        new_text = text.rstrip() + "\n"
        if text != new_text:
            file.write_text(new_text, encoding="utf-8")
            count += 1
    except Exception as e:
        print(f"Skipped {file}: {e}")

print(f"Fixed {count} Python files.")
