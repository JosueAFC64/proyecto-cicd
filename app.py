class DivisionPorCeroError(Exception):
    """Se lanza cuando se intenta dividir entre cero."""
    pass


def dividir(dividendo: float, divisor: float) -> float:
    if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Ambos argumentos deben ser numéricos")

    if isinstance(dividendo, bool) or isinstance(divisor, bool):
        raise TypeError("Ambos argumentos deben ser numéricos")

    if divisor == 0:
        raise DivisionPorCeroError("No se puede dividir entre cero")

    return dividendo / divisor


def main():
    ejemplos = [(10, 2), (7, 3), (5, 0)]
    for a, b in ejemplos:
        try:
            resultado = dividir(a, b)
            print(f"{a} / {b} = {resultado:.4f}")
        except DivisionPorCeroError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
