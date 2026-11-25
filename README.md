
# 🔢 NumPy Analyzer

## 📌 Project Overview

The **NumPy Analyzer** is a Python-based numerical analysis project developed using Object-Oriented Programming (OOP) and the NumPy library.

This project allows users to create and perform different operations on 1D, 2D and 3D NumPy arrays.

It provides functionalities such as array indexing, slicing, mathematical operations, combining and splitting arrays, searching, sorting, filtering and statistical calculations.

The project uses NumPy for numerical computations and a menu-driven interface to allow users to perform different operations interactively.
Video Demonstration Video Link: 

## 🎯 Objectives

- To understand NumPy arrays and their operations.
- To create 1D, 2D and 3D arrays.
- To perform indexing and slicing operations.
- To perform mathematical operations on arrays.
- To combine and split NumPy arrays.
- To implement searching, sorting and filtering.
- To calculate statistical values using NumPy.
- To implement Object-Oriented Programming concepts.
- To develop a menu-driven numerical analysis application.

## 🚀 Features

1. **Array Creation**
   - Create 1D arrays.
   - Create 2D arrays.
   - Create 3D arrays.
   - Display created arrays.

2. **Array Indexing**
   - Access individual array elements.
   - Retrieve elements using index positions.
   - Handle invalid index inputs.

3. **Array Slicing**
   - Perform slicing on 1D arrays.
   - Perform row and column slicing on 2D arrays.
   - Perform depth-based slicing on 3D arrays.

4. **Mathematical Operations**
   - Addition
   - Subtraction
   - Multiplication
   - Division
   - Dot Product
   - Matrix Multiplication

5. **Combining and Splitting Arrays**
   - Combine arrays using `concatenate()`.
   - Split arrays using `array_split()`.
   - Handle different array dimensions.

6. **Search, Sort and Filter**
   - Search for specific values using `argwhere()`.
   - Sort arrays in ascending order.
   - Sort arrays in descending order.
   - Filter values using conditions:
     - Greater than
     - Less than
     - Equal to

7. **Aggregate Functions and Statistical Analysis**
   - Sum
   - Mean
   - Median
   - Standard Deviation
   - Variance
   - Minimum
   - Maximum
   - Percentile
   - Correlation Coefficient

8. **Object Management**
   - Count the number of objects created.
   - Display array information.
   - Access array data through a copy of the original array.

9. **Menu-Driven Interface**
   - Select operations through the main menu.
   - Perform multiple operations.
   - Exit the application.

## 🛠️ Python Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructor (`__init__`)
- Encapsulation
- Private Attributes
- Instance Methods
- Class Variables
- Class Methods (intended object-count functionality)
- Functions and Methods
- Conditional Statements
- While Loop
- Exception Handling
- User Input Handling
- Menu-Driven Programming

## 📚 Library Used

- **NumPy:** Used for creating arrays, mathematical operations, array manipulation and statistical calculations.

## 📂 Project Structure

```text
NumPy Analyzer/
│
├── numpy_analyzer.py
│
└── README.md
```

## ▶️ How to Run the Project

**Step 1:** Install Python on your system.

**Step 2:** Install the required library.

```bash
pip install numpy
```

**Step 3:** Create a Python file named `numpy_analyzer.py`.

**Step 4:** Copy the project code into the Python file.

**Step 5:** Open the project folder in VS Code.

**Step 6:** Run the Python file.

```bash
python numpy_analyzer.py
```

**Step 7:** Select the required operations from the main menu.

## 💻 Sample Program Output

```text
Welcome to NumPy Analyzer!

========== MAIN MENU ==========

1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit

Enter your choice: 1

Select Array Type:

1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 1

Enter array elements separated by space:
10 20 30 40 50

Array created successfully!

Array:
[10. 20. 30. 40. 50.]
```

## ⚠️ Input Validation Rules

- Array elements must be entered in a valid numerical format.
- The number of elements must match the specified array dimensions.
- Both arrays must have compatible dimensions for mathematical operations.
- Division by zero is not allowed.
- Matrix multiplication requires compatible matrix dimensions.
- Valid index positions must be entered.
- Percentile values must be between 0 and 100.
- Both arrays must have the same number of elements for correlation calculations.

## 📝 Assumptions

- The project accepts numerical input from the user.
- Array dimensions are specified during array creation.
- Mathematical operations are performed according to array dimensions.
- Array splitting divides the array into two sections.
- Correlation calculations require two arrays of equal size.
- The project uses NumPy for all numerical calculations.

## 🔮 Future Enhancements

- Add graphical data visualization using Matplotlib.
- Implement more advanced matrix operations.
- Add array reshaping and transposing features.
- Add support for saving and loading arrays.
- Improve input validation and error handling.
- Develop an interactive graphical user interface.

## 👩‍💻 Author

**Dhruvi Das**

Student | Python Programming & Data Analytics Project

## 📄 License

This project is developed for educational and learning purposes. No open-source license has been specified.

---

✨ Happy Coding! ✨
