"""Generate terms of OEIS A400182 and its standard b-file.

For starting value b(n) = floor((5*n-1)/4), count iterations of the
reduced residue-dependent 6k +/- {1,2} map until the first repetition.

Note: a trajectory without a repeated value would not terminate here.
"""


def T(k: int) -> int:
    if k <= 0 or k % 5 == 0:
        raise ValueError("k must be a positive integer not divisible by 5")
    y = 6 * k + {1: -1, 2: -2, 3: 2, 4: 1}[k % 5]
    while y % 5 == 0:
        y //= 5
    return y


def a(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    k = (5 * n - 1) // 4
    seen = set()
    while k not in seen:
        seen.add(k)
        k = T(k)
    return len(seen)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate OEIS A400182 b-file")
    parser.add_argument("--terms", type=int, default=10000)
    parser.add_argument("--output", default="b400182.txt")
    args = parser.parse_args()
    if args.terms < 1:
        parser.error("--terms must be positive")
    with open(args.output, "w", encoding="utf-8") as f:
        for n in range(1, args.terms + 1):
            f.write(f"{n} {a(n)}\n")
    print(f"Wrote {args.terms} terms to {args.output}")
