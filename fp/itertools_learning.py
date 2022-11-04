# %%
import itertools as it

# %%
# it?
# dir(it)
# %%
# --------------------> DON'T RUN IT  <--------------
# print(list(it.count(10, 2)))
# %%
list(it.accumulate(range(10), lambda x, y: x + y, initial=0))
# %%

list(it.accumulate(range(10), lambda x, y: x + y, initial=1))
# %%

list(it.accumulate(range(10), lambda x, y: x + y))
# %%
list(it.chain('ABC', 'DEF'))

# %%
list(it.chain(range(10), range(10)))
# %%
list(zip(range(10), range(10)))
# %%
# lst = []
# for a, b in (range(10), range(10)):
#     lst.append((a, b))
# print(lst)
# %%
list(it.combinations("ABCD", 3))
# %%
list(it.combinations(range(4), 3))
# %%
list(it.combinations('ABCD', 2))
# %%
list(it.product('ABCD', repeat=2))
# %%
list(it.product('ABCD', repeat=3))
# %%
