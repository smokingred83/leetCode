from queue import PriorityQueue


def topKFrequent(nums: [int], k: int) -> [int]:
    queue = PriorityQueue(k)
    freqs = {}
    for n in nums:
        freq = freqs.get(n, 0) + 1
        freqs[n] = freq
    for n, freq in freqs.items():
        if queue.full():
            lowest_freq, _ = queue.queue[0]
            if freq > lowest_freq:
                queue.get()
                queue.put((freq, n))
        else:
            queue.put((freq, n))
    return [n for _, n in queue.queue]


if __name__ == "__main__":
    res = topKFrequent([1,1,1,2,2,3], 2)
    res