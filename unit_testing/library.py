import logging as log

FORMAT = '%(asctime)s --> %(module)s --> %(lineno)d --> %(message)s'
log.basicConfig(level=log.INFO, encoding='utf-8', filename="lib.log", filemode='a', format=FORMAT)


class MathOps:
    def __init__(self, logger):
        self.logger = logger

    def add(self, a: int, b: int) -> int:
        self.logger.info(f"{a=}, {b=}")
        result = a + b
        self.logger.info(f"{result=}")
        return result

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        if b != 0:
            return a / b
        else:
            raise ValueError("Deviser must be non-zero")


# debug, info, warnings, errors, critical
