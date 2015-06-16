---
layout: page
permalink: /2010/egzamin/2/
---

## 2010 Egzamin poprawkowy

###Zadanie 2

Niech \\(c(V,T)\\) oznacza liczbę spójnych składowych grafu o zbiorze wierzchołków \\(V\\) i zbiorze krawędzi \\(T\\) i niech
\\(P_g (x)\\) oznacza wielomian chromatyczny grafu \\(G\\). Udowodnij, że:

**a)** $$ P\_g (x) = \sum\_{T \subseteq E(G)} (-1)^{|T|} x^{c(V(G), T)} $$
*WSKAZÓWKA: Użyj zasady włączania-wyłączania*


**b)** Udowodnij, że wartość \\(P_{G}^{'} (0)\\) jest równa różnicy spójnych grafów rozpinających \\(G\\) o odpowiednio parzystej
i nieparzystej liczbie krawędzi.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
 	Niech naszym uniwersum \(X\) będą kolorowania grafu \(G\).
	Niech zdarzeniem \(A_e\) będzie to, że końce krawędzi \(e\) mają jednakowy kolor.
	Zastanówmy się co to jest \(S_j\). Jest to ilość kolorowań posiadających dokładnie \(j\) własności.
	To znaczy, że \(j\) krawędzie ma końce tego samego koloru.
	Ilość takich kolorowań jest rónwa \( \sum_{T \subseteq G \wedge |T|=2} x^c(V(G), T) \),
	ponieważ wszystkie wierzchołki wewnątrz SS muszą mieć ten sam kolor, a każdą SS możemy kolorować niezależnie
	na jeden z x kolorów.

	W tym momencie korzystamy ze wzoru na ilość elementów posiadających 0 własności - da to nam ilość
	kolorowań wierzchołkowych grafu na x kolorów - czyli nasz wielomian chromatyczny ;). Jest to
	$$ D(0) = \sum_{j} (-1)^j S_j = \sum_{T \subseteq E(G)} (-1)^{|T|} x^{c(V(G), T)} $$

	Drugi podpunkt jest prostszy. Zauważmy że jak policzymy pochodną i przyłożymy \( x = 0 \) to zostaną
	nam we wzorze jedynie wyrazy w których po policzeniu pochodnej nie było \(x\), czyli takie gdzie
	\(x\) był w pierwszej potędze. Czyli ilość spójnych składowych danego podgrafu \(T\) była równa jeden.
	Czyli \(T\) rozpina \(G\).

	Wybrany wyraz będzie pomnożony przez \( (-1)^{|T|} \) zatem gdy ilość krawędzi parzysta to \(1\),
	a jak nieparzysta to \(-1\). Sumując po wszystkich takich \(T\) dostajemy dokładnie to o co było pytanie w zadaniu.
    </p>
  </div>
</div>
