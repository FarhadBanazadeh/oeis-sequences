# OEIS A185023 — Ternary (4k ± 1)/3 Collatz-Type Map

**Original sequence author:** Michel Lagneau (2012)

**Computational verification and additional contributions:** Farhad Banazadeh (2026)

**OEIS:** https://oeis.org/A185023

**Research article:** https://doi.org/10.5281/zenodo.22685074
**Research article:** https://doi.org/10.5281/zenodo.22195652

## Sequence Definition

The sequence gives the number of iterations required to reach 1 under the following residue-dependent map:

- If k ≡ 0 (mod 3): T(k) = k/3
- If k ≡ 1 (mod 3): T(k) = (4k - 1)/3
- If k ≡ 2 (mod 3): T(k) = (4k + 1)/3

The initial value is k = n, with a(1) = 0.

## Computational Verification

Farhad Banazadeh reported exhaustive computational verification of convergence to 1 for positive starting values up to 10^11 using 128-bit arithmetic.

This finite verification does not constitute a proof of universal convergence.

## Contributions

The 2026 contributions to OEIS A185023 include:

- Computational verification up to 10^11.
- Additional recurrence formulas.
- A C implementation for generating sequence terms.
- A research publication and reproducibility materials.

## Sequence Data

The official 10,000-term b-file is credited to Michel Lagneau and is available at:

https://oeis.org/A185023/b185023.txt

## References

- [OEIS A185023](https://oeis.org/A185023)
- [Computational verification — Zenodo](https://doi.org/10.5281/zenodo.22685074)
- [Official OEIS b-file](https://oeis.org/A185023/b185023.txt)

## Contributor

Farhad Banazadeh

ORCID: https://orcid.org/0009-0004-7023-0298
