var solution = new Solution();
Console.WriteLine(solution.ScoreOfString("aa"));
Console.WriteLine(solution.ScoreOfString("hello"));
Console.WriteLine(solution.ScoreOfString("zaz"));

public class Solution
{
    public int ScoreOfString(string s)
    {
        int score = 0;

        for (int i = 0; i < s.Length - 1; i++)
            score += Math.Abs((int)s[i] - (int)s[i + 1]);

        return score;
    }
}