nums = input().split()

def has_007(nums):
    nums = ''.join(nums)
    if '007' in nums:
        return True
    return False      
    
print(has_007(nums))