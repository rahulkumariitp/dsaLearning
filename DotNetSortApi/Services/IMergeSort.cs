namespace DotNetSortApi.Services
{
    /// <summary>
    /// Interface for Merge Sort algorithm
    /// </summary>
    public interface IMergeSort
    {
        /// <summary>
        /// Sorts an array of numbers using merge sort and returns execution time
        /// </summary>
        (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers);
    }
}
