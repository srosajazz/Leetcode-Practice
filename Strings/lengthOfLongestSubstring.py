class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        max_length = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                char_set.remove(s[left])
                left += 1

        return max_length
# Create an instance of the Solution class
sol = Solution()

# Call the lengthOfLongestSubstring method on the instance
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)  # Output should be 3
