---
layout: page
permalink: /2017/egzamin/1/
---

## 2017 Pierwszy termin

### Zadanie 1
<p style="margin-bottom: 15px">
  Znajdź \(|\{b \in \{0,1\}^* : \#_{0}(b) + 2\#_{1}(b) \leq n\}|\), gdzie \(\#_{x}(b)\) oznacza liczbę wystąpień symbolu \(x\) w ciągu \(b\).
</p>
---

### Zadanie 2
<p style="margin-bottom: 15px">

  <i>Iloczyn Hadamarda</i> szeregów potęgowych \(A(x) = \sum_{n \geq 0} a_n x^n\) i 
  \(B(x) = \sum_{n \geq 0} b_n x^n\) to szereg \(A(x) \bigodot B(x) = \sum_{n \geq 0} a_{n} b_{n} x^n\). Udowodnij, że jeśli \(A\) i \(B\) są 
  funkcjami wymiernymi (czyli ilorazami wielomianów), to \(A \bigodot B\) też jest funkcją wymierną. 
  <i> Wskazówka:</i> jakie ciągi \( \langle a_{n} \rangle\) mają wymierną funkcję tworzącą \(A(x)\)?
</p>
---

### Zadanie 3
<p style="margin-bottom: 15px">
  Udowodnij, że jeśli \(m,n > 1\) i \(m \mid 2^n - 1\), to \(l(m) > l(n)\), gdzie \(l(x)\) oznacza <i> najmniejszy dzielnik pierwszy  </i> 
  liczby \(x\). <i> Wskazówka: </i> Rozważ rząd elementu \(2\) w \(\mathbb{Z}_{l(m)}^*\).
</p> 


<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
		Najpierw zauważmy, że \(m\) jest nieparzyste, więc \(l(m)\) też musi być.
		Stąd wiemy, że \(2 \in \mathbb{Z}_{l(m)}^* \).
		Oznaczmy rząd \(2\) w tej grupie jako \(o\).
		Z małego tw. Fermata mamy dzięki temu, że \(o|l(m)-1\).
		Zatem \(o < l(m)\).
		Skoro \(m | 2^n-1\), to także \(l(m) | 2^n-1\), czyli \(2^n \equiv 1 \bmod l(n) \).
		To oznacza z kolei, że \(o|n\) z definicji rzędu elementu.
		Wiemy teraz, że o jest dzielnikiem n i \(o < l(m)\), zatem najmniejszy dzielnik \(n\) też musi spełniać tę nierówność.
    </p>
  </div>
</div>

---

### Zadanie 4
<p style="margin-bottom: 15px">
  Macierz \(2 \times 3\) wypełniamy liczbami ze zbioru \(\{1,2,3\}\), przy czym każda z liczb musi 
  wystąpić przynajmniej raz. Oblicz, na ile istotnie różnych sposobów można to zrobić, jeśli dwie macierze utożsamiamy, gdy jedną można otrzymać z drugiej strony przez pewną permutację wierszy i/lub kolumn.
</p> 

<div>
  <h4 class="collapsible"><a href="https://math.stackexchange.com/questions/2113657/burnsides-lemma-applied-to-grids-with-interchanging-rows-and-columns">Rozwiązanie (link)</a></h4>
</div>

---
