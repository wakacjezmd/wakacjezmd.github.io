---
layout: page
permalink: /2014/egzamin/1/
---

## 2014 Pierwszy termin

###Zadanie 1
Udowodnij tożsamość

$$\sum_{k}{ n\brack m}{n\brace m} = {n\choose m}\frac{(n-1)!}{(m-1)!}$$

dla n, m > 0


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
