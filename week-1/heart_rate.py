"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input('Please enter your age: '))

heart_rate_max = 220 - age
heart_rate_low = int(heart_rate_max * 0.65)
heart_rate_high = int(heart_rate_max * 0.85)

# print('Your age is', age)

print('When you exercise to strengthen your heart, you should')
print('keep your heart rate between', heart_rate_low, 'and', heart_rate_high, 'beats per minute.')