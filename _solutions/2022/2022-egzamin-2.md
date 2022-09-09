---
layout: page
permalink: /2022/egzamin/2/
---

## 2022 Egzamin poprawkowy

### Zadanie 1

<div>
Uprość sumę

$$ \sum^{n}_{k=0} {\binom{\binom{k}{2}}{2}} $$
</div>

---

### Zadanie 2

<div>
Niech \( L(n, k) \), gdzie \( k > 0 \), oznacza liczbę
sposobów podziału zbioru \( \{1,\ldots,n\} \) na \( k \)
podzbiorów liniowo uporządkowanych (np. \( L(3, 2) = 6: \{1, 23\}, \{1, 32\}, \{2, 13\}, \{2, 31\}, \{3, 12\}, \{3, 21\} \)).

<ol type="a">
  <li>
  Udowodnij tożsamość $$ L(n, k) = \sum^{n}_{j=0} {n\brack j}{j\brace k} $$
  </li>
  <li>
  Znajdź zwarty wzór na \( L(n, k) \).
  </li>
</ol>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <ol type="a">
      <li>
        <p>
          <em>Prawa strona:</em> Cykle \( n \) permutacji rozmieszczamy w \( k \) blokach.
          Takie rozmieszczenie możemy zakodować, zapisując każdy cykl począwszy od największego
          elementu i  ustawiając cykle w każdym bloku w rosnącej kolejności początkowych 
          elementów. W ten sposób otrzymujemy zbiór \( k \) niepustych list
          zawierających łącznie \( n \) elementów.
        </p>
        <p>
          <em>Lewa strona:</em> Tak samo jak w treści zadania, każdy podział można przedstawić jako zbiór \( k \) niepustych list
          zawierających łącznie \( n \) elementów.
        </p>
        <p>
          Stosując się do wyżej wymienionych zasad zapisu każdy taki zapis możemy zamienić na podział na bloki i cykle i na odwrót. Powielając przykład z treści zadania:
          <ul>
            <li>
              \( \{1, 23\} = [(1)],[(2)(3)] \) 
            </li>
            <li>
              \( \{1, 32\} = [(1)],[(32)] \) 
            </li>
            <li>
              \( \{2, 13\} = [(2)],[(1)(3)] \) 
            </li>
            <li>
              \( \{2, 31\} = [(2)],[(31)] \) 
            </li>
            <li>
              \( \{3, 12\} = [(3)],[(1)(2)] \) 
            </li>
            <li>
              \( \{3, 21\} = [(3)],[(21)] \) 
            </li>
          </ul>
        </p>
      </li>
      <li>
        <p>
          <em>Lewa strona:</em> Robimy tak samo jak w podpunkcie a, tylko, że tym razem
          ustawiamy bloki w kolejności rosnącej początkowych elementów początkowych cyklów.
          W ten sposób otrzymujemy listę \( k \) niepustych list
          zawierających łącznie \( n \) elementów, posortowaną względem początkowych elementów tych list.
        </p>
        <p>
          <em>Prawa strona:</em> Permutujemy \( n \) elementów, wyróżniamy pierwszą pozycję oraz
          \( k - 1 \) spośród \( n - 1 \) pozostałych. Wyróżnione elementy odpowiadają
          początkom list. Następnie zaniedbujemy kolejność list ustawiając je w rosnącej
          kolejności początkowych elementów. Można to zrobić na \( {n-1\choose k-1}\frac{n!}{k!} \) sposobów.
        </p>
      </li>
    </ol>
  </div>
</div>

---

### Zadanie 3

<div>
Niech \(P(x)\) będzie wielomianem chromatycznym poniższego grafu:

<p style="margin-top: 20px; margin-bottom: 20px">
<img src="/images/2022_egz2_zad3.svg" alt="2x2 grid"  style="display:block; margin-left:auto; margin-right:auto">
</p>

Znajdź \(P'(0)\).
</div>

---

### Zadanie 4

<div>
Znajdź liczbę rozwiązań kongruencji

$$ 1 + x + x^2 +x^3 + x^4 + x^5 + x^6 + x^7 + x^8 \equiv 0 \pmod{133} $$

w zbiorze \(\{0, 1,\ldots, 132\}\).
</div>

---
