---
layout: page
permalink: /2016/egzamin/2/
---

## 2016 Egzamin poprawkowy

### Zadanie 1
<p>
  Oblicz \(\sum_{k=0} ^n \binom{2n+1}{2k+1}2^{3k} \bmod 5\).
</p>

<div>
  <h4 class="collapsible"><a href="https://math.stackexchange.com/questions/822230">Rozwiązanie (link)</a></h4>
</div>

---

### Zadanie 2
<p>
  <p>
    Dla ustalonego podziału \(\pi\) liczby \(n\), niech \(A(\pi)\) oznacza liczbę jedynek w \(\pi\), zaś \(B(\pi)\) — liczbę różnych składników w \(\pi\).
  </p>
  <p>
    PRZYKŁAD: dla podziału \(\pi: 1 + 1 + 2 + 2 + 2 + 4\) mamy \(A(\pi)=2\) oraz \(B(\pi)=3\).
  </p>
  <p>
    Udowodnij, że \(\sum_{\pi} A(\pi) = \sum_{\pi} B(\pi)\), gdzie sumowanie odbywa się po wszystkich podział ustalonej liczby \(n\).
  </p>
  <p>
    WSKAZÓWKA: Spróbuj wyrazić każdą ze stron tożsamości przez \(P(1), P(2), \dots, P(n-1)\), gdzie \(P(k)\) to łączna liczba
    podziałów liczby \(k\).
  </p>
</p>

---

### Zadanie 3

<p>
Udowodnij, że jeśli turniej nie zawiera skierowanego trójkąta, to można ustawić jego wierzchołki w takiej kolejności \( v_1, \dots, v_n \), że jeśli \( i < j \), to skierowana krawędź prowadzi od \(v_i\) do \(v_j\).
</p>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
        Lemat: W turnieju bez trójkątów istnieje wierzchołek \(v\), taki że \( deg_{out}(v) = 0 \)
        Dowód:
        Załóżmy, że wierzchołek o najmniejszym stopniu wyjściowym \(p\) spełnia \( deg_{out}(p) = k (k > 0) \).
        Każdy wierzchołek \( c \) t. że \( p \to c \) także musi mieć \( deg_{out} \) co najmniej \( k \), ale istnieje
        tylko \( k - 1 \) wierzchołków, do których może prowadzić bez utworzenia trójkąta z \(p\), co prowadzi do sprzeczności z założeniem, że \( p \) ma najmniejszy stopień. Zatem \( k \leq 0 \), czyli \( k = 0 \).

        Teraz możemy usunąć z turnieju wierzchołek o stopniu wychodzącym 0 i zostanie nam \( n-1 \) - turniej, który też nie zawiera skierowanego trójkąta.
        Usuwając z \( k \) -turnieju taki wierzchołek oznaczamy go jako \( v_k \) i w oryginalnym turnieju spełni on warunek danej nam kolejności,
        ponieważ istniała krawędź od niego do wszystkich usuniętych przed nim wierzchołków.
    </p>
  </div>
</div>


---

### Zadanie 4

<p>
  <p>
    Udowodnij, że jeśli \(a\) i \(n\) są dodatnimi liczbami całkowitymi, to \(n \mid \phi(a^n-1)\).
  </p>
  <p>
    WSKAZÓWKA: Rozważ grupę \(\mathbb{Z}^{*}_{a^n-1}\).
  </p>
</p>

<div>
  <h4 class="collapsible"><a href="https://math.stackexchange.com/a/398227/237591">Rozwiązanie (link)</a></h4>
</div>
---
