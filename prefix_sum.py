def queries_sum(nums,queries,limit):
    prefix = [nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1]) #prefix[-1] gives the last element in the array

    ans = []
    for x,y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr<limit)

    print(ans) 

queries_sum([1,6,3,2,7,2],[[0,3],[2,5],[2,4]],13)



