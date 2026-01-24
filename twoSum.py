def twoSum(nums: list, target: int) -> list:
    reminders = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        reminder = reminders.get(diff)
        if reminder != None:
            return [reminder, i]
        reminders[nums[i]] = i


if __name__ == '__main__':
    res = twoSum([2,7,11,15], 9)
    res