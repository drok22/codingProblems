public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        double median = 0.0;
        int[] mergedArray = nums1.concat(nums2).ToArray();
        Array.Sort(mergedArray);
        int list_length = mergedArray.Length;
        int middle_loc = list_length % 2;

        if (middle_loc == 0) // even length
        {
            int midIndex1 = list_length / 2 - 1;
            int midIndex2 = list_length / 2;
            median = (mergedArray[midIndex1] + mergedArray[midIndex2]) / 2.0;
        }
        else // odd length
        {
            int midIndex = list_length / 2;
            median = mergedArray[midIndex];
        }
        return median;
    }
}