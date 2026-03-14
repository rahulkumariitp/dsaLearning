namespace DotNetSortApi.Models
{
    /// <summary>
    /// Request model for sort endpoints
    /// </summary>
    public class SortRequest
    {
        public List<double> Numbers { get; set; } = new();
    }

    /// <summary>
    /// Response model for sort endpoints
    /// </summary>
    public class SortResponse
    {
        public List<double> SortedNumbers { get; set; } = new();
        public double TimeTakenMs { get; set; }
        public bool Success { get; set; }
        public string? Message { get; set; }
    }
}
