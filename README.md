Project Euler
=============

My solutions to Project Euler problems. Requires Python 3.5.

From the root directory, solutions can be run as follows:

```
$ python3
>>> from euler.solutions.solution_1 import sum_multiples
>>> sum_multiples(10, 3, 5)
23
```

This repository includes a utility which can be used to time the execution of a function. Use it as follows (continuing from above):

```
>>> from euler.utilities.timed_execution import timed_execution
>>> timed_execution(sum_multiples, 10, 3, 5)
Solution: 23
Seconds to execute 1000 times: 0.00796254602028057
```
