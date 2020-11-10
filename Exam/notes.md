# Exam
The exam is a 30 minutes oral test with no preparation. The questions are known in advance and covers the curriculum.

The exam date is Monday November 16th

# Questions
## 1.1 Logic
- **Explain sentences: negation (not), conjunction (and), and disjunction (or), tautologies and contradictions**

Negation (not): 

![not](img/not.png)

Conjuntion (and):

![and](img/and.png)

Disjunction (or):

![or](img/or.png)

**T**autologies: Something that's always True `a = a`
**C**ontradictions: Something that can never be True `a ≠ a`

- **Explain truth tables**

![example](img/example.png)

- **Present some laws of logical equivalence including De Morgan’s law**

![laws](img/laws.png)

- **Explain conditional statements, their contrapositive, converse, and inverse, hypothesis and conclusion**

Conditional Statements:

if *hypothesis* then *conclusion*

![Conditional Statements](img/cs.png)

You can also write it like this:

![Conditional Statements as or](img/cs_as_or.png)

Contrapositive: 

The negation of a conditional statement

![Contrapositive](img/cp.png)

Converse:

Is where A and B are swapped in the original conditional statement

![Converse](img/converse.png)

Inverse:

![Inverse](img/inverse.png)

Is the negation of A and B in the original conditional statement

Converse is equivalent to Inverse
Contrapositive is equivalent to the original conditional statement

- **Explain arguments, modus ponens and modus tollens**

Argument

![Socrates](img/argument.png)

Modus Ponens = Method of Affirming:

![Ponens](img/mp.png)

Modus Tollens = Method of Denying:

![Tollens](img/mt.png)

## 1.2 Predicates and Quantified statements
- Define predicates and their truth sets

    - Domain *D = {1, 2, ... 8, 9}*
    - Set-Builder notation *{x ∈ D | x ≤ 5}*
    - Truth sets *{1, 2, 3, 4, 5}*
    
- Explain the universal and existential quantifiers

![Quantifiers](img/uq.png)

- Present some arguments with quantified statements

![Arguments](img/aqs.png)

![Errors](img/eqs.png)

- Present some laws of multi-quantified statements including De Morgan’s law

![De Morgan w/ Quantifiers](img/dmq.png)

## 1.3 Sequences, Induction and Recursion
- Define a sequence

A **sequence** is a function whose **domain** is either all the integers between two given integers or all the integers greater than or equal to a given integer

1 ≤ n ≤ 8 : n2 = 1, 4, 9, . . . 64
Domain : Function = Result
Sequence

In other words, everything on the left of the equation is the sequence, and not the result.

**Propertiese:**

Sequences have a *start*.
Sequences have a *succ* fucntion (next).
The*succ* function is guarateed to reach every value in the sequence, exactly one time.
The sequence has an order.

- Explain summations and telescopic sums

???

- Explain products and theorems for working with sums and products

Adding and removing final term for summation and products
![Adding / Removing final term sum](img/+-termsum.png)

![Adding / Removing final term product](img/+-termprod.png)

Other Theorems

![Theorems](img/theorems.png)

- Explain factorials and combinations

**Factorial:**
5! = 1 * 2 * 3 * 4 * 5

**Combinations**

- Describe the induction principles

????

- Explain recursion

k! = k · (k − 1)!
![Recursion](img/recursion.png)

In other words, we use a prev. term to calculate the current term. see picture above.



## 1.4 Regular Expressions and Finite-state Automata
- Distinguish languages types according to Chomsky

**Type-0** Turning-complete languages  
**Type-1** Context-sensitive languages
**Type-2** Context-free languages
**Type-3** Regular languages 

- Define “alphabet”, “string”, and “language”

Alphabet, is a **finite** set of characters 
*Σ ={f,n,o}*

String, is either a **finite** seqeuene of characters in Σ or the empty (null) string ε
*ε, f, ff, fff, fno, ..., oofno*

Length of string, is the number of characters in the string.
*len(ε) = 0, len('oofno') = 5*

Language *L over Σ* is a set of strings over Σ
*L = {on, off}*
the empty set Ø or {} is a formal language.

- What is the Kleene closure of a language?
- How are regular expressions defined?
- Explain the parts of a finite-state automaton
- Define the eventual-state function
- Explain the relation between regular languages and languages accepted by a finite-state automaton


## 1.5 Set Theory
- Define a set
- How can an ordered pair be defined using sets only?
- Explain the Cartesian product
- Define a relation and a function, what is the empty set and a powerset
- Define subsets and set equality
- Present some laws on sets
## 1.6 Relations
- Define a relation on a set
- Explain reflectivity, symmetry, and transitivity
- What is the relation defined by a partition?
- Explain antisymmetry and partial ordering of sets
## 1.7 Static Analysis
- Explain static analysis and Hoare Logic in general
- Explain the ideas behind design by contract
- Present the general content of design by contract code
- Explain what Sound and Complete analysis are
- In general terms, explain the process of static analysis