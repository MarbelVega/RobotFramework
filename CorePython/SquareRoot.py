def sqrt(n):
    if n <= 1:
        return n

    start = 0
    end = n

    while start <= end:
        mid = (end + start) / 2
        if mid * mid == n:
            return mid

        if mid * mid > n:
            end = mid - 1
        else:
            start = mid + 1

    return mid


n = 500
print(sqrt(n))
