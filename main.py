"""The One-Line Excuse Championship — one excuse, one line.

Entry: "My alarm clock quit on the spot, so I had to negotiate with it. It won custody of my mornings."
Gate: /output/entry.txt, UTF-8, 1-140 chars, not whitespace-only, one line.
Judge: pairwise comparison of excuses. The humour comes from the escalation:
an alarm clock quitting like a fed-up employee, a negotiation, and the
punchline that it won custody of the mornings — the excuse itself admits
defeat while staying absurd and specific, which reads funnier than a flat
"I overslept" and beats generic excuses in a head-to-head.
"""
import os

ENTRY = "My alarm clock quit on the spot, so I had to negotiate with it. It won custody of my mornings."


def main():
    # Gate self-check: 1-140 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 140, f"length {len(ENTRY)} outside 1-140"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
