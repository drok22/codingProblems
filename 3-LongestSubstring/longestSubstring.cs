// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// https://www.youtube.com/watch?v=fTIzYJvhsqg

// Its a sliding window problem! you did this at LI-COR

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        int start = 0;
        int end = 0;
        int maxLen = 0;
        HashSet<char> charSet = new();

        while (end < s.Length)
        {
            if (!charSet.Contains(s[end]))
            {
                charSet.Add(s[end]);
                end++;
                maxLen = Math.Max(maxLen, end - start);
            }
            else
            {
                charSet.Remove(s[start]);
                start++;
            }
        }
        return maxLen;
    }
}