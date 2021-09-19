---
layout: page
permalink: /2019/kolokwium/1/
---

## 2019 Kolokwium 1

### Zadanie 1

Udowodnij tożsamość:

$$ \sum^{k}_{i=0} {n \choose i} = \sum^{k}_{i=0} {n-1-i \choose k-i} 2^{i} \quad \textrm{dla}\ 0 \le k \le n. $$

---

### Zadanie 2

Znajdź liczbę przechodzących w prawo i do góry dróg na kratownicy
o początku \\( \langle 0, 0 \rangle \\) i końcu \\( \langle 9, 9 \rangle \\),
które przechodzą przez dokładnie jeden z punktów
\\( \langle 3, 3 \rangle \\), \\( \langle 4, 2 \rangle \\), \\( \langle 6, 6 \rangle \\).

---

### Zadanie 3

*Uporządkowanym podziałem* dodatniej liczby całkowitej \\(n\\), czyli *\\(n\\)-kompozycją* nazywamy
przedstawienie \\(n\\) w postaci sumy dodatnich składników,
przy czym kolejność składników w tym przedstawieniu jest istotna
(np. wszystkie 3-kompozycje to: \\(1 + 1 + 1\\), \\(1 + 2\\), \\(2 + 1\\), \\(3\\)).
Udowodnij, że uporządkowanych podziałów liczby \\(n\\) na składniki \\( \le 2 \\) jest tyle samo, co
uporządkowanych podziałów liczby \\(n+2\\) na składniki \\( \ge 2 \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Aby uzyskać wszystkie podziały \(n\) na składniki \( \le 2 \), możemy do każdego
      podziału \( n-1 \) dostawić na koniec składnik \( 1 \), a do każdego
      podziału \( n-2 \) dostawić na koniec składnik \( 2 \). To przejście jest
      wzajemnie jednoznaczne, bo każdy poprawny podział \( n \) będzie miał ostatni
      składnik równy \( 1 \) albo \( 2 \) (pozostałe składniki tworzą wówczas podział
      liczby odpowiednio \( n-1 \) albo \( n-2 \)).

      Stąd otrzymujemy wzór \( a_n = a_{n-1} + a_{n-2} \), co z warunkami brzegowymi
      \( a_1 = 1, a_2 = 2 \) daje nam \( a_n = F_{n+1} \), gdzie \( F_n \) to ciąg
      Fibbonacciego.
    </p>
    <p>
      Aby uzyskać wszystkie podziały \( n+2 \) na składniki \( \ge 2 \), możemy do każdego
      podziału \( n \) dostawić składnik \( 2 \), do każdego
      podziału \( n-1 \) dostawić składnik \( 3 \) i tak aż do \( n=0 \),
      gdzie do \( 2 \) dostawiamy składnik \( n \). Dodajemy jeszcze jeden podział z
      samotnym składnikiem \( n+2 \). To przejście jest wzajemnie jednoznaczne, bo każdy
      poprawny podział \( n+2 \) będzie miał ostatni składnik równy \( 2 \) lub więcej.

      Stąd otrzymujemy wzór \( a_n = a_{n-2} + a_{n-3} + \ldots + a_{1} + a_{0} + 1 \) z
      warunkami brzegowymi \( a_0 = 1, a_1 = 1 \).
    </p>
    <p>
      Pozostało pokazać, że drugi wzór rekurencyjny jest równoważny pierwszemu.
      Pozostawiamy to jako proste ćwiczenie na indukcję.
    </p>
  </div>
</div>

---
