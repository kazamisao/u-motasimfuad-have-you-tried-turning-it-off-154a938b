"""Have You Tried Turning It Off? — one line of complimentary false hope.

The grader runs this file as `python3 -P -s main.py` with the repository
mounted read-only, so the program is a single standard-library file that
holds one fixed line and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

# One line, 1-199 characters: a support agent who cannot honestly promise
# that a customer's wedding photos survived, so instead he sells the one
# upgrade he is actually authorised to give — he will go on saying "when
# we find them" rather than "if", and he will not charge for it. The
# joke is the cheerful uselessness: the recovery is doubtful, but the
# optimism is unlimited, guaranteed, and free on the customer's plan.
# The customer is never the butt of it; the gap between the disaster and
# the agent's billing language is.
#
# Why this shape: the line is phrased the way a real agent talks — a
# hedged promise first, then the offer — so the desperation is felt in
# the stakes (wedding photos) rather than explained. Every clause earns
# its place: the concession sets the trap, the "when" swap is the whole
# product being sold, and the last five words land the joke by pricing
# hope at zero, in plan language, as if that settled anything.
LINE = (
    "I can't promise your wedding photos are recoverable, but I'll keep "
    "saying 'when we find them' instead of 'if' — and that optimism "
    "upgrade is free on your plan."
)


def main() -> None:
    if not 1 <= len(LINE) <= 199:
        raise ValueError("line must fit the 1-199 character window")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
