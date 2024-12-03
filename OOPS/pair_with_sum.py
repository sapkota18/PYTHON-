
def find_pairs_with_sum(nums,target):
    seen=set()
    pairs=[]
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement,num))
        seen.add(num)
    return pairs
nums = [1, 2, 3, 4, 5]
target = 6
result = find_pairs_with_sum(nums, target)
print(result)