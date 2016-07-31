% Including mutation testing as part of a continuous integration workflow
% Tim Waterson

# What is mutation testing?

---

If our application code breaks, will our tests detect that?

---

``` {.python}
def flip(char):
  codepoint = ord(char)

  if 64 < codepoint < 91:
    return chr(codepoint + 32)

  if 96 < codepoint < 123:
    return chr(codepoint - 32)

  return char
```

---

* `'a'` → `'A'`
* `'z'` → `'Z'`
* `'1'` → `'1'`
* `'Z'` → `'z'`
* `'A'` → `'a'`
* `'+'` → `'+'`

---

![The ROR mutation operator. Image is an extract from *Operators for Mutation Testing of Python Programs*, a 2014 paper by Derezinska and Halas.](images/ror.png)

---

``` {.python}
def flip(char):
  codepoint = ord(char)

  if 64 < codepoint <= 91:
    return chr(codepoint + 32)

  if 96 < codepoint < 123:
    return chr(codepoint - 32)

  return char
```

---

All our tests still pass...

* `'a'` → `'A'`
* `'z'` → `'Z'`
* `'1'` → `'1'`
* `'Z'` → `'z'`
* `'A'` → `'a'`
* `'+'` → `'+'`

...however we now have an erroneous result.

* `'['` → `'{'`

---

![Mutation testing output from MutPy](images/mutpy.png)

# What is continuous integration?

---

Every time the code changes, build the system and check its quality.

---

![One way to show the CI build status](images/lava-lamps.png)

---

![Travis CI in action on a GitHub project](images/travis.png)

---

![A failed build in the Jenkins console](images/jenkins.png)

# What are the benefits arising from bringing mutation testing and continuous integration together?

# What are the challenges in running mutation testing in a continuous integration environment?

## Speed

## Reporting

# What's my project doing to address those challenges?

---

![The mutiny website](images/mutiny.png)

---

![multimutiny, the main codebase for my project](images/multimutiny.png)

---

![mm-benchmark, a tool for comparing multimutiny and mutiny performance across different-sized codebases and different numbers of parallel processes](images/mm-benchmark.png)

# Any questions?
