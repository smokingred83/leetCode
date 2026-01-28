
def containsDuplicate(nums: [int]) -> bool:
    elements = set()
    for n in nums:
        if n in elements:
            return True
        elements.add(n)
    return False

if __name__ == '__main__':
    res = containsDuplicate([1,2,3,1])
    res