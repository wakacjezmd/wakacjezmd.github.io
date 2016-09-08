---
layout: page
permalink: /2011/egzamin/1/
---

## 2011 Egzamin

###Zadanie 1

Niech \\(b\_r (n,k)\\) oznacza liczbę \\(n\\)-permutacji o \\(k\\) cyklach, w
których wszystkie liczby \\(1,2,...,r\\) są w jednym cyklu. Udowodnij, że dla
\\(n \geq r\\) mamy:

$$
\sum\limits\_{k=1}^n b\_r (n,k) x^k = (r-1)! \frac{x^\overline{n}}{(x+1)^\overline{r-1} }
$$

*WSKAZÓWKA: Indukcja.*

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Indukcję będziemy robili po n. Wykorzystamy poniższą obserwację:

      $$
      b_r (n+1,k) = n b_r(n,k) + b_r(n,k-1)
      $$

      Rozpatrzmy permutacje \(n+1\) elementowe. Permutacji, w których liczba
      \(n+1\) jest sama w cyklu jest \(b_r (n,k-1)\).  Permutacji, w których ta
      liczba jest w innym cyklu jest \(n b_r (n,k) \), ponieważ liczba ta mogła
      zostać dostawiona po prawej od dowolnego elementu w kanonicznym zapisie
      cyklowym (czyli takim, w którym każdy cykl zapisujemy tak, aby najmniejszy
      element był pierwszy oraz sortujemy cykle po pierwszym elemencie rosnąco).
    </p>
    <p>
      Dla \(n=1\) zauważamy, że musi być \(r=1\) i wtedy zdanie jest prawdziwe w
      oczywisty sposób. Teraz załóżmy, że teza jest prawdziwa dla pewnego \(n\),
      udowodnę, że jest także prawdziwa dla \(n+1\).

      $$
      \sum\limits_{k=1}^{n+1} b_r (n+1,k) x^k = \\
      n \sum\limits_{k=1}^{n+1} b_r (n,k) x^k + \sum\limits_{k=1}^{n+1} b_r (n,k-1) x^k = \\
      n \sum\limits_{k=1}^{n} b_r (n,k) x^k + \sum\limits_{k=0}^{n} b_r(n,k)x^{k+1} = \\
      n \sum\limits_{k=1}^{n} b_r (n,k) x^k + x \sum\limits_{k=1}^{n} b_r(n,k)x^{k} = \\
      (n+x) (r-1)! \frac{x^\overline{n}}{(x+1)^\overline{r-1}} = \\
      (r-1)! \frac{x^\overline{n+1}}{(x+1)^\overline{r-1}}
      $$

      Pierwsza równość została otrzymana poprzez zastosowanie obserwacji. Druga
      poprzez usunięcie wyrazu zerowego z pierwszej sumy oraz przeindeksowanie
      drugiej.  Trzecia poprzez wyrzucenie zerowego wyrazu z drugiej sumy.
      Kolejne równości to zastosowanie założenia indukcyjnego i proste rachunki
      na silniach.
    </p>
  </div>
</div>

### Zadanie 2

