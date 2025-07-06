---
layout: page
permalink: /2025/kolokwium/1/
---

## 2025 Kolokwium 1

### Zadanie 1

<div>
    Dla ustalonego \( n \in \mathbb{N} \) niech \( P_{i,j} \) oznacza zbiór tych permutacji zbioru \( \{1, \ldots, n\} \), w których element \( i \) należy do cyklu długości \( j \). Uprość sumę:
    $$
        \sum_{1 \leq i,j \leq n} \mid P_{i,j} \cup P_{j,i} \mid
    $$
</div>

---

### Zadanie 2

<div>
    Dla \( n \geq 2 \) niech \( a_n \) oznacza liczbę \( n \)-ciągów 0-1 zaczynających się od 1 i kończących na 0, takich że liczba jedynek na lewo od każdego zera jest nieparzysta. Znajdź zwarty wzór na \( a_n \).
</div>

---

### Zadanie 3

<div>
    Niech \( S_k (n) \) oznacza liczbę podziałów \( n \), w których największy składnik występuje co najmniej \( k \)-krotnie (w szczególności, \( S_1 (n) \) to \( P_n \), czyli liczba wszystkich podziałów \( n \)). Przyjmujemy dodatkowo, że \( S_k (0) = 1 \) oraz \( S_k (n) = 0 \) dla  \( n \lt 0 \). Udowodnij, że dla każdego \( k \geq 1 \) istnieją liczby całkowite \( \alpha_{0}^{(k)}, \alpha_{1}^{(k)}, \dots, \alpha_{ \binom{k}{2} }^{(k)} \), takie że:

<!-- tu powinno być "dla każdego n e N" ale ż źle wygląda w latexu wiec usunąłem "każdego", jak wiesz jak to naprawić to możesz spowrotem dodać -->

    $$
        S_k (n) = \sum_{ i = 0 }^{ \binom{k}{2} } \alpha_{i}^{(k)} P_{ n - i }   \qquad    \text{dla } n \in \mathbb{N}
    $$ 

    Wskazówka: Spróbuj znaleźć zależność rekurencyjną spełnianą przez \( S_k(n) \).
</div>

---