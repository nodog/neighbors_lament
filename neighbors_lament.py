
# take an integer as input, and output the largest integer below that uses the same digits.
# example: input 53442, output is 53424
# 34278 -> 32874

def list_to_int(input_list):
    return int("".join(str(i) for i in input_list), base=10)

def swap_value_i_with_next_highest_value(input_list, index):

    # print(input_list, index)
    
    next_highest_digit_index = None
    next_highest_digit = -1

    for j in range(index + 1, len(input_list)):
        if input_list[j] < input_list[index] and input_list[j] > next_highest_digit:
            next_highest_digit = input_list[j]
            next_highest_digit_index = j
    
    if next_highest_digit_index == None:
        return None
    
    list_copy = input_list.copy()

    list_copy[index] = input_list[next_highest_digit_index]
    list_copy[next_highest_digit_index]  = input_list[index]

    # print(f"list_copy = {list_copy}")

    return list_copy

def lesser_neighbor(n):

    # print(f"n = {n}")
    
    # can 10 be rearranged as 01? I'm going to say yes, because it's a list of digits.
    if n < 10:
        return None

    # using list comprehension
    # to convert number to list of integers
    list_of_digits = [int(x) for x in str(n)]

    # print(f"list_of_digits = {list_of_digits}")

    list_of_candidates = []

    # go through the list_of_digits from most sig to least
    #   swap current digit with next highest remaining
    #   rearrange remaining digits in descending order
    #   add to candidate list if not too high

    # print(f"len(list_of_digits) - 1 = {len(list_of_digits) - 1}")

    for i in range(0, len(list_of_digits) - 1):
        # print(f"i = {i}")
        #   swap current digit with next highest remaining
        local_swap_candidate = swap_value_i_with_next_highest_value(list_of_digits, i)
        #   rearrange remaining digits in descending order
        if local_swap_candidate:
            # print(f"i = {i}  local_swap_candidate = {local_swap_candidate}")
            local_candidate = local_swap_candidate[0:i+1] + sorted(local_swap_candidate[i+1:], reverse=True)
            # print(f"local_candidate = {local_candidate}")
            #   add to candidate list if not too high
            if list_to_int(local_candidate) < n:
                list_of_candidates.append(local_candidate)
 
    if list_of_candidates: 
        max_candidate = list_to_int(max(list_of_candidates))
        # print(f"result = {max_candidate}")
        return max_candidate
    else:
        return None

if __name__ =="__main__":
    n = 54823
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
    n = 978675
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
    n = 11973
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
    n = 1324354657
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
    n = 98765433256789
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
    n = 8889
    print(f"lesser_neighbor({n}) = {lesser_neighbor(n)}")
