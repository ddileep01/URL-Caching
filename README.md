Design Document for Web Crawler application 
Problem Statement
The goal is to create a web crawler application that efficiently checks whether a URL has been previously processed to avoid redundant processing. A Bloom filter is implemented to optimize this process by caching URLs. The solution uses Python 3.7+ and adheres to constraints such as avoiding external libraries.
Data Structure
Choice of Data Structure: Bloom Filter

The Bloom filter is used to store hashes of URLs. The filter uses multiple hash functions to map a URL to a set of bits in an array. When checking if a URL is processed, the filter checks whether all the corresponding bits are set; if any bit is not set, the URL has not been processed.

Justification:
Memory Usage: Bloom filters are more memory-efficient, especially when dealing with large datasets. They use a fixed-size bit array.
False Positives: Bloom filters can produce false positives, meaning they might indicate that a URL is present when it is not.
Performance: Bloom Filters offer O(1) average time complexity for insertion and lookup and trade accuracy for memory efficiency.

In a Bloom filter, hash functions play a critical role in determining how URLs (or any data) are mapped to the bit array. The efficiency and accuracy of a Bloom filter are highly dependent on the choice and number of hash functions used. A hash function is used in a Bloom filter to map an input (in this case, a URL or a string) to a specific position in a bit array. The Bloom filter uses multiple hash functions to determine several positions in the bit array. Each hash function independently computes a hash value for the input, and the corresponding bit in the bit array is set to 1. This ensures that multiple positions are marked, reducing the likelihood of false negatives (but potentially increasing false positives). 
First Hash Function:
Concatenate the URL with the integer 0: example.com0.
Compute the MD5 hash of example.com0, which might result in a hash value like d41d8cd98f00b204e9800998ecf8427e.
Convert this hash value to an integer and take modulo the size of the bit array (let's assume the size is 1000 for simplicity). This gives a position in the bit array, say position1.

Second Hash Function:
Concatenate the URL with the integer 1: example.com1.
Compute the MD5 hash of example.com1, which might result in a hash value like 0cc175b9c0f1b6a831c399e269772661.
Convert this hash value to an integer and take modulo the size of the bit array. This gives another position in the bit array, say position2.

Third Hash Function:
Concatenate the URL with the integer 2: example.com2.
Compute the MD5 hash of example.com2, which might result in a hash value like 92eb5ffee6ae2fec3ad71c777531578f.
Convert this hash value to an integer and take modulo the size of the bit array. This gives us yet another position in the bit array, say position3.
So, for the URL example.com, the three hash functions generate three different positions in the bit array: position1, position2, and position3.

When the URL is added to the Bloom filter, the bits at these positions is set to 1. When the URL is checked in the Bloom filter, it is verified that the bits at these positions are all set to 1.
Operations and Time complexity
The time complexity of the provided code can be analyzed as follows:
Initialization of the Bloom Filter:
The _init_ method initializes the bit array with zeros. This operation takes O(n) time, where n is the size of the bit array.

Hash Function Calculation:
The _hashes method generates multiple hash values for a given URL. Each hash calculation involves creating an MD5 hash and taking a modulo operation. The time complexity for generating k hash values is O(k), where k is the number of hash functions.

Adding a URL:
The add method calls the _hashes method to generate hash values and then sets the corresponding bits in the bit array. The time complexity for adding a URL is O(k), where k is the number of hash functions.

Checking for URL Containment:
The contains method calls the _hashes method to generate hash values and then checks the corresponding bits in the bit array. The time complexity for checking if a URL is in the Bloom filter is O(k), where k is the number of hash functions.
Processing Input File:
The process_input function reads the input file line by line and processes each command. The time complexity for processing each line depends on whether the command is ADD or CONTAINS, both of which have a time complexity of O(k). Therefore, the overall time complexity for processing the input file is O(m⋅k), where m is the number of lines in the input file and k is the number of hash functions.

In summary, the time complexity for the main operations in the Bloom filter is O(k), where k is the number of hash functions. The overall time complexity for processing the input file is O(m⋅k), where m is the number of lines in the input file.

Error Handling
Invalid Input File: If the input file does not exist, an appropriate error message is displayed.

Alternative Design
Alternative Data Structure: Hash Table
A hash table is a data structure that maps keys to values using a hash function. In this case, the keys would be URLs, and the values could be simple flags indicating the presence of the URLs.
Implementation Steps:
Initialization: Create a hash table with an appropriate size. 
Adding a URL: Compute the hash of the URL and store it in the hash table.
Checking for URL Containment: Compute the hash of the URL and check if it exists in the hash table.
Time Complexity:
Initialization: O(1) for creating an empty hash table.
Adding a URL: O(1) on average, assuming a good hash function and low collision rate.
Checking for URL Containment: O(1) on average, assuming a good hash function and low collision rate. 

Space Complexity: The space complexity is O(n), where n is the number of URLs stored in the hash table.


Advantages:
1. Exact Membership Check: Unlike Bloom filters, hash tables provide exact membership checks without false positives.
2. Constant Time Operations: Both insertion and lookup operations are O(1) on average, making them very efficient.
Disadvantages:
1. Higher Memory Usage: Hash tables typically require more memory than Bloom filters because they store the actual URLs or their hash values.
2. Potential Collisions: Although hash tables are designed to handle collisions, a poor hash function or high load factor can degrade performance.

Analysis and Results
To analyze the correlation between the Bloom filter size and the number of hash functions, we conducted multiple experiments. The graph below shows how the false positive rate varies with different hash function counts for various Bloom filter sizes.

Observations:
As the number of hash functions increases, the false positive rate initially decreases.
However, after a certain point, adding more hash functions can slightly increase the false positive rate due to increased bit collisions.
Larger Bloom filters (higher bit array sizes) generally have lower false positive rates.
Conclusion
The chosen implementation efficiently meets the requirements for implementing an efficient web crawler that uses a Bloom filter to avoid redundant URL processing. Choosing between a Bloom filter and a hash table depends on the specific requirements of the application. If memory efficiency is crucial and occasional false positives are acceptable, a Bloom filter is a suitable choice. On the other hand, if exact membership checks are required and memory usage is less of a concern, a hash table is a better option.
