---
layout: page
permalink: /2014/egzamin/2/
---

## 2014 Egzamin poprawkowy

###Zadanie 2

Udowodnij, że podziałów liczby \\(n\\) na cztery części jest tyle samo co podziałów
liczby \\(3n\\) na cztery części rozmiaru co najwyżej \\(n - 1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Żeby udowodnijć to stwierdzenie wskażemy bijekcję między zbiorami podziałów.<br/>
      Weźmy dowolny podział \(n\) na liczby \( \left\{ a_1, a_2, a_3, a_4 \right\}\). Zachodzi:
      $$\sum_{i=1}^4 a_i = n $$
      Teraz rozważmy podział \(\left\{n - a_1, n - a_2, n - a_3, n - a_4\right\}\).
      $$(n - a_1) + (n - a_2) + (n - a_3) + (n - a_4) = 4n - \sum_{i=1}^4 a_i = 3n$$
      Dodatkowo \(\forall_{i}\ 1 \leq a_i \leq n - 1\), więc \(\forall_{i}\ 1 \leq n - a_i \leq n - 1\).
    </p>
  </div>
</div>
