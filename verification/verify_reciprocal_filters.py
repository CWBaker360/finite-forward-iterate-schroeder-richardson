"""Exact-rational checks of finite Schröder/Richardson filter algebra.

Requires SymPy. Checks finite polynomial identities only, not the manuscript's
analytic convergence arguments, novelty, or every claimed theorem.
"""
import sympy as sp


def verify(m: int, max_r: int = 5) -> None:
    z = sp.symbols("z")
    for r in range(max_r + 1):
        p = sp.Integer(1) * sp.prod(
            (sp.Integer(m)**(2*j) - z) / (sp.Integer(m)**(2*j) - 1)
            for j in range(1, r + 1)
        )
        ell = sp.Integer(1) * sp.prod(
            (sp.Integer(m)**(2*j)*z - 1) / (sp.Integer(m)**(2*j) - 1)
            for j in range(1, r + 1)
        )
        assert sp.cancel(ell - z**r * p.subs(z, 1/z)) == 0
        assert sp.simplify(p.subs(z, 1)) == 1
        for j in range(1, r + 1):
            assert sp.simplify(p.subs(z, sp.Integer(m)**(2*j))) == 0
        coeffs = sp.Poly(sp.expand(p), z).all_coeffs()[::-1]
        assert sp.simplify(sum(coeffs)) == 1
        for j in range(1, r + 1):
            assert sp.simplify(sum(
                coeffs[q] * sp.Integer(m)**(2*j*q)
                for q in range(r + 1)
            )) == 0
        expected = (-1)**r * sp.Integer(m)**(r*(r+1))
        assert sp.simplify(
            p.subs(z, sp.Integer(m)**(2*(r+1))) - expected
        ) == 0
        print(f"m={m}, r={r}: PASS")


if __name__ == "__main__":
    for multiplier in (3, 5):
        verify(multiplier)
    print("All exact filter checks passed.")
