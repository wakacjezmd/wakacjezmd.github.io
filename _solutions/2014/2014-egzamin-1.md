---
layout: page
permalink: /2014/egzamin/1/
---

## 2014 Pierwszy termin

###Zadanie 1
Udowodnij tożsamość

$$\sum_{k}{ n\brack k}{k\brace m} = {n\choose m}\frac{(n-1)!}{(m-1)!}$$

dla \\(n, m > 0\\)

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <b>LEWA:</b> Dzielimy \(n\) elementów na \(k\) cykli, a następnie cykle dzielimy na
      zbiory tak, że żaden zbiór nie może być pusty.
    </p>
    <p>
      <b>PRAWA:</b> Wybieramy \(m\) elementów, które będą początkami słów. Wyróżniamy jeden z nich
      i stawiamy go na pierwszym miejscu, a następnie permutujemy pozostałe \(n-1\) elementów.
      Następnie rozcinamy ten \(n\)-elementowy ciąg przed każdym z wybranych elementów i
      otrzymujemy ciąg \(m\) słów. Podzielenie przez \(m!\) przekształca ten ciąg w zbiór \(m\) słów.
      $${n\choose m}m\frac{(n-1)!}{m!} = {n\choose m}\frac{(n-1)!}{(m-1)!}$$
    </p>
    <p>
      Żeby udowodnić tę równość wskażę bijekcje pomiędzy obiema stronami. Jeżeli mamy już dany jakiś
      podział na cykle i ich zbiory, to popatrzmy na jeden ze zbiórów. Ustalmy że zapisujemy cykle tak,
      że zawsze pierwszy element cyklu jest najmniejszy ze wszystkich, które do niego należą (tak jak w zapisie kanonicznym),
      a w ramach całego zbioru ustawiamy je w kolejności malejącej względem pierwszego elementu.
      Starcie wszystkich nawiasów wyznacza bijekcje między zbiorem cykli, a słowem.
      $$(6)(358)(24) \mapsto 635824$$
      W drugą stronę, jeżeli mamy dane jakieś słowo, to możemy odzyskać zbiór cykli w następujący sposób:
      weźmy pierwszy element słowa i do jego cyklu dopisujmy po kolei następne elementy tak długo, aż
      któryś z nich nie będzie większy niż pierwszy element. Kiedy napotkamy taki, to w tym momencie kończymy cykl
      i powtarzamy procedurę zaczynając od napotkanego elementu.
      $$635824 \mapsto (6)35824 \mapsto (6)(358)24 \mapsto (6)(358)(24)$$
    </p>
</div>
</div>
###Zadanie 2
Znajdź liczbę 6-literowych słów złożonych z liter A, B, C, D, E w
których: każda z liter A, B występuje _co najwyżej raz_, a każda z liter
C, D - _co najmniej raz_.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
  Rozwiązanie oparte na rozwiązaniu zgłoszonym przez earlgreyz
  w <a href="https://github.com/wakacjezmd/wakacjezmd.github.io/issues/13">
  issue #13</a>
  </p>
  <p>
    Użyjemy zasady włączeń i wyłączeń.
  </p>
  <p>
    $$
    \begin{align}
    &X \text{- ciągi zawierające jedno \(A\) i jedno \(B\).} \\
    &Y \text{- ciągi zawierające albo tylko jedno \(A\) albo tylko jedno \(B\).} \\
    &Z \text{- ciągi bez \(A\) i bez \(B\).} \\
    &\cdot_C \text{- cecha niezawierania \(C\).} \\
    &\cdot_D \text{- cecha niezawierania \(D\).} \\
    &\hfill \\
    &|X| = 6 \cdot 5 \cdot 3^4 \\
    &|X_C| = |X_D| = 6 \cdot 5 \cdot 2^4 \\
    &|X_C \cap X_D| = 6 \cdot 5 \\
    &\hfill \\
    &|Y| = 6 \cdot 3^5 \\
    &|Y_C| = |Y_D| = 6 \cdot 2^5 \\
    &|Y_C \cap Y_D| = 6 \\
    &\hfill \\
    &|Z| = 3^6 \\
    &|Z_C| = |Z_D| = 2^6 \\
    &|Z_C \cap Z_D| = 1 \\
    \end{align}
    $$
  </p>
  <p>
    Z zasady włączeń i wyłączeń:
    $$
    \begin{align}
    \mathcal{D}_X(0) & = 6 \cdot 5 \ (3^4 - 2 \cdot 2^4 + 1) = 1500 \\
    \mathcal{D}_Y(0) & = 6 \ (3^5 - 2 \cdot 2^5 + 1) = 1080 \\
    \mathcal{D}_Z(0) & = 3^6 - 2 \cdot 2^6 + 1 = 602 \\
    \end{align}
    $$
    Zatem ostateczny wynik, to:
    $$
    \mathcal{D}_X(0) + 2\mathcal{D}_Y(0) + \mathcal{D}_Z(0) = 4262
    $$
  </p>
  <p>
    earlgreyz napisał też program weryfikujący powyższy wynik. Kod programu
    jest dostępny
    <a href="https://github.com/wakacjezmd/wakacjezmd.github.io/files/317096/abcde.cpp.txt">
    tutaj (link)</a>.
  </p>
  </div>
