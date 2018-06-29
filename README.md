# Design-of-experiment matrix generator for engineering and statistics
### Copyright Notice
Copyright (c) <2018-2028, Tirthajyoti Sarkar> 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Features
### Functions available:
* Full factorial,
* 2-level fractional factorial,
* Plackett-Burman,
* Sukharev grid,
* Box-Behnken,
* Box-Wilson (Central-composite) with center-faced option,
* Box-Wilson (Central-composite) with center-inscribed option,
* Box-Wilson (Central-composite) with center-circumscribed option,
* Latin hypercube (simple),
* Latin hypercube (space-filling),
* Random k-means cluster,
* Maximin reconstruction,
* Halton sequence based,
* Uniform random matrix 

## Acknowledgements and Requirements
The code was written in Python 3.6. It uses following external packages that needs to be installed on your system to use it,
* pydoe
* diversipy
* numpy
* pandas
