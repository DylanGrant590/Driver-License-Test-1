# Jamaican Driver's Licence Test

A console-based Python quiz application modelled after the Jamaican Driver's Licence written exam. The program walks the user through 20 questions, scores their responses, and provides a breakdown of incorrect answers by category.

## Features

- 20 questions drawn from the Jamaican Road Code
- Case-insensitive answer matching
- Score and percentage displayed at the end
- Pass/fail result based on the official 75% threshold
- Category breakdown of wrong answers (Road Rules, Right of Way, Safety, Terminology, Parking)

## Requirements

- Python 3.x
- No external libraries required

## Usage

```bash
python Test.py
```

You will be prompted to begin the test, then asked each question one at a time. At the end, your score, percentage, and any weak areas are displayed.

## Example Output

```
----------------------------------------------
Welcome to the Jamaican Driver's License Test!
----------------------------------------------

There are 20 questions. You need 75% to pass.

Would you like to begin the test? (yes/no): yes

Okay, let's begin.

Q1: The driver of any motor vehicle, when traveling down a hill, must not coast
with the gears or transmission of the vehicle in neutral. True or False?
Your answer: true
Correct!

...

----------------------------------------------
You got 16/20 correct (80.0%)
Result: PASSED

Areas to review:
  Right of Way: 2 wrong
  Terminology: 1 wrong
  Safety: 1 wrong
----------------------------------------------
```

## Project Structure

```
Driver-License-Test-1/
│
├── Test.py       # Main application
└── README.md     
```

## Author

Dylan Grant — [GitHub](https://github.com/DylanGrant590)
