Console.WriteLine("Longest Palindrome");
Console.WriteLine(Solution.LongestPalindrome("babad"));
Console.WriteLine(Solution.LongestPalindrome("cbbd"));
Console.WriteLine(Solution.LongestPalindrome("racecar"));
Console.WriteLine(Solution.LongestPalindrome("tacocat"));
Console.WriteLine(Solution.LongestPalindrome("a"));

// Start by checking if a string s is of length L by doing a basic
// palindrome check algorithm (indices i,j are equivalent at each step)
// If a palindrome is not found, reduce L by 1 and try again.
// If a palindrome is not found until L=1 that substring is returned.
// An empty string will return ""

public class Solution
{
    public static string LongestPalindrome(string s)
    {
        string palindrome = "";
        for (int length = s.Length; length > 0; length--)
        {
            for (int start = 0; start + length <= s.Length; start++)
            {
                string checkString = s.Substring(start, length);
                if (Check(checkString))
                    return checkString;
            }
        }
        return palindrome;
    }
    public static bool Check(string s)
    {
        int left = 0;
        int right = s.Length - 1;
        while (left < right)
        {
            if (s[left] != s[right])
                return false;
            left++;
            right--;
        }
        return true;
    }
}
