---
layout: page
permalink: /2024/kolokwium/1/
---

## 2024 Kolokwium 1

### Zadanie 1

<div>

Niech \( K \) będzie kwadratową planszą \( \left(2n - 1 \right) \times \left(2n - 1 \right) \) i niech \( A \) będzie centralnym kwadratem jednostkowym w \( K \). Znajdź sumę pól wszystkich prostokątów zbudowanych z kwadratów jednostkowych i zawierających \( A \).

</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie 1</h4>
  <div class="solution">
    <p>
     <img style="height: 250px; vertical-align: text-top; margin-left: 10px"
     src="/images/2024_k1_solv.svg"
     alt="siatka 7x7 z ponumerowanymi liniami pionowymi i poziomymi oraz z zaznaczonym centralnym punktem">
    </p>
    <p>
        Przykładowa plansza dla \( n = 4\) wraz z zaznaczonym kwadratem centralnym \( A \). Zauważmy, że możemy ponumerować linie poziome i pionowe w planszy, a każdy prostokąt będzie jednoznacznie wyznaczony przez wybrane 4 linie (2 pionowe i 2 poziome). Pamiętając o tym, że wybrane prostokąty muszą zawierać \( A \) dochodzimy do wniosku, że początkowa linia pozioma musi znajdować się ponad \( A \), czyli na przedziale \( [0, n-1] \), zaś końcowa pod \( A \), czyli na przedziale \( [n, 2n-1] \). Analogiczne rozumowanie należy przeprowadzić dla linii pionowych. 
    </p>
    <p>
        Powyższe rozumowanie prowadzi nas do sumy, w której otrzymamy pola wszystkich możliwych prostokątów:
        $$
        \sum_{i = 0}^{n-1} \sum_{j=n}^{2n-1} \sum_{k = 0}^{n-1} \sum_{l = n}^{2n-1} (j-i) \cdot (l-k) = n^6
        $$
    </p>
  </div>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie 2</h4>
  <div class="solution">
    <p>
        Zauważmy, że suma pól prostokątów zawierających wyróżnione pole jest równa sumie pól wszystkich prostokątów minus sumie pól prostokątów, które nie zawierają tego pola. Oznaczmy jako  \( A_{n \times m} \) sumę pól prostokątów złożonych z kwadratów jednostkowych w prostokącie wielkości  \( n \times m \). Aby wyznaczyć tą wartość policzmy w ilu prostokątach zawarte jest wyróżnione pole o współrzędnych  \(i , j \). Zawarte jest ono zawsze, jeżeli lewy górny róg znajduje się w lewo i w górę od tego pola, analogicznie prawy dolny w prawo i w dół. Czyli w  \( ij(n-i+1)(m-j+1)\) prostokątach.
        </p>
        <p> A zatem 
        $$
         A_{n \times m} = \sum_{i=1}^{n}\sum_{i=1}^{m}ij(n-i+1)(m-j+1) = \left(\sum_{i=1}^{n}i(n-i+1)\right) \left(\sum_{j=1}^{m}j(n-j+1)\right) = \binom{n+2}{3} \binom{m+2}{3}
        $$

         Z zasady włączeń - wyłączeń nasz wynik jest równy 
         $$
          A_{2n-1 \times 2n-1} - 4A_{2n-1 \times n-1} + 4A_{n-1 \times n-1}
        $$ Po przekształceniach otrzymujemy \( n^6\).
    </p>
  </div>
</div>

---

### Zadanie 2

<div>

Niech \( B_n \) oznacza planszę \( \{ (i, j) : 1 \leq i \leq n, 2i - 1 \leq j \leq 2i + 1 \}\) i niech \( R_{B_n} (x)\) będzie wieżomianem planszy \( B_n \). Oblicz:
$$
\lim_{n \to \infty} \sqrt[n]{R_{B_n}(1)}
$$

</div>

---

### Zadanie 3

<div>

Niech \( p_{\leq k}^{\leq l} (n)\) oznacza liczbę podziałów liczby \(n\) na co najwyżej \( k\) składników nie większych niż \( l \). Udowodnij, że enumerator takich podziałów, czyli \( P_{k,l}(x) = \sum_{n \geq 0} p_{\leq k}^{\leq l} (n) x^n\) jest określony wzorem:

$$
P_{k, l} (x) = \frac{\prod_{i = 1}^{k+l} (1 - x^i)}{\prod_{s = 1}^{k} (1 - x^s) \prod_{r = 1}^l (1 - x^r )}
$$

Wskazówka: Znajdź zależność rekurencyjną spełnianą przez funkcje \( P_{k,l}(x)\).


</div>

---