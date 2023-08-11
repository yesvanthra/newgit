# newgit
* This is a simple Python program that splits a given string into different fields using varying delimiters. It uses the `re` (regular expression) module to perform the splitting based on the provided delimiters.
<div align="center">
  <h1>String Splitting with Delimiters</h1>
  <p>A simple Python program to split a string into fields using varying delimiters.</p>
</div>

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Python program demonstrates how to split a string into different fields using varying delimiters. The `re` (regular expression) module is used to perform the splitting based on the provided delimiters.

## Usage

1. **Prerequisites:** Make sure you have Python installed on your system.

2. **Clone the Repository:** Clone this repository or download the `stringsplitting.py` file.

3. **Run the Program:** Open the `stringsplitting.py` file and find the `stringsplittingwithdelimiter` function. Modify the `text` and `delimiters` arguments to test with different inputs.

   ```bash
   python stringsplitting.py

  ## Example

  For example, running the program with the provided input:

  ```bash
  stringsplittingwithdelimiter("sdfkdjsadfsd diweiw;1231:foo", ' ;:')
  ['sdfkdjsadfsd', 'diweiw', '1231', 'foo']
