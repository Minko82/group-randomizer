# 🎲 Random Group Generator

Takes a list of items, **shuffles them**, and splits them into a set number of groups. 

<br>

---

## 🚀 How It Works
1. **Enter a list of items** (separated by spaces).
2. **Enter the number of groups** you want.
3. The script:
   - **Shuffles** the list using the **Fisher-Yates shuffle (Knuth Shuffle)** to ensure randomness.
   - **Splits** the items into groups using a **round-robin method** (cycling through groups one by one).
   - **Prints the final groups**.

<br>

---

## ▶ How to Use
Make sure you have **Python 3** installed.

1️⃣ Run the script:
```sh
python3 group-generator.py
```

<br>

---
## 💡 Notes

### 📌 Splitting the Input (split())
- The split() method splits a string into a list with spaces as the default separator
  - You can also specify the separator, like this: split(','), split(';'), etc.
 
  Example:
  ```vbnet
    Input:  "Alice Bob Charlie"
    Output: ["Alice", "Bob", "Charlie"]
  ```

<br>

### 📌 Randomizing the List (random.shuffle())
- The script shuffles the list using the **Fisher-Yates shuffle**
- This ensures true randomness
  
<br>

### 📌 Enumerate()
- Enumerate is a built-in function that iterates over a list while providing both the index and the item


<br>

### 📌 Round-Robin Method
- The **Round-Robin method** evenly distributes items by cycling through a list and starting over once it reaches the end.

- Example: Handing out 6 slices into 3 pizza boxes:
  -   1️⃣ First slice → Box 1
  -   2️⃣ Second slice → Box 2
  -   3️⃣ Third slice → Box 3
  -   4️⃣ Fourth slice → Back to Box 1

<br>

**In this context...**

| **Person**  | **Index** | **Group (Index % 3)** | **Assigned to** |
|------------|---------|-------------------|--------------|
| Charlie    | 0       | `0 % 3 → 0`       | Group 1      |
| Eve        | 1       | `1 % 3 → 1`       | Group 2      |
| Bob        | 2       | `2 % 3 → 2`       | Group 3      |
| Dave       | 3       | `3 % 3 → 0`       | Group 1      |
| Alice      | 4       | `4 % 3 → 1`       | Group 2      |
| Frank      | 5       | `5 % 3 → 2`       | Group 3      |


