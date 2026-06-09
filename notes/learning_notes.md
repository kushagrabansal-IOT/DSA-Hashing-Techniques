# Hashing — Learning Notes
# By Kushagra Bansal | Project Lab India

## Hash Patterns (MASTER THESE)
| Pattern | When | Code |
|---------|------|------|
| Frequency Count | count occurrences | Counter(arr) |
| Complement Lookup | two sum | if target-x in seen |
| Prefix+Hash | subarray sum=k | freq[prefix-k] |
| Sliding+Hash | longest window | seen[c] >= l |
| Group by key | anagrams | d[sorted(s)] |

## Two Sum Variations
- Unsorted array: HashMap complement in O(n)
- Sorted array: Two pointers in O(n) O(1) space
- Multiple pairs: Sort + two pointers
- Three sum: Fix one, two-sum the rest
- K sum: Reduce to two-sum recursively

## defaultdict vs Counter
defaultdict(int): auto-initialize to 0
Counter(arr): frequency map, supports .most_common(k)
Both: O(1) average lookup, O(n) space

## Hash Collision Resolution
Chaining: Each bucket is a linked list
Open Addressing: Linear probe, Quadratic probe, Double hashing
Load Factor: resize when size/capacity > 0.7