Znajdź największą potęgę dwójki, która dzieli \\(3^{2^k} -1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    Rozwiązanie jest dostępne na stronie
    <a href="http://wakacjezmd.wikidot.com/2011-czerwiec">
      Wakacji z Matematyką Dyskretną w serwisie wikidot.com
    </a>.
  </p>
  </div>
</div>

### Zadanie 3

Kolorujemy wierzchołki czworościanu foremnego z użyciem 3 kolorów, a krawędzie
z użyciem 2 kolorów. Oblicz, na ile istotnie różnych sposobów można to zrobić,
jeśli utożsamiamy takie kolorowania, że jedno przechodzi na drugie przy pewnym
obrocie czworościanu w \\(\Bbb{R}^3 \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Grupa obrotów czworościanu foremnego zawiera 12 elementów - identyczność,
      po 2 obroty (w prawo i w lewo)  przy osiach przechodzących przez wybrany
      wierzchołek i środek podstawy \(2\cdot 4\), i po 1 obrocie dla osi
      przechodzącej przez środki przeciwległych krawędzi \(1\cdot 3\).
      (Dokładniej obroty można zobaczyć
      <a href="https://upload.wikimedia.org/wikipedia/commons/9/98/Tetrahedral_group_2.svg">tutaj</a>).
    </p>
    <p>
      Dla każdego obrotu chcemy policzyć liczbę punktów stałych, to jest takie
      kolorowanie wierzchołków i krawędzi, które po zastosowaniu obrotu
      pozostaje niezmienione (tj. dla przykładu krawędź \(a\), która po obrocie
      przechodzi na miejsce krawędzi \(b\), powinna mieć taki sam kolor jak
      krawędź \(b\)). Dzięki temu, po zastosowaniu Lematu Burnside'a, będziemy
      w stanie wyznaczyć liczbę orbit, tj. odpowiedzieć na pytanie, ile jest
      unikalnych kolorowań. Każdy czworościan powstały przez obrót traktujemy
      jako pewną permutację
      \(\left\{1,2,3,4\right\}\times \left\{1,2,3,4,5,6\right\}\) (lewa
      permutacje jednoznacznie określa położenie wierzchołków, a prawa
      położenie krawędzi). W takim razie obrót ma też powiązany z nim rozkład
      na cykle. Można zauważyć, że jeśli mamy jeden cykl, to żeby przy obrocie
      kolorowanie zostało niezmienione, wszystkie elementy z cyklu muszą mieć
      ten sam kolor (na tej samej zasadzie, co wcześniej pokazany przykład
      z dwoma krawędziami). Rozpatrzmy dla przykładu obrót przez oś symetrii
      przechodzącą przez jeden z wierzchołków (żeby ukonkretyzować, chodzi o
      operacje przedstawioną <a href="http://i.imgur.com/p3ipW7wh.jpg">tu</a>
      - czyli obrót w prawo o 60 stopni z osią symetrii przechodzącą przez
      wierzchołek \(D\), omówie tylko kolorowanie wierzchołków, z krawędziami
      numerujemy krawędzie i postępujemy analogicznie).
    </p>
    <p>
      Widać że permutacja składa się z cykli
      \(\left[A,C,B\right]\left[D\right]\). Oznacza to, iż dla tego obrotu,
      punktów stałych jest \(3^2\) - na 3 sposoby wybieramy kolor dla cyklu
      pierwszego, to samo dla drugiego. Jeśli chodzi o krawędzie, obrót będzie
      składał się z dwóch cykli 3 elementowych - krawędzie wychodzące
      z wierzchołka D, i tworzące trójkąt ABC, czyli punktów stałych dla
      kolorowań krawędzi będzie \(2^2\); w takim razie punkty stałe kolorowań
      wierzchołków i krawędzi są równoliczne z liczbą par (unikalne kolorowanie
      wierzchołków, unikalne kolorowanie krawędzi) - ich jest \(3^2 2^2\).
    </p>
    <p>
      Policzyliśmy liczbę punktów stałych dla osi obrotu przechodzącej przez
      ustalony wierzchołek. Pozostała nam identyczność - tutaj cykli dla
      wierzchołków jest tyle samo co wierzchołków, tak samo dla krawędzi, czyli
      punktów stałych jest \(3^4 2^6\) - a także obrót przez oś przechodzącą
      przez środki przeciwległych krawędzi - tu cykli jest - po 2 dla
      wierzchołków i po 4 dla krawędzi (przy tym obrocie krawędzie przechodzą
      same na siebie), czyli punktów stałych jest \(3^2 2^4\).
    </p>
    <p>
      Pozostało skorzystać z lematu Burnside'a, co da nam liczbę orbit. Jego
      postać dla naszego problemu to
      $$
      \frac{1}{12} (3^4\cdot 2^6 + 8 \cdot 3^2 \cdot 2^2 + 3 \cdot 3^2\cdot 2^4) = 492
      $$
    </p>
  </div>
</div>
