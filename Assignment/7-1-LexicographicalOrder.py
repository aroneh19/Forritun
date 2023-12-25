def precedes(first: str, second: str) -> str:
    if first.lower() < second.lower():
        return first
    return second