# Scientific Data Encryption Analyzer

![Project Demo](demo.png)  

A Python tool that simulates XOR encryption on sample scientific datasets, introduces random transmission errors, and uses NumPy and SciPy to perform statistical analysis for detecting data integrity issues.

This repo shows lightweight encryption techniques combined with statistical error detection, with potential applications in protecting and validating scientific data (e.g., sensor readings, simulation outputs) in computational research environments.

## Key Features
- Generates sample scientific data (e.g., random measurements)
- Applies simple XOR encryption/decryption
- Simulates transmission errors (bit flips at a configurable rate)
- Analyzes differences using NumPy (mean, standard deviation) and SciPy (one-sample t-test)
- Gives a clear error detection output

## Technologies Used
- Python
- NumPy
- SciPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sequence9/Scientific-Data-Encryption-Analyzer.git
   cd Scientific-Data-Encryption-Analyzer
