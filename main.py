import os

ENTRY = "Inventory audit complete: the yogurt expired Tuesday. I watched you read the date, put it back, and lie to yourself. Verdict: in this fridge, you're the leftovers now."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
