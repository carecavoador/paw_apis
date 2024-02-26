import random


def jogo_simples() -> list[int]:
    """Retorna um jogo simples com 6 dezenas."""
    return sorted(random.sample(range(1, 61), k=6))
