def create_list(file):
  with open(file) as data:
    data_list = []
    for value in data:
      data_list.append(int(value.strip()))

  return data_list

def check_increases(array):
  i = 0
  count = 0

  while i < len(array) - 1: # Since the last element will have an index 1 less than the length
    if array[i + 1] > array[i]:
      count += 1
    i += 1
  
  return count

depth_list = create_list('day_1_input.txt')
result = check_increases(depth_list)

print(result)

