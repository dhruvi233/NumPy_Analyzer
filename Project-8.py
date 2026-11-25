import numpy as np

class DataAnalytics:
    count = 0

    def __init__(self, arr):
        self.__arr = arr
        DataAnalytics.count +=1

    def display(self):
        print("Array:")
        print(self.__arr)

    def get_array(self):
        return self.__arr.copy()

    
    def show_count(cls):
        print("Total objects created:", cls.count)

    
    def welcome():
        print("\nWelcome to NumPy Analyzer!")

    
    def __check_array(self):
        if self.__arr.size == 0:
            print("Array is empty.")
            return False
        return True

    
    def indexing(self):
        if not self.__check_array():
            return

        print("Array:", self.__arr)

        indices = input(
            "Enter index positions separated by comma: "
        )

        try:
            index = tuple(
                int(x.strip()) for x in indices.split(",")
            )

            if len(index) != self.__arr.ndim:
                print("Enter the correct number of indices.")
                return

            print("Element:", self.__arr[index])

        except (ValueError, IndexError):
            print("Invalid index.")

    
    def slicing(self):
        print("Array:", self.__arr)

        if self.__arr.ndim == 1:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))

            print("Sliced Array:", self.__arr[start:end])

        elif self.__arr.ndim == 2:
            r1 = int(input("Enter row start: "))
            r2 = int(input("Enter row end: "))

            c1 = int(input("Enter column start: "))
            c2 = int(input("Enter column end: "))

            print("Sliced Array:")
            print(self.__arr[r1:r2, c1:c2])

        else:
            start = int(input("Enter depth start: "))
            end = int(input("Enter depth end: "))

            print("Sliced Array:")
            print(self.__arr[start:end])

    
    def mathematical_operations(self):

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = int(input("Enter your choice: "))

        second = np.array(
            list(map(float, input(
                "Enter second array elements separated by space: "
            ).split()))
        )

        if choice in [1, 2, 3, 4]:
            if second.size != self.__arr.size:
                print("Both arrays must have the same number of elements.")
                return

            second = second.reshape(self.__arr.shape)

            if choice == 1:
                print("Addition:", self.__arr + second)

            elif choice == 2:
                print("Subtraction:", self.__arr - second)

            elif choice == 3:
                print("Multiplication:", self.__arr * second)

            elif choice == 4:
                if np.any(second == 0):
                    print("Division by zero is not allowed.")
                else:
                    print("Division:", self.__arr / second)

        elif choice == 5:
            print(
                "Dot Product:",
                np.dot(self.__arr.flatten(), second.flatten())
            )

        elif choice == 6:
            if self.__arr.ndim != 2:
                print("Matrix multiplication requires a 2D array.")
                return

            if second.size != self.__arr.shape[1]:
                print("Invalid number of elements for matrix multiplication.")
                return

            rows = int(input("Enter rows of second matrix: "))

            if rows != self.__arr.shape[1]:
                print("Invalid matrix dimensions.")
                return

            second = second.reshape(rows, -1)

            if self.__arr.shape[1] == second.shape[0]:
                print("Matrix Multiplication:")
                print(np.matmul(self.__arr, second))
            else:
                print("Matrix dimensions do not match.")

        else:
            print("Invalid choice.")

    
    def combine_split(self):

        print("\n1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            if self.__arr.ndim == 1:
                second = np.array(list(map(
                    float,
                    input("Enter second array elements: ").split()
                )))

                result = np.concatenate((self.__arr, second))

            else:
                shape = self.__arr.shape

                if self.__arr.ndim == 2:
                    rows = int(input("Enter rows for second array: "))
                    size = rows * shape[1]
                    print("Enter", size, "elements:")
                    values = list(map(float, input().split()))
                    second = np.array(values).reshape(rows, shape[1])

                else:
                    depth = int(input("Enter depth for second array: "))
                    size = depth * shape[1] * shape[2]
                    print("Enter", size, "elements:")
                    values = list(map(float, input().split()))
                    second = np.array(values).reshape(
                        depth, shape[1], shape[2]
                    )

                result = np.concatenate(
                    (self.__arr, second), axis=0
                )

            print("Combined Array:")
            print(result)

        elif choice == 2:

            result = np.array_split(self.__arr, 2, axis=0)

            print("First Array:")
            print(result[0])

            print("Second Array:")
            print(result[1])

        else:
            print("Invalid choice.")

    
    def search_sort_filter(self):

        print("\n1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = float(input("Enter value to search: "))

            result = np.argwhere(self.__arr == value)

            if len(result) > 0:
                print("Value found at positions:")
                print(result)
            else:
                print("Value not found.")

        elif choice == 2:

            print("\n1. Ascending")
            print("2. Descending")

            order = int(input("Enter choice: "))

            result = np.sort(self.__arr, axis=-1)

            if order == 2:
                result = np.flip(result, axis=-1)

            print("Sorted Array:")
            print(result)

        elif choice == 3:

            value = float(input("Enter filter value: "))

            print("\n1. Greater than")
            print("2. Less than")
            print("3. Equal to")

            condition = int(input("Enter choice: "))

            if condition == 1:
                result = self.__arr[self.__arr > value]

            elif condition == 2:
                result = self.__arr[self.__arr < value]

            elif condition == 3:
                result = self.__arr[self.__arr == value]

            else:
                print("Invalid condition.")
                return

            print("Filtered Array:")
            print(result)

        else:
            print("Invalid choice.")

    
    def aggregates_statistics(self):

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.__arr))

        elif choice == 2:
            print("Mean:", np.mean(self.__arr))

        elif choice == 3:
            print("Median:", np.median(self.__arr))

        elif choice == 4:
            print("Standard Deviation:", np.std(self.__arr))

        elif choice == 5:
            print("Variance:", np.var(self.__arr))

        elif choice == 6:
            print("Minimum:", np.min(self.__arr))

        elif choice == 7:
            print("Maximum:", np.max(self.__arr))

        elif choice == 8:
            p = float(input("Enter percentile (0-100): "))
            if 0 <= p <= 100:
                print("Percentile:", np.percentile(self.__arr, p))
            else:
                print("Enter a value between 0 and 100.")

        elif choice == 9:
            second = np.array(list(map(
                float,
                input("Enter second array elements: ").split()
            )))

            if second.size == self.__arr.size:
                result = np.corrcoef(
                    self.__arr.flatten(),
                    second.flatten()
                )

                print("Correlation Coefficient:")
                print(result[0, 1])
            else:
                print("Both arrays must have the same number of elements.")

        else:
            print("Invalid choice.")



