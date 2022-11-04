# %%
from library import MathOps
import logging

# %%
logger = logging.getLogger(__name__)
math_ops = MathOps(logger)
math_ops.add(2, 4)

logger.warning("This module may fail")
# %%
