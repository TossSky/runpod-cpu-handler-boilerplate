def run(input_data):
    a = input_data.get("a")
    b = input_data.get("b")
    operation = input_data.get("op")
    # Hi
    if a is None or b is None or operation not in {"add", "sub", "mul", "div"}:
        return {"error": "Missing or invalid input"}

    print("test run log")

    result = {
        "add": a + b,
        "sub": b - a,
        "mul": a * b,
        "div": a / b if b != 0 else "inf"
    }[operation]

    return result
