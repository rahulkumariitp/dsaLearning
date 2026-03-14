using Microsoft.AspNetCore.Mvc;
using DotNetSortApi.Models;
using DotNetSortApi.Services;

namespace DotNetSortApi.Controllers
{
    /// <summary>
    /// API controller for sorting operations
    /// </summary>
    [ApiController]
    [Route("api/[controller]")]
    public class SortController(IInsertionSort insertionSort, IMergeSort mergeSort, IQuickSort quickSort, ILogger<SortController> logger) : ControllerBase
    {
        private readonly IInsertionSort _insertionSort = insertionSort;
        private readonly IMergeSort _mergeSort = mergeSort;
        private readonly IQuickSort _quickSort = quickSort;
        private readonly ILogger<SortController> _logger = logger;

        /// <summary>
        /// POST /api/sort/insertion
        /// Sorts an array using Insertion Sort algorithm
        /// </summary>
        [HttpPost("insertion")]
        public ActionResult<SortResponse> InsertionSort([FromBody] SortRequest request)
        {
            try
            {
                // Validate input
                if (request?.Numbers == null || request.Numbers.Count == 0)
                {
                    return BadRequest(new SortResponse
                    {
                        Success = false,
                        Message = "Invalid request. Numbers array is required and must not be empty."
                    });
                }

                _logger.LogInformation($"Sorting {request.Numbers.Count} numbers using Insertion Sort");

                // Perform sorting
                var (sortedArray, timeTakenMs) = _insertionSort.Sort(request.Numbers);

                var response = new SortResponse
                {
                    SortedNumbers = sortedArray,
                    TimeTakenMs = timeTakenMs,
                    Success = true
                };

                return Ok(response);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error during sorting: {ex.Message}");
                return StatusCode(500, new SortResponse
                {
                    Success = false,
                    Message = $"Error: {ex.Message}"
                });
            }
        }

        /// <summary>
        /// POST /api/sort/merge
        /// Sorts an array using Merge Sort algorithm
        /// </summary>
        [HttpPost("merge")]
        public ActionResult<SortResponse> MergeSort([FromBody] SortRequest request)
        {
            try
            {
                // Validate input
                if (request?.Numbers == null || request.Numbers.Count == 0)
                {
                    return BadRequest(new SortResponse
                    {
                        Success = false,
                        Message = "Invalid request. Numbers array is required and must not be empty."
                    });
                }

                _logger.LogInformation($"Sorting {request.Numbers.Count} numbers using Merge Sort");

                // Perform sorting
                var (sortedArray, timeTakenMs) = _mergeSort.Sort(request.Numbers);

                var response = new SortResponse
                {
                    SortedNumbers = sortedArray,
                    TimeTakenMs = timeTakenMs,
                    Success = true
                };

                return Ok(response);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error during sorting: {ex.Message}");
                return StatusCode(500, new SortResponse
                {
                    Success = false,
                    Message = $"Error: {ex.Message}"
                });
            }
        }

        /// <summary>
        /// POST /api/sort/quick
        /// Sorts an array using Quick Sort algorithm
        /// </summary>
        [HttpPost("quick")]
        public ActionResult<SortResponse> QuickSort([FromBody] SortRequest request)
        {
            try
            {
                // Validate input
                if (request?.Numbers == null || request.Numbers.Count == 0)
                {
                    return BadRequest(new SortResponse
                    {
                        Success = false,
                        Message = "Invalid request. Numbers array is required and must not be empty."
                    });
                }

                _logger.LogInformation($"Sorting {request.Numbers.Count} numbers using Quick Sort");

                // Perform sorting
                var (sortedArray, timeTakenMs) = _quickSort.Sort(request.Numbers);

                var response = new SortResponse
                {
                    SortedNumbers = sortedArray,
                    TimeTakenMs = timeTakenMs,
                    Success = true
                };

                return Ok(response);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Error during sorting: {ex.Message}");
                return StatusCode(500, new SortResponse
                {
                    Success = false,
                    Message = $"Error: {ex.Message}"
                });
            }
        }

        /// <summary>
        /// GET /api/sort/health
        /// Health check endpoint
        /// </summary>
        [HttpGet("health")]
        public ActionResult<object> Health()
        {
            return Ok(new { status = "healthy" });
        }
    }
}
