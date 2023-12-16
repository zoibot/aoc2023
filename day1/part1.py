ls = open('input.txt').readlines()
vals = []
for l in ls:
    nums = [c for c in l if c.isdigit()]
    vals.append(int(nums[0] + nums[-1]))
print(sum(vals))
