


nums=[4,3,5,6,7,2,1,0]


def partition(nums,low,high):
    pivot=nums[0]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j



def quicksort(nums,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quicksort(nums,low,p_index-1)
        quicksort(nums,p_index+1,high)

quicksort(nums,0,len(nums)-1)

print(nums)

            
            
            


