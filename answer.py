import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        """
        Initialize the Bloom filter with a given size and number of hash functions.
        
        :param size: The size of the bit array.
        :param num_hashes: The number of hash functions to use.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0 for _ in range(size)]  # Initialize the bit array with zeros

    def _hashes(self, url):
        """
        Generate hash values for a given URL using multiple hash functions.
        
        :param url: The URL to hash.
        :return: A list of hash values.
        """
        hash_values = []
        for i in range(self.num_hashes):
            # Create a hash value using MD5 and mod it with the size of the bit array
            hash_value = int(hashlib.md5((url + str(i)).encode()).hexdigest(), 16) % self.size
            hash_values.append(hash_value)
        return hash_values

    def add(self, url):
        """
        Add a URL to the Bloom filter.
        
        :param url: The URL to add.
        """
        if all(self.bit_array[hash_value] == 1 for hash_value in self._hashes(url)):
            print(f"Warning: The Bloom filter is full. Cannot add {url}.")
            return
        for hash_value in self._hashes(url):
            self.bit_array[hash_value] = 1  # Set the corresponding bit to 1

    def contains(self, url):
        """
        Check if a URL is in the Bloom filter.
        
        :param url: The URL to check.
        :return: True if the URL is in the Bloom filter, False otherwise.
        """
        return all(self.bit_array[hash_value] for hash_value in self._hashes(url))

def process_input(input_file, output_file, bloom_filter):
    """
    Process the input file and write results to the output file using the Bloom filter.
    
    :param input_file: The input file containing commands and URLs.
    :param output_file: The output file to write results to.
    :param bloom_filter: The Bloom filter instance to use.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                command, url = line.strip().split(' ', 1)  # Split each line into command and URL
                if command == 'ADD':
                    bloom_filter.add(url)  # Add the URL to the Bloom filter
                    outfile.write(f"Added: {url}\n")
                elif command == 'CONTAINS':
                    result = bloom_filter.contains(url)  # Check if the URL is in the Bloom filter
                    outfile.write(f"URL Existence Check for {url}: {result}\n")
                else:
                    outfile.write(f"Invalid command: {command}\n")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Configurable size and number of hash functions
bloom_filter_size = 10000000
num_hash_functions = 3

# Create a Bloom filter instance
bloom_filter = BloomFilter(bloom_filter_size, num_hash_functions)

# Process the input file and write to the output file
process_input('inputPS03.txt', 'outputPS03.txt', bloom_filter)