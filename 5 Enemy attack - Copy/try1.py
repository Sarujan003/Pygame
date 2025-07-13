def finIndex(nums,target):
        first = 0
        last = len(nums) - 1
        while (first <= last):
                mid = (first+last)//2
                if nums[mid] == target:
                        while mid >= 0:
                                if nums[mid] == target:
                                        mid = mid - 1
                                        continue
                                else:
                                        break
                        mid = mid + 1
                        index_1 = mid
                        while mid < len(nums):
                                if nums[mid] == target:
                                        mid = mid + 1
                                        continue
                                else:
                                        break
                        index_2 = mid - 1
                        return [index_1,index_2]
                else:
                        if nums[mid] > target:
                                last = mid - 1
                        elif nums[mid] < target:
                                first = mid + 1
        return [-1,-1]

nums = [5,7,7,8,8,10]
print(finIndex(nums , 8))