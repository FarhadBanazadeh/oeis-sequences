# OEIS A185023 — Ternary (4k ± 1)/3 Collatz-Type Map

**Original OEIS sequence author:** Michel Lagneau (2012)

**Independent investigation and computational extension:** Farhad Banazadeh (2026)

**OEIS:** https://oeis.org/A185023

**Research publication:** https://doi.org/10.5281/zenodo.22685074

**Research publication:** https://doi.org/10.5281/zenodo.22195652

**Historical submission:** https://oeis.org/history?seq=A397114

## 1. Sequence Definition

OEIS A185023 gives the number of iterations required to reach 1 under the residue-dependent ternary Collatz-type map.

For positive integers k, define:

- If k ≡ 0 (mod 3): T(k) = k/3
- If k ≡ 1 (mod 3): T(k) = (4k - 1)/3
- If k ≡ 2 (mod 3): T(k) = (4k + 1)/3

The initial value is k = n.

The sequence is defined by the number of iterations required to reach 1, with a(1) = 0.

For a starting value that does not reach 1, the conventional value is -1.

## 2. Independent Research and Historical Background

This map was independently investigated by Farhad Banazadeh in 2026 without prior knowledge of the existing OEIS entry A185023, originally submitted by Michel Lagneau in 2012.

Banazadeh independently studied the dynamics of the ternary (4k ± 1)/3 map, conducted extensive computational verification, and prepared a research publication presenting the computational results.

A related sequence was submitted to OEIS under A397114 in September 2026. The revision history documents the submission, including its mathematical definition, sequence data, computational results, and source code.

Following recognition of the earlier A185023 entry, the separate submission was recycled, and Banazadeh's relevant contributions were incorporated into A185023.

This history documents an independent investigation and subsequent computational extension of an already existing OEIS sequence. It does not imply priority over the original 2012 entry.

## 3. Computational Verification up to 10^11

Farhad Banazadeh reported an exhaustive computational verification of the ternary (4k ± 1)/3 Collatz-type map for positive starting values up to 10^11.

The research employed 128-bit arithmetic to support the large-scale computation.

The verification reported convergence to 1 throughout the tested finite range.

This computational evidence does not constitute a mathematical proof that every positive integer eventually reaches 1.

Universal convergence remains a conjecture.

## 4. Contributions to OEIS A185023

Banazadeh's documented contributions include:

- Independent mathematical investigation of the ternary (4k ± 1)/3 map.
- Exhaustive computational verification up to 10^11.
- Additional recurrence formulas for the sequence.
- A C implementation for computing sequence terms.
- Publication of the computational research on Zenodo.
- Contribution of computational findings and references to the existing OEIS record.

These contributions are recorded in the relevant sections of OEIS A185023.

## 5. Example Trajectory

Starting with n = 8:

8 → 11 → 15 → 5 → 7 → 9 → 3 → 1

The trajectory reaches 1 after seven iterations.

Therefore:

a(8) = 7.

## 6. Sequence Data and Reproducibility

The official OEIS b-file contains 10,000 indexed sequence terms and is credited to Michel Lagneau.

Official b-file:

https://oeis.org/A185023/b185023.txt

The Python implementation in this repository provides an additional method for generating and checking sequence terms.

The research publication documents the extended computational verification.

## 7. OEIS Submission History

The OEIS revision history for A397114 preserves the earlier submission and subsequent editorial changes.

- August 19, 2026: Earlier activity and edits under A397114.
- September 11, 2026: Submission of the ternary (4k ± 1)/3 sequence definition, data, formulas, examples, and C implementation.
- September 15, 2026: Recycling of the A397114 submission.
- September 2026: Banazadeh's computational contributions and related publication were recorded in A185023.

Historical revision record:

https://oeis.org/history?seq=A397114

Current OEIS entry:

https://oeis.org/A185023

## 8. References

1. Michel Lagneau, OEIS A185023, original sequence submission, 2012.

   https://oeis.org/A185023

2. A Ternary (4k±1)/3 Collatz-Type Map: Computational Verification up to 10^9 , Zenodo, 2026.

   https://zenodo.org/doi/10.5281/zenodo.22195652

3. A Ternary (4k±1)/3 Collatz-Type Map: Exact 3-Adic Symbolic Dynamics, Density-One First Descent, Algebraic Cycle Analysis, and Exhaustive Verification up to 10^11 , Zenodo, 2026.

   https://zenodo.org/doi/10.5281/zenodo.22964212

4. Extended Computational Verification of the Ternary (4k +/- 1)/3 Collatz-Type Map up to 10^11: A 128-Bit Exhaustive Certification*, Zenodo, 2026.

   https://doi.org/10.5281/zenodo.22685074

5. OEIS A397114, historical revision record, 2026.

   https://oeis.org/history?seq=A397114

6. OEIS A185023, official sequence data.

   https://oeis.org/A185023/b185023.txt

## 9. Researcher Information

**Farhad Banazadeh**

Independent Mathematics Researcher

ORCID: https://orcid.org/0009-0004-7023-0298

GitHub: https://github.com/FarhadBanazadeh

OEIS contributor profile: https://oeis.org/wiki/User:Farhad_Banazadeh

---

**Research integrity statement:** The independent investigation, historical OEIS submission, and computational contributions are documented separately from the original authorship of A185023. The finite computational verification does not establish universal convergence.
