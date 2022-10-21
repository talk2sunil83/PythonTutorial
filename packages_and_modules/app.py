# %%
from proto import module
import library
from library import add

# Syntactically, both are correct, but there is cost associated with them
#  1. Whole file is read and all the objects are kept in memory
#  2. Whole file is read but Only specific objects and their dependence will be in memory
# %%
library.add(2, 3)
# %%
add(5, 7)
# %%
# aliasing the objects
import library as l
# %%
from library import add as new_add
# %%
new_add(3, 5)
# %%
a = 5
# %%
type(a)
# %%
a: int = 5
# %%

