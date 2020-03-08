sec_per_min = 60
min_per_hour = 60
hour_per_day = 24
sec_per_hour = sec_per_min * min_per_hour
sec_per_day = sec_per_hour * hour_per_day

print(sec_per_hour)
print(sec_per_day)
print(sec_per_day / sec_per_hour)
print(sec_per_day // sec_per_hour)