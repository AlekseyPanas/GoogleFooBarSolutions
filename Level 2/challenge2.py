def solution(arr):
    queue = [arr]

    prev_length = 0
    sums = []

    while queue:
        current = queue[0][:]
        queue.pop(0)

        if len(current) != prev_length and len(sums):
            return max(sums)
        prev_length = len(current)

        if sum(current) % 3 == 0:
            divisble_thing = "".join([str(x) for x in list(sorted(current, reverse=True))])
            if divisble_thing:
              sums.append(int(divisble_thing))

        for itm in current:
            copy = current[:]
            copy.remove(itm)
            queue.append(copy)

    if len(sums):
      return max(sums)
    else:
      return 0


print(solution([3, 1, 4, 1, 5, 9]))
