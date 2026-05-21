'''
import math

print(f"{math.pi:.2f}")
print(f"{math.pi:.5}")
print(f"{math.pi:.5f}")
print(f"{math.pi:.1f}")
print(f"{math.pi:.1}")

'''

name = "Ana"
print(f"|{name:10}|")   # |Ana       |   (7 spaces after)
print(f"|{name:>10}|")  # |> for right align (default)|   explicit
print(f"|{name:<10}|")  # |Ana       |   left align
print(f"|{name:^10}|")  # |   Ana    |   center