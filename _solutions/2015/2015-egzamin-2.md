---
layout: page
permalink: /2015/egzamin/2/
---

## 2015 Egzamin poprawkowy

### Zadanie 1
<p>
  Znajdź liczbę \(k\)-krotek zbiorów \(\langle S_1, \dots, S_k \rangle\), gdzie \(S_1, \dots, S_k \subseteq \{1, \dots, n\}\)
  oraz <b>(a)</b> \(S_1 \subseteq S_2 \subseteq \dots \subseteq S_k\); <b> (b) </b> \(\mid S_1 \cap \dots \cap S_k \mid = r\);
  <b> (c) </b> \(S_1 \subseteq S_2 \supseteq S_3 \subseteq \dots \) (kierunek zawierania na zmianę).
</p>

---

### Zadanie 2
<p>
   <i> Pagórek </i> z monet to rozmieszczenie jednakowych monet w pewnej liczbie rzędów w taki sposób, że w każdym 
   rzędzie monety tworzą jeden spójny blok, a każda moneta w każdym rzędzie oprócz najniższego dotyka dokładnie dwóch monet 
   w rzędzie bezpośrednio poniżej, na przykład <img class="inline-image" src="/images/2015_2.png"> Niech \(a_n\) ozbnacza liczbę pagórków, w którym najniższy rząd zawiera dokładnie \(n\) monet. Znajdź funkcję tworzącą i zwarty wzór na \(a_n\). WSKAZÓWKA: Nietrudno zgadnąć wynik po obliczeniu kilku pierwszych wyrazów ciągu z równania rekurencyjnego.
</p>
---

### Zadanie 3
Znajdź Niech \\(G=(V,E)\\) będzie grafem takim, że \\(E=E\_1 \cup E\_2\\), gdzie graf
\\(G\_1=(V, E\_1)\\) jest planarny, zaś graf \\(G\_2=(V, E\_2)\\) jest lasem.
Udowodnij, że \\(\chi(G) < 9\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    <b>Wskazówka:</b>
  </p>
  <p>
    Narysuj 5 grafów \(K_4\). Nazywij je \(A, B, C, D, K\). Ich wierzchołki
    ponumeruj i nazwij według następującego schematu: graf \(A\) posiada
    wierzchołki \(a_1, a_2, a_3, a_4\).
  </p>
  <p>
    Stwórz drzewa z korzeniami w wierzchołkach \(K\). Niech \(k_1\) będzie
    połączone z wierzchołkbmi \(b_1, b_2, b_3, b_4\),
    \(k_2\) z \(b_1, b_2, b_3, b_4\), itd.
  </p>
  </div>
</div>

---

### Zadanie 4

Oblicz \\((1\cdot 3\cdot 5\dots 97)^2 \mod{101}\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    Zauważmy, że
    $$
    \begin{align*}
      1 &\equiv -100 &&\pmod {101} \\
      3 &\equiv -98 &&\pmod {101} \\
      5 &\equiv -96 &&\pmod {101}
    \end{align*}
    $$
    Stąd
    $$
    x \equiv (1 \cdot 3 \cdot 5 \dots 97)((-100)\cdot(-98)\dots(-4)) \pmod{101}
    $$
  </p>
  <p>
    Z twierdzenia Wilsona wiemy, że \(100! \equiv -1 \pmod{101}\). Zatem
    $$
    \begin{align*}
      &4x \equiv
      2 \cdot 2\ (1 \cdot 3 \cdot 5 \dots 97)((-100)\cdot(-98)\dots(-4))
      \pmod{101} \\

      &4x \equiv
      2 \cdot (-99)\ (1 \cdot 3 \cdot 5 \dots 97)((-100)\cdot(-98)\dots(-4))
      \pmod{101} \\

      &\begin{cases}
        4x &\equiv 100! &&\pmod{101} \\
        100! &\equiv -1 &&\pmod{101}
      \end{cases} \\

      &4x \equiv -1 \pmod{101} \\
    \end{align*}
    $$
    Stąd \(x = 25\).
  </p>
  <p>
    Wynik można sprawdzić poniższymi metodami:
    <ul>
      <li>
        Mathematica:
        <pre><code>
          Mod[Power[Product[i, {i, 3, 97, 2}], 2], 101]
        </code></pre>
      </li>
      <li>
        WolframAlpha:
        <pre><code>
          (product 2*n+1, 1 to 48)^2 mod 101
        </code></pre>
      </li>
    </ul>
  </p>
  <p>
    Do badania kongruencji w Matematice przydaje się <code>Reduce</code>:

    <pre><code>
      Reduce[4x == -99*2*100!, Modulus -> 101]
    </code></pre>
  </p>
  </div>
</div>


---
