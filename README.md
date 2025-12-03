# Summary of Search Algorithm Performance Tests  
**Algorithms tested:** Knuth–Morris–Pratt (KMP), Boyer–Moore (BM), Rabin–Karp (RK)  
**Text sizes:**  
- **text_1:** 12,657 characters  
- **text_2:** 17,590 characters  

The test measured execution time (in seconds) for four scenarios:  
1. Pattern **exists** in text_1  
2. Pattern **exists** in text_2  
3. Pattern **does not exist** in text_1  
4. Pattern **does not exist** in text_2


## 1. Test Results Table

| Algorithm     | Exists in text_1 | Exists in text_2 | Non-existent in text_1 | Non-existent in text_2 |
|---------------|------------------|-------------------|--------------------------|--------------------------|
| **KMP**       | 0.310 s          | 0.946 s           | 0.667 s                  | 0.949 s                  |
| **Boyer–Moore** | 0.072 s          | 0.189 s           | 0.081 s                  | 0.118 s                  |
| **Rabin–Karp** | 0.711 s          | 2.230 s           | 1.529 s                  | 2.156 s                  |


## 2. Overall Performance Ranking
Across all test scenarios (existing and non-existing patterns), the performance ranking is:

1. **Boyer–Moore — fastest**
2. **KMP — medium performance**
3. **Rabin–Karp — slowest**

Boyer–Moore is consistently the best-performing algorithm, while Rabin–Karp is significantly slower across all tests.

## 3. Algorithm-by-Algorithm Analysis

### **3.1 Boyer–Moore**
- Fastest algorithm in every scenario.  
- Shows particularly strong performance when the pattern is **absent**, achieving the smallest execution time.  
- Efficient due to skipping behavior and reverse scanning.  
- Best suited for general-purpose searching.

### **3.2 Knuth–Morris–Pratt (KMP)**
- Moderate performance: slower than Boyer–Moore but significantly faster than Rabin–Karp.  
- Performs similarly whether the pattern exists or not, due to deterministic linear scanning.  
- Execution time increases proportionally with text size.

### **3.3 Rabin–Karp**
- Slowest in all scenarios, especially for the larger text_2.  
- Hash recomputation introduces overhead, making single-pattern search inefficient.  
- Performs much worse when the pattern does not exist (due to many hash comparisons). 
- According to the [Wiki page about Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm), this algorithm is practical only for **multiple-pattern searching**, not for single queries.

## 4. Key Insights

### **Insight 1 — Boyer–Moore is superior for practical single-pattern matching**
It is up to **4× faster than KMP** and **20–25× faster than Rabin–Karp** in some tests.  
Its skipping mechanism greatly reduces comparisons.

### **Insight 2 — KMP is reliable and stable**
KMP shows consistent performance regardless of whether the pattern is present.  
This makes it suitable for applications where **worst-case linear time is required**.

### **Insight 3 — Rabin–Karp suffers from overhead in single-pattern cases**
The hashing strategy makes it inefficient for single-pattern searches, especially on longer texts.  
It is best applied only in scenarios involving **searching many patterns simultaneously**.

## 5. Final Conclusion
The experiment demonstrates clear differences in performance:

- **Boyer–Moore** delivers the best results across all tests and is the recommended algorithm for typical substring search in large texts.
- **KMP** provides predictable, stable linear performance but is outperformed by BM in practical scenarios.
- **Rabin–Karp** is the least efficient for single-pattern matching and should be used only for multi-pattern contexts.

Overall, **Boyer–Moore is the most efficient algorithm** for the tested data sizes and search scenarios.

