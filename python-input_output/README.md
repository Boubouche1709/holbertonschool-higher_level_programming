# 🐍Python - Input/Output

<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width=40% height=40%/>
</p>

---
## 📁 Project: Python - Input/Output

This directory contains Python scripts that explore file operations (read/write), serialization (JSON), deserialization, and command-line argument parsing. The project follows Holberton School's curriculum and demonstrates fundamental I/O manipulation using Python.

---

## 📚 Ressources

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [sys package](https://docs.python.org/3/library/sys.html)

---

## 📝 Description

This project introduces core I/O capabilities in Python:

* Opening and managing files
* Reading from and writing to files
* Working with the `with` statement
* Serializing and deserializing Python objects using JSON
* Handling command-line arguments

---

## 🎯 Learning Objectives

* Understand how file handling works in Python
* Differentiate between reading, writing, and appending to a file
* Use `with` statement to safely handle file context
* Explain JSON serialization and deserialization
* Implement custom serialization methods in Python classes
* Access command line parameters in a script

---

## 🛠 Requirements

* Python version: 3.8.5
* OS: Ubuntu 20.04 LTS
* Code style: `pycodestyle` 2.7.\*
* All scripts should be executable and start with `#!/usr/bin/python3`
* A `README.md` is mandatory
* Test cases (where required) reside in the `tests/` directory

---

## ✅ Tasks

### 0. Read file

Reads a text file (UTF8) and prints its content to stdout.

### 1. Write to a file

Writes a string to a text file and returns the number of characters written.

### 2. Append to a file

Appends a string at the end of a text file and returns the number of characters added.

### 3. To JSON string

Returns the JSON representation of a Python object.

### 4. From JSON string to Object

Converts a JSON string into a Python data structure.

### 5. Save Object to a file

Writes an object to a file using JSON representation.

### 6. Create object from a JSON file

Creates an object from a JSON file.

### 7. Load, add, save

Adds all arguments to a Python list, then saves it as JSON to a file.

### 8. Class to JSON

Returns the dictionary description for JSON serialization of an object.

### 9. Student to JSON

Defines a `Student` class with a method to serialize its attributes.

### 10. Student to JSON with filter

Enhances serialization with an optional filter list of attributes.

### 11. Student to disk and reload

Saves a `Student` to a file and loads it back, updating its attributes.

### 12. Pascal's Triangle

Generates Pascal’s triangle of size `n` as a list of lists.

---
