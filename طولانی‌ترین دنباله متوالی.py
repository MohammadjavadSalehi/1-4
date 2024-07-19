def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    longest_sequence = []
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            current_sequence = [current_num]
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                current_sequence.append(current_num)
            
            if current_length > max_length:
                max_length = current_length
                longest_sequence = current_sequence
    
    return max_length, longest_sequence

input_data = input()

nums = eval(input_data)

max_length, longest_sequence = longest_consecutive(nums)

print(f"{max_length} (sequence: {longest_sequence})")