</div>

###Zadanie 3
Wierzchołki grafu \\(G\_n\\) to wszystkie liczby złożone ze zbioru
\\({1,\dots,n}\)) a para \\({i,j}\\) jest krawędzią wtedy i tylko wtedy gdy
\\(i\perp j\\). Rozstrzygnij czy graf \\(G\_{1000}\\) jest:

a) planarny

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
     Nie, następujące względnie pierwsze liczby: 4, 9, 25, 36, 49
     (kwadraty kolejnych liczb pierwszych)
     tworzą klikę \(K_5\) co z tw.
     Kuratowskiego oznacza że nie jest planarny.

  </div>
</div>

b) hamiltonowski

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
     <p>Skorzystam z twierdzenia o tym że jeżeli graf ma cykl hamiltona to
     usunięcie k wierzchołków spowoduje jego rozpadnięcie się na co
     najwyżej k składowych. </p>

     <p>Mamy dokładnie 499 wierzchołków etykietowanych liczbami parzystymi i
     zdecydowanie mniej wierzchołków nieparzystych (bo wiele spośród nich to
     liczby pierwsze). Po usunięciu wierzchołków nieparzystych których jest
     mniej niż 499 w grafie zostaje 499 wierzchołków parzystych które są
     izolowane gdyż w ich rozkładzie na czynniki pierwsze jest 2.</p>

     <p> Zatem nasz graf rozpadł się na 499 składowych i na mocy przytoczonego
     twierdzenia nie może być hamiltonowski. </p>
  </div>
</div>

c) eulerowski

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
     <p>Zbadajmy sąsiadów wierzchołka \(2\cdot 223\) (\(223\) to liczba pierwsza).
        Są to wszystkie nieparzyste liczby złożone, oprócz \(3\cdot 223\).
        Rozważmy teraz sąsiadów wierzchołka \(4\). Są to wszystkie nieparzyste
        liczby złożone. W takim razie stopnie wierzchołków \(4\) i \(2\cdot 223\)
        różnią się o \(1\), czyli jeden z nich musi być parzysty. W takim
        razie graf nie jest eulerowski.</p>
  </div>
</div>

###Zadanie 4

Uprość wyrażenie \\( \frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)}\\) gdzie \\(c(\pi)\\) to ilość cykli w permutacji \\(\pi\\).
<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
	Grupując elementy podanej sumy na grupki permutacji o takich samych ilościach cykli uzyskujemy, że
	$$ \sum\limits\_{\pi \in S\_k} n^{c(\pi)}=\\
	  \sum\limits\_{i=1}^{k} {k \brack i} n^i   $$
	Zauważmy, że ta suma zlicza nam ilość pokolorowań cykli wszystkich k-permutacji na n kolorów. <br><br>
	Spróbujmy generować takie kolorowania w inny sposób - tworząc permutacje w zapisie kanonicznym cyklowym z kolorom przypisanym cyklom.
	Elementy wstawiamy do cyklu w kolejności od najmniejszego do największego.
	Wstawiając pierwszy element do permutacji może on być pokolorowany na jeden z \\(n\\) kolorów.
	Drugi element może tworzyć nowy cykl i być pokolorowany na jeden z \\(n\\) kolorów,
	bądź stać w cyklu na prawo od elementu pierwszego i mieć taki sam kolor jak on.
	Łatwo widać że w takim wypadku daje nam to \\(n+1\\) możliwości. Uogólniając to rozumowanie, uzyskujemy następującą równość:
	$$   \sum\limits\_{i=1}^{k} {k \brack i} n^i =  n^\overline{k} $$
	Daje nam to odpowiedź:
$$ 	\frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)} = \frac{n^\overline{k}}{k!} $$
	 </p>
  </div>
</div>
