namespace DotNetSortApi.Services
{
    /// <summary>
    /// Implementation of Insertion Sort algorithm
    /// Time Complexity: O(n²) average and worst case, O(n) best case
    /// Space Complexity: O(1)
    /// </summary>
    public class InsertionSortService : IInsertionSort
    {
        /// <summary>
        /// Sorts an array of numbers using insertion sort
        /// </summary>
        public (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers)
        {
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();

            var arr = new List<double>(numbers);
            int n = arr.Count;

            for (int i = 1; i < n; i++)
            {
                double key = arr[i];
                int j = i - 1;

                while (j >= 0 && key < arr[j])
                {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = key;
            }

            stopwatch.Stop();
            double timeTakenMs = stopwatch.Elapsed.TotalMilliseconds;

            return (arr, timeTakenMs);
        }
    }
}
