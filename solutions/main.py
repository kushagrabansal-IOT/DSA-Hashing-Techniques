# DSA-Hashing-Techniques — Solutions
# Author: Kushagra Bansal — Project Lab India
from collections import defaultdict, Counter

def two_sum(nums, target):
    """Hash complement lookup | O(n) T, O(n) S"""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen: return [seen[target-n], i]
        seen[n] = i
    return []

def two_sum_sorted(nums, target):
    """Two pointer for sorted array | O(n) T, O(1) S"""
    l, r = 0, len(nums)-1
    while l < r:
        s = nums[l]+nums[r]
        if s == target: return [l,r]
        elif s < target: l += 1
        else: r -= 1
    return []

def group_anagrams(strs):
    """Sort key grouping | O(n·k log k) T"""
    d = defaultdict(list)
    for s in strs: d[tuple(sorted(s))].append(s)
    return list(d.values())

def subarray_sum_k(nums, k):
    """Prefix sum + hash | O(n) T, O(n) S"""
    count = prefix = 0
    freq = defaultdict(int); freq[0] = 1
    for x in nums:
        prefix += x
        count += freq[prefix-k]
        freq[prefix] += 1
    return count

def longest_unique_window(s):
    """Sliding window + hash | O(n) T, O(charset) S"""
    seen = {}; l = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l: l = seen[c]+1
        seen[c] = r; best = max(best, r-l+1)
    return best

def top_k_frequent(nums, k):
    """Bucket sort by freq | O(n) T, O(n) S"""
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums)+1)]
    for num, freq in count.items(): buckets[freq].append(num)
    result = []
    for i in range(len(buckets)-1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k: return result[:k]
    return result

def four_sum_count(A, B, C, D):
    """Hash AB sums, lookup -(C+D) | O(n²) T"""
    ab = Counter(a+b for a in A for b in B)
    return sum(ab[-(c+d)] for c in C for d in D)

def longest_consecutive(nums):
    """HashSet for O(1) lookup | O(n) T, O(n) S"""
    s = set(nums); best = 0
    for n in s:
        if n-1 not in s:   # Start of sequence
            cur = n; streak = 1
            while cur+1 in s: cur += 1; streak += 1
            best = max(best, streak)
    return best

class MyHashMap:
    """Chaining HashMap from scratch"""
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
    def _hash(self, key): return key % self.size
    def put(self, key, val):
        bucket = self.table[self._hash(key)]
        for i,(k,v) in enumerate(bucket):
            if k == key: bucket[i] = (key,val); return
        bucket.append((key,val))
    def get(self, key):
        for k,v in self.table[self._hash(key)]:
            if k == key: return v
        return -1
    def remove(self, key):
        h = self._hash(key)
        self.table[h] = [(k,v) for k,v in self.table[h] if k!=key]

if __name__ == "__main__":
    print("="*58)
    print("  DSA Hashing Techniques — Project Lab India")
    print("="*58)
    print(f"  TwoSum([2,7,11,15],9):       {two_sum([2,7,11,15],9)}")
    print(f"  GroupAnagrams count:          {len(group_anagrams(['eat','tea','tan','ate','nat']))}")
    print(f"  SubarraySum([1,1,1],k=2):     {subarray_sum_k([1,1,1],2)}")
    print(f"  LongestUnique('abcabcbb'):    {longest_unique_window('abcabcbb')}")
    print(f"  TopKFreq([1,1,1,2,2,3],k=2): {top_k_frequent([1,1,1,2,2,3],2)}")
    print(f"  LongestConsec([100,4,200,1]): {longest_consecutive([100,4,200,1,3,2])}")
    hm=MyHashMap(); hm.put(1,10); hm.put(2,20)
    print(f"  HashMap get(1):               {hm.get(1)}")
    hm.remove(1)
    print(f"  HashMap get(1) removed:       {hm.get(1)}")
    print("="*58)
