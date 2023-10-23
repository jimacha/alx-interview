Curriculum <br>
**Short Specializations** <br>

# 0x04. UTF-8 Validation

## UTF-8 Validation Algorithm in Python

This Python script implements the UTF-8 validation algorithm, which checks whether a given list of integers represents a valid UTF-8 encoding sequence.

### Prerequisites

- Python 3.x installed on your system.

### How to Use

1. **Clone the Repository:**
   ```
   git clone <repository-url>
   cd utf-8-validation
   ```

2. **Run the Script:**
   ```
   python utf8_validation.py
   ```

3. **Input:**
   Modify the `data` list in the `utf8_validation.py` file to test different input sequences.

4. **Output:**
   The script will print whether the input sequence is a valid UTF-8 encoding or not.

### Algorithm Explanation

The UTF-8 encoding is a variable-width character encoding for Unicode. It can use one to four one-byte (8-bit) code units to represent a single character. The algorithm validates whether the given list of integers forms a valid UTF-8 encoding. It checks the following rules:

- A character in UTF-8 can be from 1 to 4 bytes long.
- For 1-byte character, the first bit is 0, followed by its Unicode code.
- For n-bytes character (n > 1), the first n bits are 1 followed by a 0, and then n - 1 bytes with the most significant 2 bits being 10.

### Example

```python
data = [197, 130, 1]  # Example input sequence
is_valid = utf8_validation(data)
print(f"Is the input sequence valid UTF-8? {'Yes' if is_valid else 'No'}")
```

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or a pull request.


Feel free to customize this README according to your project's specific needs. Good luck with your UTF-8 validation algorithm in Python!