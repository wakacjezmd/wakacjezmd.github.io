---
layout: page
permalink: /2011/egzamin/1/
---

## 2011 Egzamin

###Zadanie 1

Niech \\(b\_r (n,k)\\) oznacza liczbę \\(n\\)-permutacji o \\(k\\) cyklach, w których wszystkie liczby
\\(1,2,...,r\\) są w jednym cyklu. Udowodnij że dla \\(n \geq r\\) mamy:

$$ \sum\limits\_{k=1}^n b\_r (n,k) x^k = (r-1)! \frac{x^\overline{n}}{(x+1)^\overline{r-1} } $$

*WSKAZÓWKA: Indukcja.*

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
	Indukcję będziemy robili po n. Wykorzystamy poniższą obserwację:

	$$ b_r (n+1,k) = n b_r(n,k) + b_r(n,k-1) $$

	Rozpatrzmy permutacje \(n+1\) elementowe. Permutacji, w których liczba \(n+1\) jest sama w cyklu jest \(b_r (n,k-1)\).
	Permutacji, w których ta liczba jest w innym cyklu jest \(n b_r (n,k) \) ponieważ liczba ta mogła zostać dostawiona po prawej od dowolnego elementu w kanonicznym zapisie cyklowym
	(czyli takim w którym każdy cykl zapisujemy tak aby najmniejszy element był pierwszy oraz sortujemy cykle po pierwszym elemencie rosnąco). <br>

	Dla \(n=1\) zauważamy, że musi być \(r=1\) i wtedy zdanie jest prawdziwe w oczywisty sposób. Teraz załóżmy, że teza jest prawdziwa dla pewnego \(n\), udowodnę że jest także prawdziwa dla \(n+1\).

	$$  \sum\limits_{k=1}^{n+1} b_r (n+1,k) x^k = \\
	    n \sum\limits_{k=1}^{n+1} b_r (n,k) x^k + \sum\limits_{k=1}^{n+1} b_r (n,k-1) x^k = \\
	    n \sum\limits_{k=1}^{n} b_r (n,k) x^k + \sum\limits_{k=0}^{n} b_r(n,k)x^{k+1} = \\
	    n \sum\limits_{k=1}^{n} b_r (n,k) x^k + x \sum\limits_{k=1}^{n} b_r(n,k)x^{k} = \\
	    (n+x) (r-1)! \frac{x^\overline{n}}{(x+1)^\overline{r-1}} = \\
	    (r-1)! \frac{x^\overline{n+1}}{(x+1)^\overline{r-1}} $$

	Pierwsza równość została otrzymana poprzez zastosowanie obserwacji. Druga poprzez usunięcie wyrazu zerowego z pierwszej sumy oraz przeindeksowanie drugiej.
	Trzecia poprzez wyrzucenie zerowego wyrazu z drugiej sumy. Kolejne równości to zastosowanie założenia indukcyjnego i proste rachunki na silniach.

    </p>
  </div>
</div>
