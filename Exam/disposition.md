### 1 Logic

- **Sentences**
    - negation
    - conjunction
    - disjunction
    - **t**autologies
    - **c**ontradictions
- **Truth tables (maybe skip this)**
- **Laws of Equivalence** 
    - Commutative  $a ∧ b ≡ b ∧ a$
    - Associatitve $(a ∧ b) ∧ c ≡ a ∧ (b ∧ c)$
    - Distributive $a ∧ (b ∨ c) ≡ (a ∧ b) ∨ (a ∧ c)$
    - De Morgan's $¬(a ∧ b) ≡ ¬a ∨ ¬b$
- **Proof of De Morgan's with truth table**
- **Conditional statements** $a→b≡¬a∨b$
    - **if** *hypothesis* **then** *conclusion*
    - Converse $b → a$
    - Inverse $¬a → ¬b$
    - Contrapositive $a → b ≡ ¬b → ¬a$
- **Biconditonal statements** $a ↔ b$
    - $a \leftrightarrow b≡ b \leftrightarrow a$
- **Arguments**
    - Modus Ponens (method of affirming)
    - Modus Tollens (method of denying)

### 2 Predicates and Quantified statements

- **Predicate**
    - Domain $D = {1, 2, \dots, 8, 9}$
    - Set-Builder notation $\{x ∈ D | x ≤ 5\}$
    - Truth sets ${1, 2, 3, 4, 5}$
- **Quantifiers**
    - Universal $∀x ∈ D, P(x)$ 
    - Existential $∃x ∈ E, Q(x)$
- **Universal Conditional statements** $∀x, P(x) → Q(x) ≡ P(x) ⇒ Q(x)$
- **Arguments**
    - Modus Ponens (method of affirming)
    - Modus Tollens (method of denying)
    - Errors
- **Multi-Quantified statements** 
    - $∃x∈D,∀y∈E, P(x, y)$
    - $∀x ∈ D, ∃y ∈ E, P(x, y)$ 
- **Laws of Multi-Quantified statements** 
    - De Morgan's

### 3 Sequences, Induction and Recursion
Define a sequence
Explain summations and telescopic sums
Explain products and theorems for working with sums and products
Explain factorials and combinations
Describe the induction principles
Explain recursion


- **Sequence**
    - Definition $D:f(x)=\text{result}$
    - Properties
- **Summations** 
    - $\sum\limits_{k=m}^n a_k$
    - $a_m + a_{m+1} + a_{m+2} + \dots + a_n$
- **Telescopic**
    - $\sum\limits_{k=1}^n \frac{1}{k(k+1)} = \frac{1}{1} - \frac{1}{n+1}$
- **Product**
    - $\prod\limits_{k=m}^n a_k$
    - $a_m \cdot a_{m+1} \cdot a_{m+2} \cdot \dots \cdot a_n$
- **Adding and removing a final term**
    - $\sum\limits_{k=0}^n 2^k + 2^{n+1} = \sum\limits_{k=0}^{n+1} 2^k$
    - $\sum\limits_{k=1}^n \frac{1}{k^2}=\sum\limits_{k=1}^{n-1} \frac{1}{k^2} + \frac{1}{n^2}$
    - $\prod\limits_{k=0}^n 2^k \cdot 2^{n+1} = \prod\limits_{k=0}^{n+1} 2^k$
    - $\prod\limits_{k=1}^n k = \prod\limits_{k=0}^{n-1} k \cdot n$
- **Theorems**
    - $\sum\limits_{k=m}^{n} a_k + \sum\limits_{k=m}^{n} b_k = \sum\limits_{k=m}^{n} (a_k + b_k) $
    - $ c \cdot \sum\limits_{k=m}^{n} a_k = \sum\limits_{k=m}^{n} c \cdot a_k$
    - $\prod\limits_{k=m}^{n} a_k \cdot \prod\limits_{k=m}^{n} b_k = \prod\limits_{k=m}^{n} a_k \cdot b_k$
- **Factorials** $n! = k \cdot (k-1)!$
- **Combinations** $\binom{n}{r}=\frac{n!}{r!(n-r)!}$
- **Induction**
    - Hypothesis
    - Base
    - Consequense
    - Proof
- **Recursion**


### 4 Regular Expressions and Finite-state Automata

- **Chomsky**
- **Formal languages**
    - Alphabet $Σ$
    - String over $Σ$
    - Language L over $Σ$
