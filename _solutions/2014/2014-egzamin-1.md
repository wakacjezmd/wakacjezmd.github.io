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
     <p>Użyjemy wykładniczych funkcji tworzących. Na początku policzymy WFT dla
     słów złożonych tylko jednej litery, a potem je spleciemy.</p>
     <p>Dla litery A istnieje dokładnie jedno słowo długości zero zawierające co
     najwyżej raz literę A, podobnie dla słowa długości 1. Słowa o długości większej
     niż 1 i składające się wyłącznie z liter A nie istnieją. Zapiszmy enumerator:
     \(\sum^{\infty}_{n=0}([n=0]+[n=1])\frac{z^n}{n!} = z + 1\). Taki sam enumerator
     wyjdzie dla B.</p>
     <p>W przypadku gdy rozpatrujemy słowa długości \(n\) złożone tylko z litery C
     to będzie istniało tylko jedno słowo o ile \(n \ne 0\). Enumerator wygląda tak:
     \(\sum^{\infty}_{n=0}[n\ne 0]\frac{z^n}{n!} = \sum^{\infty}_{n=0}\frac{z^n}{n!} - 1 = e^z - 1\). To samo dla litery D.</p>
     <p>Na literę E nie nakładamy żadnych ograniczeń zatem enumeratorem jest
     \(\sum^{\infty}_{n=0}\frac{z^n}{n!} = e^z\).</p>
     <p>Teraz należy to wszystko ze sobą spleść:
     \((z+1)^2(e^z-1)^2e^z = (z^2+2z+1)(e^{3z}-2e^{2z}+e^z)\). Po wymnożeniu
     otrzymamy sumę następujących enumeratorów (strzałką oznaczyłem wynik wyciągnięty
     z enumeratora tj. wartość przy \(\frac{z^6}{6!}\) w otrzymanym szeregu):<br>
     \(e^z = \sum^{\infty}_{n=0}\frac{z^n}{n!} \leadsto 1\) <br>
     \(-2\cdot e^{2z} = -2 \cdot \sum^{\infty}_{n=0}\frac{(2z)^n}{n!} =
     \sum^{\infty}_{n=0}(-2 \cdot 2^n \frac{z^n}{n!})  \leadsto -2\cdot 2^6\) <br>
     \(e^{3z} \leadsto 3^6\) <br>
     \(2z\cdot e^z = 2\cdot \sum^{\infty}_{n=0}z\cdot \frac{z^n}{n!} =
     2\cdot \sum^{\infty}_{n=0}\frac{n+1}{n+1}\cdot \frac{z^{n+1}}{n!} =
     2\cdot \sum^{\infty}_{n=0}(n+1)\cdot \frac{z^{n+1}}{(n+1)!}\leadsto 2\cdot 6\)<br>
     \(-4z\cdot e^{2z} \leadsto -4\cdot 2^5\cdot 6\) <br>
     \(2z\cdot e^{3z} \leadsto 2\cdot 3^5\cdot 6\) <br>
     \(z^2\cdot e^z \leadsto 6\cdot 5\) <br>
     \(-4\cdot z^2\cdot e^{2z} \leadsto -4\cdot 2^4\cdot 6\cdot 5 \) <br>
     \(z^2\cdot e^{3z} \leadsto 3^4\cdot 6\cdot 5\) <br>
     Teraz wystarczy wszystko do siebie dodać. Wychodzi
     \(602 + 2160 + 540 = 3302\).
     </p>
  </div>
</div>

###Zadanie 3
Wierzchołki grafu \\(G\_n\\) to wszystkie liczby złożone ze zbioru
{1,...,n} a para {i,j} jest krawędzią wtedy i tylko wtedy gdy
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
