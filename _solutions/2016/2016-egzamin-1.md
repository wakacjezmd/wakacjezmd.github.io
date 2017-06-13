---
layout: page
permalink: /2016/egzamin/1/
---

## 2016 Pierwszy termin

### Zadanie 1

Udowodnij tożsamość \\(\sum^n\_{k=1}(-1)^k(k-1)!{n \brace k} = 0\\) dla
\\(n > 1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    $$
    \begin{align*}
      \sum^n_{k=1}(-1)^k(k-1)!{n \brace k}
      &=\sum^n_{k=1}(-1)^k(k-1)!\left(k{n-1 \brace k} +
       {n-1 \brace k-1}\right) = \\
      &=\sum^n_{k=1}(-1)^k k!{n-1 \brace k} +
       \sum^n_{k=1}(-1)^k (k-1)!{n-1 \brace k-1}
    \end{align*}
    $$
  </p>
  <p>
    Teraz rozpiszmy obie sumy:
    $$
    \begin{align*}
      &=&&- 1!{n-1 \brace 1}
       + 2!{n-1 \brace 2}
       - 3!{n-1 \brace 3}
       + \dots
       + (-1)^{n-1}(n-1)!{n-1 \brace n-1}
       + (-1)^{n}n!{n-1 \brace n} + \\
      &&&- 0!{n-1 \brace 0}
       + 1!{n-1 \brace 1}
       - 2!{n-1 \brace 2}
       - \dots
       + (-1)^{n-1}(n-2)!{n-1 \brace n-2}
       + (-1)^{n}(n-1)!{n-1 \brace n-1}\\
    \end{align*}
    $$
  </p>
  <p>
    Możemy zauważyc redukcję kolejnych wyrazów, w wyniku czego, powyższa suma zredukuje się do:
    $$
    \begin{align*}
      = -0!{n-1 \brace 0} + (-1)^{n} \cdot n! \cdot {n-1 \brace n}
      = 1 \cdot [n-1 = 0] + (-1)^{n} \cdot n! \cdot 0 = 0 + 0 = 0
    \end{align*}
    $$
  </p>
  </div>
</div>

---

### Zadanie 2

Niech \\( UP(n) \\) będzie zbiorem _uporządkowanych podziałów_ liczby \\( n \\),
czyli ciągów \\( a = (a_1, \dots, a_k) \\) dodatnich liczb całkowitych
takich, że \\( a_1 + \dots + a_k = n \\), i niech
\\( f(a) = a_1 \cdot a_2 \dots a_n \\) będzie _iloczynem składników_ takiego
podziału. Udowodnij, że \\( \sum\limits_{a \in UP(n)}f(a) = F_{2n} \\), gdzie
\\( F_n \\) oznacza \\( n \\)-tą liczbę Fibonacciego.

_Wkazówka_: Niech \\( a' \\) oznacza podział powstający z
\\( a \\) przez zastąpienie ostatniego składnika jedynką. Rozważ
\\( \sum\limits_{a \in UP(n)} f(a') \\)

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  <p>
    Tezę rozszerzamy o dodatkowy warunek:
    $$
    \sum\limits_{a \in UP(n)}f(a') = F_{2n - 1}, ~~ n > 0
    $$
  </p>
  <p>
    Rozumujemy przez indukcję po \( n \). Baza indukcyjna jest oczywista:
  </p>
  <p>
    $$
    \sum\limits_{a \in UP(1)}f(a) = 1 = F_2 \qquad
    \sum\limits_{a \in UP(1)}f(a') = 1 = F_1
    $$
  </p>
  <p>
    Załóżmy teraz, że teza jest prawdziwa dla \( n \in \mathbb{N} \).
    Weźmy \( a \in UP(n+1) \). Możemy rozpatrzyć dwa przypadki:
    <ul><li>
      \( a \) <b>kończy się jedynką</b>. Zbiór takich \( a \) oznaczmy przez
      \( A \). Taki podział możemy otrzymać z pewnego \( b \in UP(n) \)
      przez dopisanie jedynki na końcu. Wówczas oczywiście
      \( f(a') = f(a) = f(b) \) (gdzie \( a' \) - jak we wskazówce)
    </li>
    <li>
      \( a \) <b>kończy się liczbą</b> \( \neq 1 \). Zbiór takich \( a \)
      oznaczmy przez \( B \). Taki podział otrzymujemy przez dodanie jedynki do
      <b>ostatniego składnika</b> pewnego \( b \in UP(n) \). Wówczas
      oczywiście \( f(a') = f(b') \)<br>
      Takie przypisanie \( a \to b \) jest <b>na</b>, co jest istotne
      dla reszty dowodu.
    </li></ul>
  </p>
  <p>
    Jasne jest zatem, że \( A \cup B = UP(n+1), A \cap B = \emptyset \) oraz
    (korzystając z założenia indukcyjnego):
    $$
    \sum\limits_{a \in A} f(a') = \sum \limits_{b \in UP(n)} f(b) = F_{2n}
    $$
    $$
    \sum\limits_{a \in B} f(a') = \sum \limits_{b \in UP(n)} f(b') = F_{2n - 1}
    $$
    Z czego wynika, że
    $$
    \sum\limits_{a \in UP(n+1)} f(a') =
        \sum\limits_{a \in A} f(a') + \sum\limits_{a \in A} f(a') =
        F_{2n} + F_{2n - 1} = F_{2n + 1}
    $$
  </p>
  <p>
    Dalej, wiemy, że \( \sum_{a \in A}f(a) = \sum_{a \in A}f(a') = F_{2n} \).
    Ponadto dla \( a \in B \) zachodzi tożsamość
    \( f(a) = f(b) + f(b') \), z czego bezpośrednio wynika
    $$
        \sum\limits_{a \in B}f(a) = \sum\limits_{b \in UP(n)}f(b)
                                  + \sum\limits_{b' \in UP(n)}f(b) =
                                    F_{2n} + F_{2n-1} = F_{2n+1}
    $$
    Ostatecznie
    $$
        \sum\limits_{a \in UP(n)}f(a) = \sum\limits_{a \in A}f(a)
                                      + \sum\limits_{a \in B}f(a) =
                                        F_{2n} + F_{2n+1} = F_{2n+2}
    $$
    Co kończy dowód
  </p>
  </div>
</div>
---

### Zadanie 3

Uprość sumę \\(\sum^n\_{k-1}\left\lfloor \frac{n}{k} \right\rfloor \phi(k)\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <a href="http://math.stackexchange.com/questions/1155433/euler-phi-function-and-floor-function">
        http://math.stackexchange.com/questions/1155433/euler-phi-function-and-floor-function
      </a>
    </p>
  </div>
</div>

---

### Zadanie 4

---
