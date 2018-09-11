---
layout: page
permalink: /2018/egzamin/1/
---

## 2018 Pierwszy termin

### Zadanie 1

Niech \\( f\_n(k) \\) oznacza liczbę \\( n \\)-permutacji o dokładnie \\( k \\) punktach stałych. Uprość sumę \\( \sum\_{k=0}^{n} k f\_n(k) \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>Skoro \( f_n(k) \) to liczba \( n \)-permutacji o \( k \) punktach stałych, to \( \sum_{k=0}^n k f_n(k) \) jest liczbą punktów stałych łącznie we wszystkich \( n \)-permutacjach.</p>
    <p>Rozważmy wszystkie \( n \)-permutacje, w których \( x \) jest punktem stałym. Punkt stały \( x \) w każdej z nich zwiększa zadaną sumę o \( 1 \). Takich permutacji jest \( (n-1)! \). Zatem z punktów stałych w \( x \) suma zwiększa się o \( (n-1)! \).</p>
    <p>\( x \) możemy wybrać na \( n \) sposobów, więc suma jest równa \( n (n-1)! = n! \).</p>
  </div>
</div>

---

### Zadanie 2

Niech \\( A(x) \\) będzie enumeratorem takich podziałów liczby, które zawierają dokładnie jeden (chociaż być może występujący wielokrotnie) ze składników \\( 2 \\), \\( 3 \\), \\( 5 \\), zaś \\( P(x) \\) – enumeratorem wszystkich podziałów. Znajdź zwarty wzór na \\( B(x) \\) takie, że \\( A(x) = P(x) \cdot B(x) \\).

---

### Zadanie 3

Oblicz, ile jest liczb całkowitych \\( 1 \leq n \leq 1000 \\) takich, że liczba \\( 9^n - n \\) jest podzielna przez \\( 65 \\).

---

### Zadanie 4

Każdą krawędź grafu \\( W\_6 \\) („koło o 6 szprychach”, czyli cykl \\( C\_6 \\) wraz z dodatkowym wierzchołkiem połączonym krawędziami ze wszystkimi wierzchołkami cyklu) orientujemy, a każdy wierzchołek malujemy na jeden z \\( k \\) kolorów. Oblicz, na ile istotnie różnych sposobów można to zrobić, jeśli dwa zorientowane i pomalowane grafy utożsamiamy, gdy jeden przechodzi na drugi przy pewnym izomorfizmie zachowującym orientację krawędzi i kolory wierzchołków.

---
