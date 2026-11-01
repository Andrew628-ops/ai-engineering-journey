def normalize_vector(v):
    total = 0
    final_result = []
    for row in v:
        total = total + row ** 2
    result = total ** 0.5
    if result == 0:
            raise ValueError("magnitude cannot be zero")
    for r in v:
        final_result.append(r/result)
    return final_result