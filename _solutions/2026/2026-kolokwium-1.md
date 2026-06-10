---
layout: page
permalink: /2026/kolokwium/1/
---

## 2026 Kolokwium 1

### Zadanie 1

Niech \\(a\_n\\) oznacza liczbę \\(n\\)-permutacji \\(a\_1 a\_2 \dots a\_n\\), które mają
dwa *lewostronne maksima lokalne*, tzn.
$$
\left| \left\{ i \in \{1, 2, \dots, n-1\} \colon a_i < a_{i+1} \right\} \right| = 2 .
$$
Udowodnij, że \\( a\_n = 3^n - (n+1) 2^n + \binom{n+1}{2} \\).

---

### Zadanie 2

Dla \\(n \ge 0\\) niech \\(d\_n\\) oznacza liczbę \\(n\\)-słów nad alfabetem \\(\\{A, B, C\\}\\),
w których litery \\(A\\) i \\(B\\) nie sąsiadują ze sobą. Znajdź zwarty wzór na \\(d\_n\\).

---

### Zadanie 3

*Dwukolorowym podziałem* liczby \\(n\\) nazwiemy taki podział \\(n\\), którego każdy
składnik jest czerwony albo niebieski, przy czym wszystkie składniki tego samego
rozmiaru mają ten sam kolor (np. \\(n = 3\\) ma \\(8\\) dwukolorowych podziałów:
\\((1+1+1)N\\), \\((1+1+1)C\\), \\((2)C+(1)C\\), \\((2)C+(1)N\\), \\((2)N+1(C)\\),
\\((2)N+(1)N\\), \\((3)C\\), \\((3)N\\)).

Udowodnij, że liczba dwukolorowych podziałów \\(n\\) to
$$
\sum_{k=0}^{n} P_k Q_{n-k},
$$
gdzie \\(P\_n\\) to liczba wszystkich podziałów \\(n\\), zaś \\(Q\_n\\) to liczba podziałów
\\(n\\) na składniki nieparzyste.

---
