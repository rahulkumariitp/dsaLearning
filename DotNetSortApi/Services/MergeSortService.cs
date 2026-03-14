namespace DotNetSortApi.Services
{
    /// <summary>
    /// Implementation of Merge Sort algorithm
    /// Time Complexity: O(n log n) best, average, and worst case
    /// Space Complexity: O(n)
    /// </summary>
    public class MergeSortService : IMergeSort
    {
        /// <summary>
        /// Sorts an array of numbers using merge sort
        /// </summary>
        public (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers)
        {
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();

            var arr = new List<double>(numbers);
            
            if (arr.Count > 1)
            {
                MergeSortHelper(arr, 0, arr.Count - 1);
            }

            stopwatch.Stop();
            double timeTakenMs = stopwatch.Elapsed.TotalMilliseconds;

            return (arr, timeTakenMs);
        }

        /// <summary>
        /// Helper method to recursively sort array using merge sort
        /// </summary>
        private void MergeSortHelper(List<double> arr, int left, int right)
        {
            if (left < right)
            {
                int mid = (left + right) / 2;

                // Recursively sort left half
                MergeSortHelper(arr, left, mid);

                // Recursively sort right half
                MergeSortHelper(arr, mid + 1, right);

                // Merge the sorted halves
                Merge(arr, left, mid, right);
            }
        }

        /// <summary>
        /// Merge two sorted subarrays
        /// </summary>
        private void Merge(List<double> arr, int left, int mid, int right)
        {
            // Create copies of the left and right subarrays
            var leftArr = arr.GetRange(left, mid - left + 1);
            var rightArr = arr.GetRange(mid + 1, right - mid);

            int i = 0, j = 0, k = left;

            // Merge the two subarrays back
            while (i < leftArr.Count && j < rightArr.Count)
            {
                if (leftArr[i] <= rightArr[j])
                {
                    arr[k] = leftArr[i];
                    i++;
                }
                else
                {
                    arr[k] = rightArr[j];
                    j++;
                }
                k++;
            }

            // Copy remaining elements from left subarray
            while (i < leftArr.Count)
            {
                arr[k] = leftArr[i];
                i++;
                k++;
            }

            // Copy remaining elements from right subarray
            while (j < rightArr.Count)
            {
                arr[k] = rightArr[j];
                j++;
                k++;
            }
        }
    }
}
