"""OEIS A185023: steps to reach 1 for a ternary Collatz-type map.

Original sequence: Michel Lagneau. Contributions by Farhad Banazadeh.
This computes a finite number of terms, not a proof of convergence.
"""


def T(k: int) -> int:
    """One step of the residue-dependent map on positive integers."""
    if k < 1:
        raise ValueError("k must be a positive integer")
    r = k % 3
    if r == 0:
        return k // 3
    if r == 1:
        return (4 * k - 1) // 3
    return (4 * k + 1) // 3


def a(n: int, max_steps: int = 1_000_000) -> int:
    """Return the number of steps to 1, or raise if not reached in max_steps.

    No negative return value is inferred if the safety cap is reached.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    k = n
    for steps in range(max_steps + 1):
        if k == 1:
            return steps
        if steps == max_steps:
            break
        k = T(k)
    raise RuntimeError(f"Starting value {n} did not reach 1 within {max_steps} steps")


def write_bfile(count: int = 10000, filename: str = "b185023_generated.txt") -> None:
    """Generate local indexed data; the official OEIS b-file is credited to Michel Lagneau."""
    with open(filename, "w", encoding="utf-8") as out:
        for n in range(1, count + 1):
            out.write(f"{n} {a(n)}\n")


if __name__ == "__main__":
    print(", ".join(str(a(n)) for n in range(1, 81)))
    # Uncomment to generate local data:
    # write_bfile()
