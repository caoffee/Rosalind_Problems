from collections import deque #double-ended queue

def reversal_distance(p, q):
    p, q = tuple(p), tuple(q)
    if p == q:
        return 0

    front, back = {p: 0}, {q: 0}
    queue_front, queue_back = deque([p]), deque([q])

    while queue_front and queue_back:
        if len(queue_front) <= len(queue_back):
            curr_queue, curr_visited, other_visited = queue_front, front, back
        else:
            curr_queue, curr_visited, other_visited = queue_back, back, front
        for _ in range(len(curr_queue)):
            curr = curr_queue.popleft()
            dist = curr_visited[curr]

            for i in range(len(curr)):
                for j in range( i + 1, len(curr)):
                    new_perm = curr[:i] + curr[i:j+1][::-1] + curr[j+1:]
                    if new_perm in other_visited:
                        return dist + 1 + other_visited[new_perm]
                    if new_perm not in curr_visited:
                        curr_visited[new_perm] = dist + 1
                        curr_queue.append(new_perm)
    return -1

with open('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_rear.txt') as file:
    lines = [line.strip() for line in file if line.strip()]  # remove blank lines

# Each case = 2 lines: p then q
for i in range(0, len(lines), 2):
    p = list(map(int, lines[i].split()))
    q = list(map(int, lines[i + 1].split()))
    print(reversal_distance(p, q))
