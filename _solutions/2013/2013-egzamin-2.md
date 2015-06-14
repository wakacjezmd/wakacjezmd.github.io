---
layout: page
permalink: /2013/egzamin/2/
---

## 2013 Egzamin poprawkowy

###Zadanie 1

Udowodnij, że liczba \\(\frac{(kn)!}{k!(n!)^{k}}\\) jest całkowita dla dowolnych naturalnych n i k.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Oznaczmy \( p(n, k) \) jako liczbę podziałów zbioru n elementowego na bloki
      zawierające dokładnie k elementów. W szczególności \( \forall_{n,k}\ p(n, k) \in \mathbb{Z} \).
    </p>
    <p>
      Pokażemy przez IK, że \((kn)! = p(kn, k)k!(n!)^k\).
    </p>
    <p>
      <b>LEWA:</b> \((kn)!\) to liczba permutacji pól prostokąta o wymiarach \( k \times n \).
    </p>
    <p>
      <b>PRAWA:</b> Dowolną permutacje pól takiego prostokąta możemy również uzyskać najpierw
      wybierając z \(kn\) pól \(k\)-elementowe podzbiory (wiersze), następnie ustalić ich kolejność
      na \(k!\) sposobów, a na koniec ustawić każdy z wierszy na \(n!\) sposobów, więc do iloczynu
      dojdzie czynnik \((n!)^k\).
    </p>
    <p>
      Skoro pokazaliśmy, że powyższa równość jest prawdziwa, to możemy podzielić ją stronami
      przez \(k!(n!)^k\) i wtedy otrzymamy:
      $$\frac{(kn)!}{k!(n!)^k} = p(kn, k)$$
      Ponieważ prawa strona na pewno jest liczbą całkowitą, to lewa także musi nią być.
    </p>
  </div>
</div>


---

###Zadanie 2

Graf jest *k-zdegenerowany*, jeśli każdy jego podgraf zawiera wierzchołek stopnia
co najwyżej k (na przykład każdy graf planarny jest 5-zdegenerowany). Udowonij, że jeśli \\(G\\)
jest spójnym 100-wierzchołkowym grafem 10-zdegenerowanym, to liczba wierzchołków stopnia \\(\geq 30\\) jest mniejsza niż 66.

*WSKAZÓWKA: Co można powiedzieć o średnim stopniu wierzchołka w \\(G\\)?*

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Załóżmy, że mamy graf \(G\) będący grafem \(k\)-zdegenerowanym. Oznacza to, że ma on wierzchołek stopnia co najwyżej
      \(k\). Możemy go z niego usunąć, a wtedy suma stopni wszystkich pozostałych wierzchołków spadnie o co najwyżej \(2k\) (k od usuwanego wierzchołka i k od jego sąsiadów).
      W ten sposób otrzymujemy graf \(H \subset G\), ale z definicji \(k\)-zdegenerowania wynika, że on także posiada taki wierzchołek.
      Procedurę tę możemy kontynuować schodząc aż do grafu pustego.
    </p>
    <p>
      Ponieważ przy każdej iteracji suma stopni wierzchołków
      malała co najwyzej o \(k\), to możemy powiedzieć, że dla dowolnego grafu \(k\)-zdegenerowanego zachodzi: $$\sum_{i=1}^{\left|V(G)\right|} deg(v_i) \leq 2k\left|V(G)\right|$$
      Przekształcając te nierówność otrzymujemy:
      $$\frac{\sum_{i=1}^{\left|V(G)\right|} deg(v_i)}{\left|V(G)\right|} \leq 2k$$
      czyli, w grafie \(k\) zdegenerowanym średni stopień wierzchołka nie może przekraczać \(k\).
    </p>
    <p>
      Załóżmy teraz, że w grafie \(G\) liczba wierzchołków stopnia \( \geq 30\) jest większa niż 66. Mamy:
      $$\frac{\sum_{i=1}^{\left|V(G)\right|} deg(v_i)}{\left|V(G)\right|} \geq \frac{66\cdot 30+34\cdot 1}{100} = 20.14 \geq 20 = 2k$$
      (spójność grafu wymusza to, że pozostałe 34 wierzchołki musza mieć przynajmniej jedną krawędź), czyli graf \(G\) nie może być wtedy \(k\)-zdegenerowany.
    </p>
    <p>
      <b>Sprzeczność.</b>
    </p>
  </div>
</div>

---

###Zadanie 3

Liczbę naturalną n nazywany *tegoroczną*, jeśli rozkłąd n na czynniki pierwsze zawiera czynnik,
który występuje dokładnie w potędze 2013. Tak więc liczba \\(2^{2013}3^{5}\\) jest tegoroczna, ale liczba \\(5^{2014}7^{3000}\\) już nie (chociaż jest *przyszłoroczna*). Udowodnij,
że istnieje ciąg arytmetyczny o 2013 elementach i różnicy ciągów równej 2013, którego wszystkie elementy są tegoroczne.

*WSKAZÓWKA: Chińskie twierdzenie o resztach.*

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Niech \(p_n\) oznacza \(n\)-tą liczbę pierwszą.
    </p>
    <p>
      Szukamy liczby a będącej początkiem takiego ciągu.
      Możemy ułożyć układ 2013 równań postaci:
      $$(i)\ \ \ \ a \equiv -2013\cdot i\ (mod\ p_i)$$
      $$\left\{
          \begin{array}{lr}
            a \equiv 0\ (mod \ p_{1}^{2013})\\
            \ldots\\
            a + 2013\cdot i \equiv 0\ (mod \ p_{i}^{2013})\\
            \ldots\\
            a + 2013\cdot 2013\equiv 0\ (mod \ p_{2013}^{2013})
          \end{array}
        \right.$$
      Co można przepisać jako:
      $$\left\{
          \begin{array}{lr}
            a \equiv 0\ (mod \ p_{1}^{2013})\\
            \ldots\\
            a \equiv -2013\cdot i \ (mod \ p_{i}^{2013})\\
            \ldots\\
            a \equiv -2013\cdot 2013 \ (mod \ p_{2013}^{2013})\\
          \end{array}
        \right.$$
      Ponieważ \(\forall_{i,j}\ i \neq j \Rightarrow p_i \perp p_j\), to również
      \(\forall_{i,j}\ i \neq j \Rightarrow p_i^{2013} \perp p_j^{2013}\), a więc dzięki
      chińskiemu twierdzeniu o resztach możemy powiedzieć, że istnieje dokładnie jedna liczba
      \(a\) taka, że \(1 \leq a \leq p_1^{2013} \cdot \ldots \cdot p_{2013}^{2013}\) spełniająca
      wszystkie powyższe kongruencje.
    </p>
  </div>
</div>
