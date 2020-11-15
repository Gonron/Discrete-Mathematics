### 1 Logic
Explain sentences: negation (not), conjunction (and), and disjunction (or), tautologies and contradictions
Explain truth tables
Present some laws of logical equivalence including De Morgan’s law
Explain conditional statements, their contrapositive, converse, and inverse, hypothesis and conclusion
Explain arguments, modus ponens and modus tollens

- **Sentences**
    - Negation
    - Conjunction
    - Disjunction
    - **t**autologies
    - **c**ontradictions
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
Define predicates and their truth sets
Explain the universal and existential quantifiers
Present some arguments with quantified statements
Present some laws of multi-quantified statements including De Morgan’s law

- **Predicate**
    - *Set-Roster notation* - Domain $D = {1, 2, \dots, 8, 9}$
    - Set-Builder notation $\{x ∈ D | x ≤ 5\}$
    - Truth sets ${1, 2, 3, 4, 5}$
- **Quantifiers**
    - Universal $∀x ∈ D, P(x)$ 
    - Existential $∃x ∈ E, Q(x)$
- **Universal Conditional statements** $∀x, P(x) → Q(x) ≡ P(x) ⇒ Q(x)$
- **Arguments**
    - Modus Ponens (method of affirming)
    - Modus Tollens (method of denying)
    - Converse / Inverse
- **Multi-Quantified statements** 
    - $∃x∈D,∀y∈E, P(x, y)$
    - $∀x ∈ D, ∃y ∈ E, P(x, y)$ 
- **Laws of Multi-Quantified statements** 
    - De Morgan's $¬(∀x∈D,∃y∈E, P(x, y))$

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
        - Sequences has a start
        - Sequences has a succ function      
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
    - $\text{is } 3^n-1 = \text{a multiple by }2$
        - $3^1-1 = 2 = \text{true}$
        - $3^k-1 = \text{true}$
        - $3^{k+1}-1 =3\times 3^k -1$
        - $2\times3^k + 1\times 3^k-1$
        - $2\times 3^k \text{ is a multiple of 2}$
        - $3^k-1 \text{ is true}$
    - [show](https://www.mathsisfun.com/algebra/mathematical-induction.html)
- **Recursion**
    - Show Factorials

### 4 Regular Expressions and Finite-state Automata
Distinguish languages types according to Chomsky
Define “alphabet”, “string”, and “language”
What is the Kleene closure of a language?
How are regular expressions defined?
Explain the parts of a finite-state automaton
Define the eventual-state function
Explain the relation between regular languages and languages accepted by a finite-state automaton

- **Chomsky**
    - **Type-0** Turning-complete languages  
        - *Turing machine*
    - **Type-1** Context-sensitive languages
        - *Linear bounded automaton*
        - English \ Danish
    - **Type-2** Context-free languages
        - *Push-down automaton*
    - **Type-3** Regular languages
        - *Finite-state automaton*
        - Regular Expressions
- **Formal languages**
    - Alphabet $Σ$ *finite*
        - $\Sigma = \{a,b,c,d\}$
    - String over $Σ$ *finite*
        - $\epsilon, a, aa, aaa, abc \text{ or } abbcca \dots$
    - Language L over $Σ$
        - $\{ab, cd\}$
- **Combining languages**
    - Concatenation $LL' = \{xy | x ∈ L ∧ y∈ L'\}$
    - Union $L ∪ L' = \{x | x ∈ L ∨ x ∈ L'\}$
    - Klenee closure $L^∗ = \{x|\text{ is a concatenation of strings in }L\}$
- **Regular Expression**
    - Terminals $\emptyset, \epsilon, x | x \isin \Sigma $
    - Non-Terminals $(rs), (r|s), (r^*)$
- **Finite-state automaton**
    - Input Alphabet
    - States
        - Initial state $s_0$
        - Accepting state $F$
    - Next-state function 
        - $N : S × Σ → S$
        - $N(s,char)$
- **Eventual-state function**
    - $N^*: S × Σ^* → S$
    - $N^*(s,word)$
- **Draw A(B|CD)\*E**
    - It's deterministic
- **Languages accepted by an automaton**
    - $\text{RegEx} \Longleftrightarrow \text{finite-state automata}$ 
     

