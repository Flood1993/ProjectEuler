# Work on this one

nums = set()

cnt = 2
prod = 1

while True:
    if prod in nums:
        break

    nums.add(prod)

    prod = (prod * cnt) % 100000
    cnt += 1

print(cnt)
print(nums)
