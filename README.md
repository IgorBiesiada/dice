# 🎲 Dice Roller - Simulate Your Tabletop Dice Rolls!

A Python-based dice rolling simulator perfect for tabletop games like RPGs or board games. This function parses and processes dice roll commands in a flexible format such as `xDy+z` to deliver results quickly and accurately.

---

## 🚀 Features

- **Supports Popular Dice Types:** D3, D4, D6, D8, D10, D12, D20, D100.
- **Flexible Input Format:**
  - `xDy+z` where:
    - `x` → Number of rolls (optional; defaults to 1).
    - `y` → Dice type (e.g., D6, D20).
    - `z` → Modifier (optional; positive or negative).
- **Examples of Commands:**
  - `D6` → Roll a single 6-sided die.
  - `2D10+5` → Roll two 10-sided dice, then add 5.
  - `D20-3` → Roll one 20-sided die, then subtract 3.
- **Error Handling:** Identifies and reports invalid inputs like unsupported dice types or incorrectly formatted commands.

---

## 🛠 Installation

1. Clone the repository or copy the function code into your project.
2. Install Python (version 3.7 or higher recommended).
3. Ready to roll—no additional dependencies needed!

---

## 📖 Usage

### Function Definition
```python
def dice(dice_code: str) -> dict | str
