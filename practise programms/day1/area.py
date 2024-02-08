def max_area(height):
    max_area = 0
    left_pointer = 0
    right_pointer = len(height) - 1

    while left_pointer < right_pointer:
      
        width = right_pointer - left_pointer
        h_left = height[left_pointer]
        h_right = height[right_pointer]

      
        current_area = min(h_left, h_right) * width

       
        max_area = max(max_area, current_area)

       
        if h_left < h_right:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_area


input_array = [1, 5, 4, 3]
output = max_area(input_array)
print(f"Output: {output}")

