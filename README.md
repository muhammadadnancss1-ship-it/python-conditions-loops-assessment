# Python Conditions & Loops Assessment

Two beginner-friendly, **console-based Python applications** built for a programming assessment. They demonstrate how conditional statements control decisions and how loops, counters, and accumulators process multiple records in realistic scenarios.

- **Task 1 — Student Scholarship Eligibility System:** Evaluates a student's marks, attendance, and family income to determine scholarship eligibility.
- **Task 2 — Smart Pharmacy Inventory & Sales Management System:** Processes medicine sales, checks stock availability, calculates revenue, and identifies medicines needing restocking.

Both programs run separately and use standard Python only. **No third-party packages or databases are required.**

## Repository Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Requirements

- Python 3.8 or later
- A terminal (PowerShell, Command Prompt, macOS Terminal, or Linux terminal)
- Optional: Visual Studio Code or another text editor

## Task 1: Student Scholarship Eligibility System

### Purpose

The university needs a simple way to assess whether a student qualifies for a full scholarship, a partial scholarship, or no scholarship. The program collects student information, validates it, applies the university's eligibility rules, and displays a report with the decision and reasons for ineligibility.

### Information Collected

1. Student name
2. Academic marks (percentage)
3. Attendance (percentage)
4. Monthly family income (Pakistani rupees)

### Eligibility Rules

**All three basic requirements must be met:**

| Requirement | Eligibility threshold |
| --- | --- |
| Academic marks | At least **80%** |
| Attendance | At least **85%** |
| Monthly family income | **Rs. 50,000 or less** |

After all three requirements pass, the scholarship category depends on academic marks:

| Marks | Scholarship decision |
| --- | --- |
| 90% or above | Full Scholarship |
| 80% to below 90% | Partial Scholarship |
| Below 80% | Not Eligible |

**Important:** High marks alone do not guarantee a scholarship. Students must also satisfy the attendance and income requirements. An income **above** Rs. 50,000 is valid input but causes **ineligibility**. For decimal percentages, 89.5% qualifies for a partial scholarship, not a full scholarship.

### Validation and Decision Logic

- Student name must not be empty.
- Marks and attendance must each be numeric percentages between 0 and 100, inclusive.
- Family income must be a non-negative, finite number.
- Non-numeric inputs are handled with `try/except`.
- `if`, `elif`, and `else` validate the inputs; `and` checks whether all scholarship conditions pass.
- When a requirement fails, the report explains **each unmet requirement**.

### Example Execution — Not Eligible

```text
=============== SCHOLARSHIP EVALUATION ===============
Enter the student name: adan
Enter student marks in percentage: 85
Enter attendance percentage: 45
Enter monthly family income (Rs.): 50000

========== SCHOLARSHIP EVALUATION REPORT ==========
Student Name: adan
Academic Marks: 85.00%
Attendance: 45.00%
Monthly Family Income: Rs. 50000.00

Eligibility Evaluation:
- Attendance is below the required 85%.

Scholarship Result: Not Eligible
```

In this example, the student fails because attendance is below 85%, even though marks and family income meet their thresholds.

### Example Execution — Full Scholarship

```text
=============== SCHOLARSHIP EVALUATION ===============
Enter the student name: Muhammad Adnan
Enter student marks in percentage: 90
Enter attendance percentage: 89
Enter monthly family income (Rs.): 43000

========== SCHOLARSHIP EVALUATION REPORT ==========
Student Name: Muhammad Adnan
Academic Marks: 90.00%
Attendance: 89.00%
Monthly Family Income: Rs. 43000.00

Eligibility Evaluation:
- All three eligibility requirements are satisfied.

Scholarship Result: Full Scholarship
```

## Task 2: Smart Pharmacy Inventory & Sales Management System

### Purpose

The pharmacy wants to record daily medicine sales, prevent sales beyond available inventory, calculate revenue, track remaining stock, and warn the operator when medicines need restocking.

### Information Collected for Each Medicine

1. Medicine name
2. Available stock (whole units)
3. Price per unit (Rs.)
4. Requested sale quantity (whole units)

The program first asks how many medicines to process, then uses `for` with `range()` to repeat the input and sales checks for each one.

### Sale and Inventory Rules

