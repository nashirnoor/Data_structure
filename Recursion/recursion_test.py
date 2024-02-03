# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n* fact(n-1)
    
# d = fact(5)
# print(d)




# def sum_of_odd_numbers(lst, index=0, current_sum=0):
#     if index == len(lst):
#         return current_sum  # Base case: end of list reached
    
#     # Add the current element to the sum if it's odd
#     if lst[index] % 2 != 0:
#         current_sum += lst[index]
    
#     # Recursive call with updated index and sum
#     return sum_of_odd_numbers(lst, index + 1, current_sum)

# # Example usage:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# odd_sum = sum_of_odd_numbers(numbers)
# print("Sum of odd numbers:", odd_sum)  # Output: 16 (1 + 3 + 5 + 7)



def reverse(n):
    if len(n)==0:
        return n
    return reverse(n[1:]) + n[0]
    
a = reverse("hello")
print(a)
