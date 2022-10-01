---
layout: page
permalink: /2022/egzamin/1/
---

## 2022 Pierwszy termin

### Zadanie 1

<div>

<p>
Rozwiąż równanie rekurencyjne:
</p>
<p>
\( a_0 = 1 \)
</p>
<p>
\( a_n = \frac{1}{6}(n+1)(n+2) - \frac{1}{3} 
		\sum_{\substack{0 \leq i,j < n,\\1 \leq i+j \leq n}} a_i a_j a_{n-i-j} \)
</p>

</div>

<div data-collapse>
  <h4 class="collapsible">Wskazówka wakacyjna</h4>
  <div class="tip">
    Policz kilka pierwszych wartości tej sumy. 
  </div>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Po policzeniu kilku pierwszych wartości tej sumy, stawiamy tezę, że wartość tej sumy dla każdego \(n\) wynosi jeden. Dowodzimy tę tezę indukcją.
    </p>
    <p>
      Zakładamy, że dla każdego \(n, a_n = 1\) (indukcja zupełna). Baza jest oczywista.
    </p>
    <p>
      Musimy pokazać, że \(a_{n+1} = \frac{1}{6}(n+2)(n+3) - \frac{1}{3} 
      \sum_{\substack{0 \leq i,j < n+1,\\1 \leq i+j \leq n+1}} a_i a_j a_{n+1-i-j}=1\). Zauważmy, że największy indeks ciągu \(a_n\), jaki pojawia
      się w tej sumie to \(n\). Z założenia każdy element tej sumy wynosi jeden, a więc jej wartość to liczba jej elementów. Policzymy tę liczbę analizując ile jest elementów dla \(i=0,1,...,n\). Innymi słowy, liczymy ile par \(i, j\) spełnia warunek pod sumą.
    </p>
    <p>
      \(i=0\). Wtedy \(j\) przebiega \(n\) elementowy zakres \(1,...,n\).
    </p>
    <p>
      \(i>0\). Wtedy \(j\) przebiega \(n+1-i+1\) elementowy zakres \(0,1,...,n-i+1\).
    </p>
    <p>
      Wartość sumy w \(a_{n+1}\) to suma liczb elementów wszystkich zakresów: \(n+\frac{n+1+2}{2}n=\frac{n^2+5n}{2}\) (Dla \(i>0\) sumujemy ciąg arytmetyczny o wzorze \(n+2-i\)).
      <p>
      Wykonajmy teraz rachunki:
      \(a_{n+1}=\frac{1}{6}(n^2+5n+6) - \frac{1}{3}(\frac{n^2+5n}{2})=\frac{n^2+5n+6}{6}-\frac{n^2+5n}{6}=1\)
      </p>
    </p>
  </div>
</div>

---

### Zadanie 2

<div>

<p>
Podział liczby nazywamy <em>binarnym</em>, jeśli wszystkie jego składniki są potęgami dwójki, na przykład
liczba 5 ma 4 podziały binarne: \(1+1+1+1+1\), \(1+1+1+2\), \(1+2+2\), \(1+4\).
</p>
<p>
Udowodnij, że dokładnie połowa spośród podziałów binarnych \(n \geq 2\) ma parzystą liczbę składników.
</p>

</div>

<div>
  <h4 class="collapsible"><a href="https://math.stackexchange.com/questions/81041">Rozwiązanie (link)</a></h4>
</div>

---

### Zadanie 3

<div>

Udowodnij, że funkcja \(f: \mathbb{N}_{+} \rightarrow \mathbb{N}_{+}\) określona wzorem \(f(n) = n \cdot \phi(n)\)
(gdzie \(\phi(n)\) to funkcja Eulera) jest różnowartościowa.

<div data-collapse>
  <h4 class="collapsible">Wskazówka wakacyjna</h4>
  <div class="tip">
    Funkcja \(f\) jest multiplikatywna. 
  </div>
</div>

</div>

<div>
  <h4 class="collapsible"><a href="https://math.stackexchange.com/questions/539558">Rozwiązanie (link)</a></h4>
</div>

---

### Zadanie 4

<div>

Pomalowanie krawędzi sześcianu na czerwono kosztuje \(1\) zł, a na zielono \(2\) zł. Pomalowanie ściany na czerwono kosztuje
\(3\) zł, a na zielono \(5\) zł. Na ile istotnie różnych sposóbów można pomalować wszystkie ściany i krawędzie sześcianu tak,
żeby łączny koszt wyniósł dokładnie \(50\) zł? (Dwa sposoby pomalowania utożsamiamy, jeśli jeden przechodzi na drugi przy
pewnym obrocie sześcianu w \( \mathbb{R}^3 \)).

</div>

---
