# Web Crawler with Bloom Filter

## Problem Statement
The goal of this project is to develop a web crawler that efficiently tracks whether a URL has been previously processed, preventing redundant processing. A Bloom filter is implemented to optimize memory usage and speed while handling large datasets.

![Web Crawler Diagram](https://example.com/web_crawler_diagram.jpg)

## Technology Stack
- **Programming Language**: Python 3.7+
- **Data Structure**: Bloom Filter (Avoids external libraries for constraints compliance)

## Data Structure: Bloom Filter
A Bloom filter is a space-efficient probabilistic data structure used to check membership. Instead of storing actual URLs, it hashes them into a fixed-size bit array using multiple hash functions.

### Justification for Bloom Filter
- **Memory Efficiency**: Uses a fixed-size bit array, making it suitable for large datasets.
- **Fast Operations**: Provides O(1) time complexity for insertions and lookups.
- **False Positives**: Might return false positives, but never false negatives.

![Bloom Filter Structure](https://example.com/bloom_filter_structure.jpg)

### Hash Function Implementation
1. Concatenate the URL with an integer (0, 1, 2, ...).
2. Compute the MD5 hash of the concatenated string.
3. Convert the hash to an integer and take modulo the bit array size.
4. Set the corresponding bit(s) in the Bloom filter.

## Operations and Time Complexity
| Operation | Time Complexity |
|-----------|----------------|
| Initialization | O(n) |
| Hash Computation | O(k) (where k is the number of hash functions) |
| Adding a URL | O(k) |
| Checking a URL | O(k) |
| Processing an Input File | O(m \* k) (where m is the number of lines in the file) |

## Error Handling
- **Invalid Input File**: Displays an error message if the file is missing or corrupted.

## Alternative Design: Hash Table
A hash table could be used instead of a Bloom filter.

### Comparison with Bloom Filter
| Feature | Bloom Filter | Hash Table |
|---------|-------------|------------|
| Memory Efficiency | High | Lower |
| False Positives | Yes | No |
| Exact Membership Check | No | Yes |
| Time Complexity (Lookup) | O(k) | O(1) |

![Hash Table vs Bloom Filter](https://example.com/hash_table_vs_bloom_filter.jpg)
![image](https://github.com/user-attachments/assets/eed727c1-0b10-40dd-ba20-c28930c8e5c1)


## Conclusion
The Bloom filter is chosen for its efficiency in handling large datasets with minimal memory. While it may introduce false positives, it significantly reduces memory usage and lookup time, making it ideal for web crawling applications. If exact membership verification is needed, a hash table can be considered as an alternative.
