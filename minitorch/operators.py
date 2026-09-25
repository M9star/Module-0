"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


def mul(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def id(x: float) -> float:
    """Identity function."""
    return x


def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def neg(x: float) -> float:
    """Negate a number."""
    return -x


def lt(x: float, y: float) -> float:
    """Return 1.0 when x is less than y, else return 0.0."""
    return 1.0 if x < y else 0.0


def eq(x: float, y: float) -> float:
    """Return 1.0 when x is equal to y, else return 0.0."""
    return 1.0 if x == y else 0.0


def max(x: float, y: float) -> float:
    """Return the maximum of two numbers."""
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    """Check whether the inputs differ by less than 0.01."""
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    """Compute sigmoid without overflowing the exponential."""
    if x >= 0:
        value = 1.0 / (1.0 + math.exp(-x))
        return value if value < 1.0 else math.nextafter(1.0, 0.0)
    exp_x = math.exp(x)
    return exp_x / (1.0 + exp_x)


def relu(x: float) -> float:
    """Return the positive part of x."""
    return x if x > 0 else 0.0


def log(x: float) -> float:
    """Compute the natural logarithm of x."""
    return math.log(x)


def exp(x: float) -> float:
    """Compute the exponential of x."""
    return math.exp(x)


def inv(x: float) -> float:
    """Compute the reciprocal."""
    return 1.0 / x


def log_back(x: float, d: float) -> float:
    """Multiply the incoming derivative by the derivative of the log function."""
    return d / x


def inv_back(x: float, d: float) -> float:
    """Multiply the incoming derivative by the reciprocal derivative."""
    return -d / (x * x)


def relu_back(x: float, d: float) -> float:
    """Multiply the incoming derivative through positive inputs."""
    return d if x > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists



# TODO: Implement for Task 0.3.


def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: Function from one value to one value.

    Returns:
        A function that takes a list, applies `fn` to each element, and returns a
         new list
    """
    raise NotImplementedError("Need to include this file from past assignment.")


def negList(ls: Iterable[float]) -> Iterable[float]:
    "Use `map` and `neg` to negate each element in `ls`"
    raise NotImplementedError("Need to include this file from past assignment.")


def zipWith(
    fn: Callable[[float, float], float]
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: combine two values

    Returns:
        Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.

    """
    raise NotImplementedError("Need to include this file from past assignment.")


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    "Add the elements of `ls1` and `ls2` using `zipWith` and `add`"
    raise NotImplementedError("Need to include this file from past assignment.")


def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""
    Higher-order reduce.

    Args:
        fn: combine two values
        start: start value $x_0$

    Returns:
        Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`
    """
    raise NotImplementedError("Need to include this file from past assignment.")


def sum(ls: Iterable[float]) -> float:
    "Sum up a list using `reduce` and `add`."
    raise NotImplementedError("Need to include this file from past assignment.")


def prod(ls: Iterable[float]) -> float:
    "Product of a list using `reduce` and `mul`."
    raise NotImplementedError("Need to include this file from past assignment.")