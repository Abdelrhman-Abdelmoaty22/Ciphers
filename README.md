#  Encryption Algorithms in Python
This repository contains a collection of Python scripts implementing various classical encryption algorithms. Each script demonstrates the core principles behind these algorithms, making it an excellent resource for learning and experimentation.

# Overview
This repository showcases a variety of classical encryption techniques, implemented in Python. These algorithms are fundamental in the study of cryptography and serve as a stepping stone to understanding more complex encryption methods. Each script is designed to be simple yet effective, making it easy to grasp the underlying concepts.

# Scripts
# `PlayFair.py`
The PlayFair cipher is a digraph substitution cipher that encrypts pairs of letters together. This script includes:


    * Key matrix generation
    * Handling of digraphs and padding
    * Encryption and decryption functions
# `Cezar.py`
The Caesar cipher is one of the earliest and simplest encryption techniques. This script demonstrates:

    * Shifting of characters based on a key
    * Encryption and decryption processes
# `Hill.py`
The Hill cipher is a polygraphic substitution cipher based on linear algebra. This script features:

    * Matrix key generation
    * Matrix multiplication for encryption
    * Inverse matrix calculation for decryption
# `DES_BY_ME.py`
This script implements a simplified version of the Data Encryption Standard (DES), a symmetric-key algorithm. It includes:

    * Key generation and permutation functions
    * Encryption and decryption functions
    * Feistel network implementation
# `Vigenere.py`
The Vigenère cipher is a method of encrypting text by using a series of different Caesar ciphers based on the letters of a keyword. This script provides:

    * Key expansion to match text length
    * Encryption and decryption functions
# Getting Started
To get started with these scripts, you'll need Python installed on your system. Clone the repository and navigate to the directory containing the scripts.


    `git clone https://github.com/yourusername/encryption-algorithms-python.git`
    cd encryption-algorithms-python
# Usage
Each script can be run directly from the command line. They typically require input text and a key. Below is an example of how to run `Cezar.py`:

    python Cezar.py
Follow the prompts to enter the text and the key.

# Contributing
Contributions are welcome! If you have improvements or additional encryption algorithms to add, please feel free to fork the repository, make your changes, and submit a pull request.
