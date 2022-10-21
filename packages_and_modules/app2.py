# %%

import library as l
import newlibrary as nl


# %%
def aggregator(mod, action: str, a: int, b: int) -> int | None:
    action = action.lower()
    if action == 'add':
        return mod.add(a, b)
    elif action == 'sub':
        return mod.sub(a, b)
    elif action == 'mul':
        return mod.mul(a, b)
    elif action == 'div':
        return mod.div(a, b)
    else:
        print(f"Unknown action:{action}")
# %%
aggregator(l, 'add', 2, 3)
# %%
aggregator(nl, 'add', 2, 3)
# %%
