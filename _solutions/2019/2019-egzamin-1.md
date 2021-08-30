---
layout: page
permalink: /2019/egzamin/1/
---

## 2019 Egzamin - Pierwszy termin

### Zadanie 1

Uprość sumę:

$$ \sum^{n}_{k=0} {n + k \choose k} 2^{-k} $$

---

### Zadanie 2

Podział liczby $$n$$ na składniki $$ a_{1} , ... , a_{r} $$, gdzie $$ a_{1} \leq ... \leq a_{r} $$,
nazywamy *gładkim*, jeśli $$ a_{1} = 1 $$ oraz $$ a_{i} - a_{i-1} \leq 1 $$ dla $$ 2 \leq i \leq r $$.
Znajdź enumerator podziałów gładich.

Wskazówka: wskaż bijekcję między podziałami gładkimi a pewną klasą podziałów o znanym (np. z wykładu)
enumeratorze.

---

### Zadanie 3

Niech \\(f(k)\\) oznacza iloczyn niezerowych cyfr liczby k (w szczególności \\(f(0) = 1\\), a np.
\\(f(2019) = 18\\)) i niech:

\\[ S(n) = \sum^{10^{n}-1}_{k=0} f(k) \\]

(suma wartości funkcji \\(f\\) dla wszystkich argumentów mających co najwyżej \(n\) cyfr). Oblicz
\\(S(100) \bmod 1001\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Zdefiniujmy \(B = 1 + 1 + 2 + 3 + \ldots + 9 = 46\). Zauważmy, że:

      \[
          S(k) = B^k.
      \]

      <em>Interpretacja.</em> Obliczamy iloczyn cyfr w liczbach, których długość jest nie większa od \(n\). Dla
      uproszczenia możemy przyjąć, że wszystkie liczby mniejsze od \(10^n\) są długości \(n\), z ewentualnymi wiodącymi
      zerami z przodu (jeśli długość danej liczby wynosi \(k\), to wówczas dopisujemy \(n - k\) zer wiodących). W
      iloczynie \(B^n\) wybieramy z \(i\)-tego nawiasu (gdzie \(i=1\ldots n\)) składnik, który odpowiada cyfrze na
      pozycji \(i\): dla zera \(1\), a dla pozostałych cyfr składnik odpowiednio od \(1\) do \(9\).
    </p>
    <p>
      Odnotujmy, że \(1001 = 7 \cdot 11 \cdot 13\). Ponieważ te składniki są pierwsze (a w szczególności parami względnie
      pierwsze), możemy zapisać układ równoważny szukanej kongruencji.

      \[
          \begin{cases}
          B^{100} \equiv a_1 &\bmod 7  \\[4pt]
          B^{100} \equiv a_2 &\bmod 11 \\[4pt]
          B^{100} \equiv a_3 &\bmod 13 \\[4pt]
          \end{cases}
      \]

      Korzystając z MTF i podstawowych własności kongruencji, łatwo wyznaczyć \(a_1, a_2, a_3\). Dla pierwszego równania
      mamy \(B^{100} \equiv 4^{100} \equiv 4^{4} \equiv 2^2 \equiv 4 \; (\text{mod } 7)\). Analogicznie rozwiązujemy pozostałe
      kongruencje i otrzymujemy wynik \((a_1, a_2, a_3) = (4, 1, 9)\).
    </p>
    <p>
      Znalezienie takiego \(a\), że \(B^{100} \equiv a \bmod 1001\), pozostawiamy jako proste ćwiczenie na
      zastosowanie konstruktywnego dowodu ChToR. (Oczekiwany wynik to \(a = 529\)).
    </p>
  </div>
</div>



---

### Zadanie 4

Znajdź liczbę nieizomorficznych grafów skierowanych, które po zamienieniu wszystkich krawędzi na
nieskierowane stają się izomorficzne z grafem $$ K_{3,3} $$

---



