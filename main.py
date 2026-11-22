from collections import Counter
import heapq

def huffman_roundtrip(data):
    heap = [[wt, [ch, ""]] for ch, wt in Counter(data).items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = "0" + pair[1]
        for pair in hi[1:]: pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    codes = dict(heap[0][1:])
    rev = {v: k for k, v in codes.items()}
    bits = "".join(codes[c] for c in data)
    out, cur = [], ""
    for b in bits:
        cur += b
        if cur in rev: out.append(rev[cur]); cur = ""
    return "".join(out)

if __name__ == "__main__":
    assert huffman_roundtrip("abracadabra") == "abracadabra"
    print("[PASS] 056_huffman_compressor")