| Situation | Program behavior |
| --- | --- |
| Requested quantity is less than or equal to available stock | Approve the sale |
| Requested quantity exceeds available stock | Reject the sale; keep stock unchanged |
| Approved sale | Sales amount = quantity sold × price per unit |
| Approved sale | Remaining stock = available stock − quantity sold |
| Remaining stock is below 10 units | Display a warning and increase the restocking counter |
| Approved sale | Add the sales amount to total pharmacy revenue |
| Rejected sale | Add **nothing** to revenue |

A medicine with fewer than 10 units **already in stock** is counted as needing restocking even if its requested sale was rejected. Each valid medicine entry contributes at most once to the restocking counter.

### Validation and Counting Rules

- The number of medicines must be a positive whole number.
- Medicine names cannot be blank.
- Available stock and sale quantity must be non-negative whole numbers.
- Unit price must be a non-negative, finite number.
- Invalid medicine entries are skipped with a message using `continue`; subsequent entries still run.
- **Total Medicines Processed** counts valid medicine records, including records whose sales are rejected due to insufficient stock. It does not count invalid/skipped entries.
- The revenue accumulator begins at zero and increases only for accepted sales.

### Example Execution — Five Medicines

The following example uses the five-medicine test scenario supplied during development.

```text
========== SMART PHARMACY SYSTEM ==========
How many medicines do you want to process? 5

========== MEDICINE 1 ==========
Enter medicine name: penadol
Enter available stock: 50
Enter price per unit (Rs.): 150
Enter quantity sold: 10

Sale Successful!
Medicine: penadol
Sales Amount: Rs. 1500.00
Remaining Stock: 40

========== MEDICINE 2 ==========
Enter medicine name: Mogral
Enter available stock: 50
Enter price per unit (Rs.): 300
Enter quantity sold: 5

Sale Successful!
Medicine: Mogral
Sales Amount: Rs. 1500.00
Remaining Stock: 45

========== MEDICINE 3 ==========
Enter medicine name: dawtor
Enter available stock: 56
Enter price per unit (Rs.): 200
Enter quantity sold: 9

Sale Successful!
Medicine: dawtor
Sales Amount: Rs. 1800.00
Remaining Stock: 47

========== MEDICINE 4 ==========
Enter medicine name: baydall
Enter available stock: 10
Enter price per unit (Rs.): 20
Enter quantity sold: 3

Sale Successful!
Medicine: baydall
Sales Amount: Rs. 60.00
Remaining Stock: 7
WARNING: baydall requires restocking!

========== MEDICINE 5 ==========
Enter medicine name: extore
Enter available stock: 45
Enter price per unit (Rs.): 23
Enter quantity sold: 25

Sale Successful!
Medicine: extore
Sales Amount: Rs. 575.00
Remaining Stock: 20

========== FINAL PHARMACY REPORT ==========
Total Medicines Processed: 5
Total Pharmacy Revenue: Rs. 5435.00
Medicines Requiring Restocking: 1
==========================================
```

**Revenue calculation:** Rs. 1,500 + Rs. 1,500 + Rs. 1,800 + Rs. 60 + Rs. 575 = **Rs. 5,435**. Only `baydall` has remaining stock below 10 units, so the restocking count is **1**.

### Additional Scenario — Insufficient Stock

For a medicine with **8 units in stock** and **12 units requested**, the sale is rejected. The stock stays at 8, no revenue is added, and a restocking warning appears because 8 is below 10.

```text
Sale Rejected!
Reason: Insufficient stock.
Available Stock: 8
Requested Quantity: 12
Remaining Stock: 8
WARNING: Augmentin requires restocking!
```

## Python Concepts and Techniques

| Concept | Where it is used | Why it matters |
| --- | --- | --- |
| `input()` and `print()` | Both programs | Accept input and display information |
| `int()` and `float()` | Both programs | Convert input to numeric data |
| `if`, `elif`, `else` | Both programs | Handle validation and eligibility/sale decisions |
| Comparison operators (`>=`, `<=`, `<`, `>`) | Both programs | Evaluate marks, income, attendance, and stock thresholds |
| Logical operators (`and`, `or`, `not`) | Both programs | Combine conditions or explain failed checks |
| `for` and `range()` | Pharmacy | Process the requested number of medicines |
| Counter using `+= 1` | Pharmacy | Count processed and restocking medicines |
| Accumulator using `+=` | Pharmacy | Track total sales revenue |
| `continue` | Pharmacy | Skip an invalid medicine record |
| `try/except ValueError` | Both programs | Handle non-numeric input gracefully |
| Arithmetic operators | Pharmacy | Calculate sales values and remaining stock |
| f-strings and `:.2f` | Both programs | Format printed values and currency |
| `math.isfinite()` | Both programs | Reject non-finite numbers such as `nan` and `inf` |

