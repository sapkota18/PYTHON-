
def find_majority_element(nums):
    count_dict={}
    n=len(nums)
    
    for num in nums:
        count_dict[num]=count_dict.get(num ,0)+1
    
    for num,count in count_dict.items():
        if count>n/2:
            return num
    
    return "No majority element"

nums1=[3,3,4,2,3,3,3,3]
nums2=[1,2,3,4]


print(f"majority element in {nums1}:{find_majority_element(nums1)}")
print(f"majority element in {nums2}:{find_majority_element(nums2)}")
