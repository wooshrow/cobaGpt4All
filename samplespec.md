#### Program:

    def maxp(x: float, y: float) -> float:
    """
    The program takes x and y that are non-negative, and it returns the greatest of x and y.

    >>> maxp(0,0)
    0
    >>> maxp(9,1)
    1
    >>> maxp(9,10)
    10
    """
    return max(x,y)

#### Pre-cond:
x and y are non-negative.

#### Post-cond:
The program returns the greatest of x and y.

#### Prompt for pre-cond:
(defining the problem as code completion request to the AI)

    def checkPre(x: float, y: float) -> bool:
    """
    Return true if x and y are non-negative.
    """

**Solution:**
    return x>=0 and y>=0

#### Prompt2 post-cond:
(again, defining the problem as code completion)

    def checkPost(retval: float, x: float, y: float) -> bool:
    """
    Return true if retval is the greatest of x and y.
    """

**Solution:**
   return (retval==x or retval==y) and retval >=x and retval >= y

#### Test:

    invalidInputdata = [(-1,0),(0,-1),(-1,-1)]
    validTestdata    = [(0,0),(9,1),(9,10)]

#### Mutants:

    def maxInvalid1(x,y): ...
    def maxInvalid2(x,y): ...

    mutants = [maxInvalid1,maxInvalid2]

#### Evaluation:

```
# Evaluating the correctness of the proposed pre-cond:
def checkPre(x,y): ...
def checkPost(retval,x,y):...

correctlyClassifiedByPrecond  = len([v for v in invalidInputdata if not (checkPre(v[0],v[1]))]) + len([v for v in validTestdata if checkPre(v[0],v[1])])
numberOfPrecondDataSamples = len(invalidInputdata) + len(validTestdata)

# Evaluating the soundness of the proposed post-cond:
numberOfPostCondDataSamples = len(validTestdata)
numberOfAcceptedByPostCond = len([v for v in validTestdata if checkPost(maxp(v[0],v[1]),v[0],v[1])])

# Evaluating the completeness of the proposed post-cond:

numberOfMutants = len(mutants)
numberOfMutantsKilled = 0
for M in mutants:
   for v in testdata:
      if not checkPost(M(v[0],v[1]),v[0],v[1]):
         numberOfMutantsKilled += 1
         break

return ((correctlyClassifiedByPrecond,numberOfPrecondDataSamples),
  (numberOfAcceptedByPostCond,numberOfPostCondDataSamples),
  (numberOfMutantsKilled,numberOfMutants))
```
