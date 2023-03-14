# Boolean-Algebra

Given an expression of boolean algebra, computes all combinations of values that make the expression evaluate to True.

This was partly to practice parsing and postfix/infix stuff, but mostly because boolean algebra is really cool.

Form expressions using letters (in alphabetic order), operators (below), and parentheses.

## Operators
 - !: not
   - !a == not a
 - *: and
   - a * b == a and b
   - ab == a and b
   - a(b + c) == a and (b or c)
 - +: or
   - a + b == a or b
 - |: xor
   - a | b == a xor b
   - a | b == (a != b)
 - &: xnor
   - a & b == a xnor b
   - a & b == (a == b)
   
## Example
```python
# input:
(!a + !b)(!a + b)

# output:
[0, 1]
[0, 0]
```
