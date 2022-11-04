# %%
import functools as ft
import sys

# %%


@ft.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


# %%
factorial(5)
# %%
factorial(10)
# %%
factorial(100)
# %%
factorial(1000)
# %%
# factorial(5000)
# %%
print(sys.getrecursionlimit())
# %%
factorial(1000)
# %%
sys.setrecursionlimit(5000)
# %%
len(str(factorial(3000)))
# %%
ft.partial