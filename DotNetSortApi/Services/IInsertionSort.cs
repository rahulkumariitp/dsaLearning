namespace DotNetSortApi.Services
{
    /// <summary>
    /// Interface for Insertion Sort algorithm
    /// </summary>
    public interface IInsertionSort
    {
        /// <summary>
        /// Sorts an array of numbers using insertion sort and returns execution time
        /// </summary>
        (List<double> SortedArray, double TimeTakenMs) Sort(List<double> numbers);
    }
}
