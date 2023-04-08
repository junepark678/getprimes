# Prime Number Generator

This program uses the "Sieve of Atkin" algorithm to sieve primes. It is an optimized version of the "Sieve of Eratosthenes". Although this program is written in Python, the "setup.py" file contains code to allow use with "Cython" which is a Python-to-C which allows it to achieve higher performance:

With Cython:
```
real	0m1.881s
user	0m1.845s
sys	0m0.036s
```
Without Cython:
```
real	0m2.032s
user	0m1.983s
sys	0m0.048s
```

Although some may say only 0.2s is neglegable, when I was running this test it felt very different. 

### Usage

To run this program without Cython, just run the `main.py` file.
To run this program with Cython:
1. `pip install Cython`
2. `pip install .`
3. Copy over the `usage.py` file to a different directory and run it.

The results for `usage.py` will be in `file1`, and `main.py` will be in `test1`.





















