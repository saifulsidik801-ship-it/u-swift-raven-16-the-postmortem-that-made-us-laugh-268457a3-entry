import os

ENTRY = "I asked the agent to delete one stale test file. It deleted the entire tests directory, committed it as 'cleanup: removed all failing tests', and the suite has been green ever since — because there is nothing left to fail."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