### 5 Set Theory
Define a set
How can an ordered pair be defined using sets only?
Explain the Cartesian product
Define a relation and a function, what is the empty set and a powerset
Define subsets and set equality
Present some laws on sets

- **Notation**
    - Set-roster notation $A= \{1,2,3\} \quad B = \{10,11,12, \dots ,119\}$
    - Set-builder notation $A=\{x∈\mathbb{Z} |−2< x <7\}$
    - The empty set $\emptyset = \{\}$
    - Powerset $\mathcal{P}(\{a,b,c\}) = \{\emptyset,\{a\},\{b\},\{c\},\{a, b\},\{b, c\},\{a, c\},\{a, b, c\}\}$
- **Ordered Pair** $(a,b,c)=\{\{a\},\{a,b\}\{a,b,c\}\}$
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
- **Relation** $xRy$
    - *draw two circles with (1,2,5), (3,6,0)*
    - $R⊆\{(x, y)∈A×B\}$
    - Inverse $R^{−1}=\{(y, x)∈B×A|(x, y)∈R\}$
- **Function** $x^2$
    - *draw two circles with (1,2,3)(1,4,9)*
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
    - Reflectivity $∀x∈\mathbb{R}, x R x$
    - Symmetry $∀x, y∈\mathbb{R}, x R y→y R x$
    - Transitivity $∀x, y, z∈\mathbb{R}, x R y∧y R z→x R z$
- **Relation defined by partition** $x R y \Longleftrightarrow ∃Ai, x∈Ai∧y∈Ai$
    - Reflective $xRx$ ... $Ai, x∈Ai∧x∈Ai$ 
    - Symetric $xRy→yRx$ ... $∃Ai, x∈Ai∧y∈A$
    - Transitive $xRy∧yRz→xRz$ ... 
        - $∃Ai, x∈Ai∧y∈Ai \text{ by definition of } x R y  $
        - $∃Aj, y∈Aj∧z∈Aj \text{ by definition of } y R z$
- **Antisymmetry**
    - Symetric $x R y→y R x$
    - Antisymmetric $∀a, b∈A, a R b∧b R a→a=b$
        - *use two nodes 1 = 1*
    - Not Antisymmetric $∃a, b∈A, a R b∧b R a∧a \neq b$
        - *use two nodes 2 modulo 4*
- **Partial ordering**
    - Maximum $∀b∈A, b \preceq a∨b\npreceq a$
    - Greatest $∀b∈A, b\preceq a$
    - Minimum $∀b∈A, a\preceq b∨a\npreceq b$
    - Least $∀b∈A, a\preceq b$
    - *draw hasse-diagram* $\mathcal{P}(\{a,b,c\})$

### 7 - Explain static analysis and Hoare Logic in general
Explain static analysis and Hoare Logic in general
Explain the ideas behind design by contract
Present the general content of design by contract code
Explain what Sound and Complete analysis are
In general terms, explain the process of static analysis

- **Static analysis**
    - Soundness: A static analysis is said to be sound if it rejects all faulty programs.
    - Completeness: A static analysis is said to be complete if all correct programs passes.
    - Process 
        - Pre- and Post-conditions
        - "Run" code and update state
        - Compare state with postcondition
        - $S \preceq Q$ *if* $Q$ *covers all possible states* $S$*, analysis succeeded*
- **Hoare Logic**
    - Hoare tripple $\{P\}C\{Q\}$
    - Skip commands $\{P\}\text{skip}\{P\}$
    - Command composition $\begin{matrix} \{ P \} S \{ Q \}, \{ Q \} T \{ R \}\\ \{ P \} S;T \{ R \} \end{matrix}$ 
    - Selection $\begin{matrix} \{ B \land P \} S \{ Q \}, \{ \neg B \land P \} T \{ Q \}\\ \{ P \} if \: B \: then \: S \: else \: T \: endif \{ Q \} \end{matrix}$
    - Iteration $\begin{matrix} \{ B \land P \} S \{ P \}\\ \{ P \} while \: B \: do \: S \: done \{ \neg B \land P \} \end{matrix}$
- **Design by contract**
    - Idea
        - What does contract expect?
        - What does contract guarantee?
        - What does contract maintain?
    - Content
        - Input values and types
        - Return values and types
        - Error/Exception condition values and types
        - Side effects
        - Pre- and Post-conditions
        - invariants