## How to Run the Programs

### 1. Download or Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-conditions-loops-assessment.git
cd python-conditions-loops-assessment
```

Replace `YOUR_USERNAME` with your own GitHub username. Alternatively, download the repository ZIP, extract it, and open a terminal inside the extracted folder.

### 2. Check Python Installation

```bash
python --version
```

On some computers use `python3 --version` or, on Windows, `py --version`.

### 3. Run Task 1

```bash
python student_scholarship_system.py
```

### 4. Run Task 2

```bash
python pharmacy_inventory_system.py
```

Use `python3` on systems where `python` is unavailable, or `py` on Windows where that launcher is configured.

**Example using Windows PowerShell in VS Code:**

```powershell
cd E:\Python\python_week_01\python-conditions-loops-assessment
python student_scholarship_system.py
python pharmacy_inventory_system.py
```

Run each program separately and follow the prompts. These examples assume the project folder is saved at the location shown; change the path if needed.

## Suggested Test Cases

### Task 1 — Scholarship

| Marks | Attendance | Income (Rs.) | Expected outcome |
| --- | --- | --- | --- |
| 90 | 89 | 43,000 | Full Scholarship |
| 85 | 90 | 40,000 | Partial Scholarship |
| 85 | 45 | 50,000 | Not Eligible — attendance too low |
| 95 | 90 | 60,000 | Not Eligible — income too high |
| 79 | 90 | 30,000 | Not Eligible — marks too low |
| 80 | 85 | 50,000 | Partial Scholarship — boundary case |
| 101 | 90 | 40,000 | Invalid marks |

### Task 2 — Pharmacy

| Available stock | Unit price (Rs.) | Requested quantity | Expected result |
| --- | --- | --- | --- |
| 50 | 150 | 10 | Sale of Rs. 1,500; 40 units left |
| 10 | 20 | 3 | Sale of Rs. 60; 7 left; restock warning |
| 8 | 200 | 12 | Sale rejected; 8 left; restock warning |
| 10 | 20 | 0 | Sale of Rs. 0; 10 left; no warning |
| −5 | 20 | 2 | Invalid record; skipped |

**Boundary note:** Low stock is strictly **below 10**, so 10 remaining units do not trigger a warning. A requested quantity equal to available stock is permitted and leaves zero units.

## Development Notes and Scope

- Both programs are standalone Python command-line exercises, not graphical applications.
- They calculate results for the current execution only; they do **not** use a database or save records between runs.
- The pharmacy program assumes stock values entered for each medicine are current and does not maintain a persistent inventory catalogue.
- The assignment focuses on foundational Python rather than production billing, authentication, or real pharmacy regulation.
- Example medicine names and prices are illustrative test data, not live pharmacy pricing.

## GitHub Upload and Submission

1. Sign in to GitHub and create a **new public repository** named `python-conditions-loops-assessment` (or make it accessible to your evaluator as required).
2. Place the two `.py` files and this `README.md` at the root of the repository.
3. Open a terminal in the project folder and run:

   ```bash
   git init
   git add student_scholarship_system.py pharmacy_inventory_system.py README.md
   git commit -m "Complete Python conditions and loops assessment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/python-conditions-loops-assessment.git
   git push -u origin main
   ```

4. Replace `YOUR_USERNAME` with your actual GitHub username. If the repository was already cloned, use its existing Git configuration rather than initializing or adding the remote again.
5. Open the repository in your browser, confirm that all three files are visible, and verify that `README.md` displays correctly.
6. Submit the GitHub repository URL and the three required files through the LMS.

### Submission Checklist

- [ ] `student_scholarship_system.py` exists and runs.
- [ ] `pharmacy_inventory_system.py` exists and runs.
- [ ] `README.md` includes descriptions, concepts, run instructions, and sample outputs.
- [ ] Scholarship conditions and rejection reasons have been tested.
- [ ] Pharmacy successful/rejected sales, revenue totals, and restock warnings have been tested.
- [ ] The GitHub repository contains the latest versions of all files.
- [ ] The repository URL works for the evaluator.
- [ ] The repository URL and all three source/documentation files are submitted to the LMS.

---

**Assessment focus:** Conditional statements, loops, comparisons, logical operators, input validation, counters, accumulators, and clear console output.
