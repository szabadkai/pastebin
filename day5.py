def parse_modes(m):
    mode = [0, 0, 0]
    for i,char in enumerate(reversed(m)):
        mode[i] = int(char)
    return mode
#
#
# Opcode 3 takes a single integer as input and saves it to the address given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.

def calculate(num1, nums):
    idx = 0
    nums = nums
    while nums[idx] != 99:
        num, modes = int(str(nums[idx])[-2:]), str(nums[idx])[:-3]
        mode = parse_modes(modes)
        inc = 4
        if num == 1:
            val1 = nums[idx + 1] if mode[0] == 1 else nums[nums[idx + 1]]
            val2 = nums[idx + 2] if mode[1] == 1 else nums[nums[idx + 2]]
            idx3 = nums[idx + 3]
            nums[idx3] = val1 + val2
        elif num == 2:
            val1 = nums[idx + 1] if mode[0] == 1 else nums[nums[idx + 1]]
            val2 = nums[idx + 2] if mode[1] == 1 else nums[nums[idx + 2]]
            idx3 = nums[idx + 3]
            nums[idx3] = val1 - val2
        elif num == 3:
            val1 = nums[idx + 1]
            nums[num1] = val1
            inc = 2
        elif num == 4:
            val1 = nums[nums[idx + 1]]
            print(val1)
            inc = 2
        idx += inc
    return nums


with open("input") as f:
    for line in f:
        input_values = [int(num) for num in line.split(",")]
        print(calculate(1, input_values[:]))
