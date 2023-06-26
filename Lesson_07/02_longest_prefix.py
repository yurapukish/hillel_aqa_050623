# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# understand how many characters


# for
# startwith

l1 = ["flower", "flow", 'flight']
iter_obj = min(l1, key=lambda x: len(x))

# lesson solution
prefix = ''
for ch in iter_obj:
    prefix += ch
    if not all([el.startswith(prefix) for el in l1]):
        prefix = prefix[:-1]
        break
print(f'{prefix=}')





