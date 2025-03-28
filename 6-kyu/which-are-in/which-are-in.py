def in_array(array1, array2):
    return sorted({s for s in array1 if any(s in t for t in array2)})