DataAnalytics.welcome()

obj = None

while True:

    print("\n========== MAIN MENU ==========")

    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("\nSelect Array Type:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        arr_choice = int(input("Enter your choice: "))

        if arr_choice == 1:

            values = list(map(float, input(
                "Enter array elements separated by space: "
            ).split()))

            arr = np.array(values)

        elif arr_choice == 2:

            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            values = list(map(float, input(
                "Enter array elements separated by space: "
            ).split()))

            if len(values) != rows * cols:
                print("Incorrect number of elements.")
                continue

            arr = np.array(values).reshape(rows, cols)

        elif arr_choice == 3:

            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            values = list(map(float, input(
                "Enter array elements separated by space: "
            ).split()))

            if len(values) != depth * rows * cols:
                print("Incorrect number of elements.")
                continue

            arr = np.array(values).reshape(depth, rows, cols)

        else:
            print("Invalid array choice.")
            continue

        obj = DataAnalytics(arr)

        print("\nArray created successfully!")
        obj.display()

        

        while True:

            print("\n1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            sub = int(input("Enter your choice: "))

            if sub == 1:
                obj.indexing()

            elif sub == 2:
                obj.slicing()

            elif sub == 3:
                break

            else:
                print("Invalid choice.")

    elif choice in [2, 3, 4, 5]:

        if obj is None:
            print("Please create an array first.")
            continue

        if choice == 2:
            obj.mathematical_operations()

        elif choice == 3:
            obj.combine_split()

        elif choice == 4:
            obj.search_sort_filter()

        elif choice == 5:
            obj.aggregates_statistics()

    elif choice == 6:

        print("\nThank you for using NumPy Analyzer!")
        print("Goodbye!")

        DataAnalytics.show_count()
        break

    else:
        print("Invalid choice. Please try again.")

    
