namespace DotNetSortApi.Services
{
    /// <summary>
    /// Interface for Quick Sort algorithm
    /// </summary>
    public interface IQuickSort
    {
        /// <summary>
        /// Sorts an array of numbers using quick sort and returns execution time
        /// </summary>
        (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers);
    }
}
