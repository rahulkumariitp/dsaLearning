using DotNetSortApi.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddControllers();
builder.Services.AddOpenApi();

// Register sorting service for dependency injection
builder.Services.AddScoped<IInsertionSort, InsertionSortService>();
builder.Services.AddScoped<IMergeSort, MergeSortService>();
builder.Services.AddScoped<IQuickSort, QuickSortService>();

// Add CORS policy to allow requests from React frontend
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowReactApp", builder =>
    {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// Enable CORS with the defined policy
app.UseCors("AllowReactApp");

app.UseHttpsRedirection();
app.UseAuthorization();

app.MapControllers();
app.Run();
