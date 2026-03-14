namespace DotNetSortApi.Services
{
    /// <summary>
    /// Implementation of Quick Sort algorithm
    /// Average Time Complexity: O(n log n), Worst: O(n^2)
    /// Space Complexity: O(log n) on average
    /// </summary>
    public class QuickSortService : IQuickSort
    {
        public (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers)
        {
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();

            var arr = new List<double>(numbers);
            QuickSortHelper(arr, 0, arr.Count - 1);

            stopwatch.Stop();
            double timeTakenMs = stopwatch.Elapsed.TotalMilliseconds;

            return (arr, timeTakenMs);
        }

        private void QuickSortHelper(List<double> arr, int low, int high)
        {
            if (low < high)
            {
                int p = Partition(arr, low, high);
                QuickSortHelper(arr, low, p - 1);
                QuickSortHelper(arr, p + 1, high);
            }
        }

        private int Partition(List<double> arr, int low, int high)
        {
            double pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++)
            {
                if (arr[j] <= pivot)
                {
                    i++;
                    var tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
            var tmp2 = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = tmp2;
            return i + 1;
        }
    }
}
