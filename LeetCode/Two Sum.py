def twoSum(nums, target):
    answers = []
    for x in nums:
        y = target - x
        if (y) in (nums[nums.index(x) + 1:]):
            answers.append(x)
            answers.append(y)
            ind_1 = nums.index(answers[0])
            nums[ind_1] = 'x'
            ind_2 = nums.index(answers[1])
    print([ind_1, ind_2])