---
layout: page
permalink: /2013/egzamin/1/
---

## 2013 Pierwszy termin

### Zadanie 3

Rozwiąż kongruencję \\(x^{59} \equiv 604 \ (mod\ 2013)\\)

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Wiemy, że \( 2013 = 3 \cdot 11 \cdot 61\), \(\phi(p) = p-1 \) (dla \(p\)
      będącej liczbą pierwszą), a kongruencja w treści jest równoważna
      poniższemu układowi:
      $$
      \left\{
        \begin{array}{lr}
          x^{59} \equiv 604\ (mod\ 3) \equiv 1\ (mod\ 3)\\
          x^{59} \equiv 604\ (mod\ 11) \equiv 10\ (mod\ 11)\\
          x^{59} \equiv 604\ (mod\ 61) \equiv 55\ (mod\ 61)
        \end{array}
      \right.
      $$
    </p>
    <p>
      \((1)\)
    </p>
    <p>
      $$
      x^{2} \equiv 1\ (mod\ 3) \Rightarrow x^{58} \equiv 1\ (mod\ 3)
      $$
      $$
      x^{59} \equiv 1\ (mod\ 3)
      $$
      $$
      x \equiv 1\ (mod\ 3)
      $$
    </p>
    <p>
      \((2)\)
    </p>
    <p>
      $$
      x^{10} \equiv 1\ (mod\ 11) \Rightarrow x^{60} \equiv 1\ (mod\ 11)
      $$
      $$
      x^{59} \equiv 10\ (mod\ 11)
      $$
      $$
      x \equiv 10^{-1}\ (mod\ 11) \equiv 10\ (mod\ 11)
      $$
    </p>
    <p>
      \((3)\)
    </p>
    <p>
      $$
      x^{60} \equiv 1\ (mod\ 61)
      $$
      $$
      x^{59} \equiv 55\ (mod\ 61)
      $$
      $$
      x \equiv 55^{-1}\ (mod\ 61) \equiv 10\ (mod\ 61)
      $$
    </p>
    <p>
      Otrzymujemy układ kongruencji:
      $$
      \left\{
        \begin{array}{lr}
          x \equiv 1\ (mod\ 3)\\
          x \equiv 10\ (mod\ 11)\\
          x \equiv 10\ (mod\ 61)
        \end{array}
      \right.
      $$
    </p>
    <p>
      Teraz z konstruktywnej wersji chińskiego twierdzenia o resztach, możemy
      wyliczyć, że
      $$
      x \equiv 1 \cdot 671 \cdot 2 + 10 \cdot 183 \cdot 8 +
      10 \cdot 33 \cdot 37\ (mod\ 2013)
      $$
      $$
      x \equiv 10\ (mod\ 2013)
      $$
    </p>
  </div>
</div>

---
