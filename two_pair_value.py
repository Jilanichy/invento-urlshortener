def get_aspected_index(two_pair_values, target_value):
  # saving all the matched result in this list
  result_list = []
  
  # iterating through all the pairs and returning the index of last one
  #complexity O(n)
  for pair in range(len(two_pair_values)):
    sum = two_pair_values[pair][0] + two_pair_values[pair][1]
    if sum == target_value:
      result_list.append(pair)
  return result_list[-1]
  
'''
An array will have two integer pair values and will have a target value. Now you have to find the index of two pair values by (target value == sum of two pair values).
'''
two_pair_values = [
[1, 5],
[9, -7],
[0, 8],
[6, 3],
[4, 11],
[14, 0],
[8, 1],
[4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result) # result will be shown 6
