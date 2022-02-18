nums = input().split()

def has_33(nums):
    nums = ''.join(nums)
    if '33' in nums:
        return True
    return False      
    
print(has_33(nums))