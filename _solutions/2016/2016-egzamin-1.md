---
layout: page
permalink: /2016/egzamin/1/
---

## 2016 Pierwszy termin

### Zadanie 1

Udowodnij tożsamość \\(\sum^n\_{k=1}(-1)^k(k-1)!{n \brace k} = 0\\) dla
\\(n > 1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    $$
    \begin{align*}
      \sum^n_{k=1}(-1)^k(k-1)!{n \brace k}
      &=\sum^n_{k=1}(-1)^k(k-1)^{\underline{k-1}}\left(k{n-1 \brace k} +
       {n-1 \brace k-1}\right) = \\
      &=\sum^n_{k=1}(-1)^k k^{\underline{k}}{n-1 \brace k} +
       \sum^n_{k=1}(-1)^k (k-1)^{\underline{k-1}}{n-1 \brace k-1}
    \end{align*}
    $$
  </p>
  <p>
    Teraz rozpiszmy obie sumy:
    $$
    \begin{align*}
      &=&&- 1^{\underline{1}}{n-1 \brace 1}
       + 2^{\underline{2}}{n-1 \brace 2}
       - 3^{\underline{3}}{n-1 \brace 3}
       + \dots
       \pm (-1)^{n-1}(n-1)^{\underline{n-1}}{n-1 \brace n-1} + \\
      &&&- 0^{\underline{0}}{n-1 \brace 0}
       + 1^{\underline{1}}{n-1 \brace 1}
       - 2^{\underline{2}}{n-1 \brace 2}
       - \dots
       \pm (-1)^{n}(n-1)^{\underline{n-1}}{n-1 \brace n-1} = \\
      & = 0
    \end{align*}
    $$
  </p>
  </div>
</div>

---

### Zadanie 2

---

### Zadanie 3

Uprość sumę \\(\sum^n\_{k-1}\left\lfloor \frac{n}{k} \right\rfloor \phi(k)\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <a href="http://math.stackexchange.com/questions/1155433/euler-phi-function-and-floor-function">
        http://math.stackexchange.com/questions/1155433/euler-phi-function-and-floor-function
      </a>
    </p>
  </div>
</div>

---

### Zadanie 4

---
