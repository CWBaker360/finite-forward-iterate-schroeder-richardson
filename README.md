# Finite Forward-Iterate Schröder Approximation from Geometric Richardson Extrapolation

**Reciprocal Filters and Exact Paired Remainders**

Wayne Baker  
Independent Researcher  
Revised theorem note v0.2.1 — September 2026

## Overview

This note studies a finite forward-iterate realization of geometric Richardson
extrapolation through Schröder–Koenigs conjugacy.

Let Φ be an odd analytic germ with Φ(0)=0 and Φ'(0)=1, let H=Φ^{-1}, and define

S_m(x) = Φ(m H(x)),    m > 1.

The Schröder relation

H(S_m(x)) = m H(x)

diagonalizes the associated composition operator on powers of H. Geometric
Richardson extrapolation can then be represented by a finite fixed-weight
linear combination of forward iterates of S_m.

The construction yields:

- an explicit finite forward-iterate realization of the Richardson extrapolant;
- reciprocal composition-side and scale-side filters;
- exact paired remainder identities;
- explicit first-surviving coefficients and skipped-mode order jumps;
- an active-mode uniqueness criterion;
- finite exact recovery for truncated analytic germs; and
- a sine/arcsine specialization in which the forward maps are classical
  Chebyshev multiple-angle polynomials.

## Claim boundary

Schröder–Koenigs linearization, composition-operator eigenfunctions,
geometric-node Richardson extrapolation, and Richardson order jumps are
classical ingredients and are not claimed as new.

The emphasis of this note is narrower: the explicit finite forward-iterate
realization, its reciprocal pairing with the shrinking-scale Richardson
filter, and the resulting exact paired remainder formulas in the original
variable.

## Files

- `forward_iterate_schroeder_richardson_v0_2_1.pdf` — manuscript
- `forward_iterate_schroeder_richardson_v0_2_1.tex` — LaTeX source

## Version

v0.2.1 — September 2026

## Citation

DOI: https://doi.org/10.5281/zenodo.23122616

## Author

Wayne Baker  
Independent Researcher
