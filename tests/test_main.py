import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_two_sum():
    assert two_sum([2,7,11,15],9) == [0,1]
    assert two_sum([3,2,4],6) == [1,2]
    assert two_sum([3,3],6) == [0,1]

def test_group_anagrams():
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    assert len(result) == 3

def test_subarray_sum():
    assert subarray_sum_k([1,1,1],2) == 2
    assert subarray_sum_k([1,2,3],3) == 2

def test_longest_unique():
    assert longest_unique_window("abcabcbb") == 3
    assert longest_unique_window("bbbbb") == 1
    assert longest_unique_window("pwwkew") == 3

def test_top_k():
    result = top_k_frequent([1,1,1,2,2,3],2)
    assert 1 in result and 2 in result

def test_longest_consecutive():
    assert longest_consecutive([100,4,200,1,3,2]) == 4

def test_hashmap():
    hm = MyHashMap()
    hm.put(1,10); hm.put(2,20)
    assert hm.get(1) == 10
    hm.remove(1)
    assert hm.get(1) == -1
