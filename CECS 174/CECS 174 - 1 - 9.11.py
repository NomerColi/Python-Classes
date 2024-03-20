print("Insert time in float type")
total_time = eval(input()) # takes 0 or 1 parameter only and returns back a str

MIN = 60
SEC = 3600

h = int(total_time)
mf = (total_time - h) * 60
m = int((total_time - h) * 60)
s = int((mf - m) * 60)


print("hour", h, "minute", m, "second", s, "in", total_time)
print(f"hour {h:2d} minute {m} second {s} in {total_time:20.2f}")

total_second = int(total_time * SEC) # do not use magic numbers like 3600
print("total second", total_second)

h = total_second // SEC
m = total_second % 3600 // 60

print("hour", h, "minute", m, "second", s, "in", total_time)
