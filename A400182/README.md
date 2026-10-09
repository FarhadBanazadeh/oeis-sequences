# OEIS A400182 — Reduced (6k ± {1,2})/5 Collatz-Type Map

**Author:** Farhad Banazadeh  
**OEIS:** https://oeis.org/A400182  
**Research article:** https://doi.org/10.5281/zenodo.22786203

## Sequence Definition

The sequence counts the number of iterations until the first repeated value, starting from the n-th positive integer not divisible by 5.

The starting values are given by:

`b(n) = floor((5*n - 1)/4)`

For positive integers k not divisible by 5, define the reduced map:

- If k ≡ 1 (mod 5): T(k) = (6k - 1)/5^v_5(6k - 1)
- If k ≡ 2 (mod 5): T(k) = (6k - 2)/5^v_5(6k - 2)
- If k ≡ 3 (mod 5): T(k) = (6k + 2)/5^v_5(6k + 2)
- If k ≡ 4 (mod 5): T(k) = (6k + 1)/5^v_5(6k + 1)

Here v_5(m) is the 5-adic valuation of m.

## Known Cycles

The known cycles are:

- Fixed point: 1
- Fixed point: 2
- Nine-cycle: 22 → 26 → 31 → 37 → 44 → 53 → 64 → 77 → 92 → 22

## Computational Verification

An exhaustive computation verified that all positive starting values k ≤ 10^11 not divisible by 5 enter one of the three observed cycles.

This finite verification does not establish global convergence for all positive integers.

## Sequence Data

The accompanying `b400182.txt` file contains 10,000 indexed sequence terms in standard OEIS b-file format.

## References

- [OEIS A400182](https://oeis.org/A400182)
- [Research publication — Zenodo](https://doi.org/10.5281/zenodo.22786203)

## Author

Farhad Banazadeh  
ORCID: https://orcid.org/0009-0004-7023-0298
