def reverseTheRange(array, start, stop):
    if not array:
        return 0

    length = len(array)

    i = start
    j = stop

    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return array


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    B = int(input())
    C = int(input())
    print(reverseTheRange(array, B, C))
