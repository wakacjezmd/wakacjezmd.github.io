---
layout: page
permalink: /2015/kolokwium/1/
---

## 2015 Pierwsze kolokwium

###Zadanie 1
Znajdź liczbę przedstawień liczby naturalnej \\(n\\) w postaci pewnej liczby
nieujemnych składników całkowitych, przy czym istotna jest kolejność składników,
a z każdych dwóch kolejnych składników co najmniej jeden jest dodatni.

Przykład: Dla \\(n = 2\\) jest \\(12\\) takich przedstawień:  

- \\(0+1+0+1,\\)
- \\(0+1+0+1+0\\),
- \\(0+1+1+0+1+1+0\\),
- \\(0+2\\),
- \\(0+2+0\\),
- \\(1+0+1\\),
- \\(1+0+1+0\\),
- \\(1+1\\),
- \\(1+1+0\\),
- \\(2\\),
- \\(2+0\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
        $$4\sum\limits^{n-1}_{i=0}(i+1)^{n-i}$$
    </p>
    <p>
        Tworzymy \(i + 1\) komórek i wypełniamy je jedynkami. Pomiędzy każdymi
        dwiema komórkami wstawiamy \(0\) (warto zauważyć, że \(i\) jest liczbą
        zer). Teraz pozostało nam \(n - i\) jedynek, które możemy dowolnie
        włożyć do \(i + 1\) komórek. Otrzymaną sumę po \(i\) mnożymy przez
        \\(4\\),ponieważ możemy dołożyć dodatkowe zero z lewej, z prawej, z obu
        stron lub w ogóle.
    </p>
  </div>
</div>

---

###Zadanie 2

---

###Zadanie 3

---
