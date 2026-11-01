def dot_product(a, b):
    total = 0
    for x, y in zip(a, b):
        total = total + x * y
    return total

def cosine_similarity(a, b): 
    t1 = 0
    t2 = 0
    if len(a) != len(b):
        raise ValueError("length cannot be different")
    for m1, m2 in zip(a, b):
        t1 = t1 + m1 ** 2
        t2 = t2 + m2 ** 2
    result1 = t1 ** 0.5
    result2 = t2 ** 0.5

    if result1 == 0 or result2 == 0:
         raise ValueError("either magnitude cannot be zero")
    
    result = dot_product(a, b)/(result1 * result2)
    return result