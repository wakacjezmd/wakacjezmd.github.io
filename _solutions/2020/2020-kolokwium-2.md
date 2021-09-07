---
layout: page
permalink: /2020/kolokwium/2/
---

## 2020 Kolokwium 2

### Zadanie 1

<div>
Znajdź liczbę etykietowanych drzew \(10\)-wierzchołkowych, które zawierają drzewo

<p style="margin-top: 20px; margin-bottom: 20px">
<img src="/images/2020_2nd_test_1.svg" alt="(1)--(2)--(3)"  style="display:block; margin-left:auto; margin-right:auto">
</p>

jako podgraf.
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <em>Fun fact: </em>ktoś (pewnie z MIMu) zadał w wakacje 2020 roku
  <a href="https://math.stackexchange.com/q/3793447">pytanie o to zadanie</a>
  na <code>math.stackexchange</code>.
  </div>
</div>

---

### Zadanie 2

Niech \\(G_1, \ldots, G_{10}\\) będą grafami planarnymi o tym samym zbiorze wierzchołków \\(V\\) i zbiorach krawędzi
odpowiednio \\(E_1, \ldots, E_{10}\\). Rozważmy stanowiący ich sumę graf \\(G = \langle V, E \rangle\\), gdzie \\(E =
\cup_{i=1}^{10} E_i\\). Udowodnij, że \\( \chi(G) \leq 60 \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <ol>
    <li>
    <p>
    <em>Lemat.</em> Dla grafu \(E\) (określonego tak, jak w z treści zadania), istnieje wierzchołek \(v\) taki, że
    \(\deg(v) \leq 59\).
    </p>
    <p>
    <em>Dowód.</em>
    Korzystając ze standardowej nierówności dla grafów planarnych (wynikającej ze wzoru Eulera) oraz lematu o uściskach
    dłoni, odnotujmy, że:
    \[
        \textstyle
        |E_i| \leq 3|V| - 6 \implies  2|E| = 2|\bigcup_{i} E_i| \leq 2\sum_{i} |E_i| \leq 60 |V| - 120
    \]
    Dalej załóżmy, że taki wierzchołek nie istnieje. Czyli najmniejszy stopień wierzchołka w grafie wynosi \(60\). Stąd
    mamy \(\sum_{v \in V} \deg(v) \geq 60 |V|\). Sprzeczność.
    </p>
    </li>

    <li style="margin-top: 15px">
    <p>
    <em>Lemat.</em> Graf określony tak, jak w treści zadania, można pokolorować na \(60\) kolorów lub mniej.
    </p>
    <p>
    <em>Dowód.</em> Rozważmy \(2\)-graf. Da się go pokolorować na dwa kolory. Rozważmy dowolny \(n\)-graf. Rozważmy
    \((n-1)\)-graf powstały z \(n\)-grafu przez usunięcie wierzchołka \(v\) spełniającego \(\deg(v) \leq 59\) oraz
    krawędzi z nim incydentnych. Oczywiście taki graf również spełnia warunki zadania, więc na mocy założenia
    indukcyjnego można pokolorować go na \(60\) kolorów lub mniej. Przenieśmy kolorowanie \(n-1\) wierzchołków na
    wejściowy \(n\)-graf.  Ponieważ stopień wierzchołka \(v\) jest mniejszy od \(60\), to w zbiorze \(60\) kolorów
    znajdzie się kolor, który nie występuje wśród wierzchołków sąsiadujących.
    </p>

    </li>
    </ol>
  </div>
</div>

---

### Zadanie 3

<div>
Udowodnij, że liczby \(n \geq 2\) oraz \(n+1\) są jednocześnie pierwsze wtedy i
tylko wtedy, gdy:

\[
    4(n-1)! + 4 + n \equiv 0 \mod n(n+2)
\]
</div>