- **Combining languages**
    - Concatenation $LL' = {xy | x ∈ L ∧ y∈ L'}$
    - Union $L ∪ L' = \{x | x ∈ L ∨ x ∈ L'\}$
    - Klenee closure $L^∗ = \{x|\text{ is a concatenation of strings in }L\}$
- **Regular Expression**
    - Terminals $\emptyset, \epsilon, x | x \isin \Sigma $
    - Non-Terminals $(rs), (r|s), (r^*)$
- **Finite-state automaton**
    - Input
    - States
        - Initial state $s_0$
        - Accepting state $F$
    - Next-state function 
        - $N : S × Σ → S$
        - $N(s,m)$
- **Draw A(B|CD)\*E**
    - It's deterministic
- **Eventual-state function**
    - $N^*: S × Σ^* → S$
    - $N^*(s,w)$
- **Languages accepted by an automaton**
     

### 5 Set Theory
- **Notation**
    - Set-roster notation $A= \{1,2,3\} \quad B = \{10,11,12, \dots ,119\}$
    - Set-builder notation $M = \{x ∈ S | P(x)\}$
    - The empty set $\emptyset = \{\}$
    - Powerset $\mathcal{P}(\{a,b,c\}) = \{\emptyset,{a},{b},{c},{a, b},{b, c},{a, c},{a, b, c}\}$
- **Ordered Pair** $(a,b)=\{\{a\},\{a,b\}\}$
- **Cartesian product** $A×B=\{(a, b)|a∈A∧b∈B\}$
    - More sets $A×B×C=\{(a, b, c)|a∈A∧b∈B∧c∈C\}$
- **Operations**
    - Membership $e ∈ M$
    - Intersection $A \cap B$
    - Union $A ∪ B$
    - Difference $A − B = A \cap B^c$
    - Complement $A^c$ 
- **Subset** $A ⊆ B \Longleftrightarrow ∀x∈A, x∈B$
    - Not a subset $A \nsubseteq B \Longleftrightarrow ∃x∈A, x \not\in B $
    - Proper subset $A⊂B \Longleftrightarrow ∀x∈A, x∈B∧∃x∈B, x \not\in A$
    - Equality $A=B  \Longleftrightarrow A⊆B∧B⊆A$
    - Transitivity $A⊆B∧B⊆C→A⊆C$
- **Disjoint sets** $A∩B=∅$
    - Partitions $\{A_1, A_2, A_3, \dots, A_n\} \text{ of set } A $
    - $A = \bigcup\limits_{i=1}^{n} A_{i}$
    - $∀a, b∈\{1,2,3, \dots, n\}, Aa∩Ab=\emptyset∨a=b$
- **Laws**
    - Commutative $A∩B = B∩A$
    - Associative $(A∩B)∩C = A∩(B∩C)$
    - Distribution $A∪(B∩C) = (A∪B) ∩(A∪C)$
    - De Morgan $(A∪B)^{c} = A^{c}∩B^{c}$ 
- **Relation** $R⊆\{(x, y)∈A×B\}$
    - Inverse $R^{−1}=\{(y, x)∈B×A|(x, y)∈R\}$
- **Function**
    - $∀x∈A,∃y∈B,(x, y)∈F$
    - $∀x∈A∧y∈B∧z∈B,((x, y)∈F∧(x, z)∈F)→y=z$

### 6 Relations
Define a relation on a set
Explain reflectivity, symmetry, and transitivity
What is the relation defined by a partition?
Explain antisymmetry and partial ordering of sets

- **Definition**
    - When $R$ is a relation $xRy$
    - $R⊆\{(x, y)∈A×B\}$
    - $R^{−1}=\{(y, x)∈B×A|(x, y)∈R\}$
- **Properties**
    - Reflectivity $∀x∈A,(x, x)∈R$
    - Symmetry $∀x, y∈A,(x, y)∈R→(y, x)∈R$
    - Transitivity $∀x, y, z∈A,(x, y)∈R∧(y, z)∈R→(x, z)∈R$
- **Proof properties?** <TODO change title>
- **Relation defined by partition** <TODO change title>
    - Reflective
    - Symetric
    - Transitive
- **Antisymmetry**
    - Symetric $x R y→y R x$
    - Antisymmetric $∀a, b∈A, a R b∧b R a→a=b$
    - Not Antisymmetric $∃a, b∈A, a R b∧b R a∧a=b$
- **Partial ordering**