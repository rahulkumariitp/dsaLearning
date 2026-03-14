// Type definitions for Sort Request and Response
export interface SortRequest {
  backend: 'python' | 'dotnet'
  algorithm: 'insertion' | 'merge' | 'quick'
  numbers: number[]
  apiUrl: string
}

export interface SortResponse {
  sorted_numbers?: number[] // Python API response format
  sortedNumbers?: number[] // .NET API response format
  time_taken_ms?: number // Python API format
  timeTakenMs?: number // .NET API format
}

export interface BackendConfig {
  name: string
  value: 'python' | 'dotnet'
  url: string
}
