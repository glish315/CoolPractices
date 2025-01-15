# Day 01 
---
## Programming Tasks

1. **Very simple: Print greeting**: Write a function `greet(name)` that returns the string: "Hello, [name]!". [1.py](https://github.com/glish315/internships/tree/main/day01/Python/1.py)

2. **Simple: Reversing text**: Write a function `reverse_string(s)` that reverses the given string.  [2.py](https://github.com/glish315/internships/tree/main/day01/Python/2.py)

    **INPUT:** '123456'  **OUTPUT:** '654321' 

4. **Easy: Even numbers in a range**: Write a function `count_even_numbers(start, end)` that returns the number of even numbers in the given range. [3.py](https://github.com/glish315/internships/tree/main/day01/Python/3.py)

5. **Medium: Bracket validation**: Write a function `is_valid_brackets(s)` that checks the validity of a string of brackets.   [4.py](https://github.com/glish315/internships/tree/main/day01/Python/4.py)
  `is_valid_brackets("()[]{}")`  
  `is_valid_brackets("([]}")`

6. **Hard: Sorting algorithm (QuickSort)**: Write a function `quick_sort(array)` that implements the QuickSort algorithm. [5.py](https://github.com/glish315/internships/tree/main/day01/Python/5.py)

---
## Git Tasks
For the tasks related to Git, I want to know what commands you use; if something can be done through the UI, that's fine, but I want to know the console commands.

- **Basic: Creating a repository**: Create a local repository.  
  Add a `README.md` file with the content: `# My Repository`.  
  Make a commit and link the repository to GitHub.

- **Easy: Working with branches**: Create a new branch called `feature`.  
  Add a file `feature.txt` with the content: `New feature`.  
  Merge the feature branch into main. (How to do this?) [feature.txt](https://github.com/glish315/internships/blob/main/day01/feature.txt)

- **Hard: Resolving a merge conflict**: Create a feature branch.  
  In the file `conflict.txt`, add different content in the main and feature branches.  
  Perform a merge and resolve the conflict manually. [conflict.txt](https://github.com/glish315/internships/blob/main/day01/conflict.txt)

---


# Day 02
---
## Simple Web Scraper

**Description:** Create a script that retrieves data from a selected website (e.g., article titles from a blog). The program should:
- Use the `requests` library to fetch data.
- Parse HTML using `BeautifulSoup` and extract headers (e.g., `<h2>`).
- Save the retrieved data to a text file.

**Tip:** Ensure proper handling of HTTP errors and appropriate HTML parsing.

---
## Mini Project: Logic Game

**Description:** Create a "Hangman" game in Python:
- The game randomly selects a word from a text file (e.g., `words.txt`).
- The user has 6 attempts to guess the entire word by providing single letters.
- The game displays progress (e.g., `_ _ a _ _`), the number of remaining attempts, and the letters used.
- After winning/losing, the game should offer the option to restart.



