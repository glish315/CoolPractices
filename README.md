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


# Day 02/03
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

---


# Day 04/Weekend
---
## Task for the Intern: Setting Up and Configuring a Linux Server

### Objective of the Task
The goal is to gain practical knowledge in managing a Linux server, configuring basic network services, and implementing DevOps tools such as web servers, Jenkins, and integration with GitHub.

### Scope of the Task

1. Basic Server Configuration
    - Update the operating system.
    - Create a new user with administrative privileges.
    - Configure a basic firewall.
2. Domain Configuration
    - Connect the domain to the server by setting the appropriate DNS records.
    - Configure an SSL certificate for the domain using Let's Encrypt.
3. Installation and Configuration of the Web Server
    - Install and configure Apache or Nginx as the web server.
    - Configure virtual hosts for the selected domain. (The domain will be provided to you.)
4. Installation and Configuration of Jenkins
    - Install Jenkins on the server.
    - Configure basic Jenkins settings, including access via a web browser.
    - Open the appropriate ports in the firewall to allow access to Jenkins.
5. Connecting Jenkins to GitHub
    - Create an SSH key for the Jenkins user and configure it in the GitHub repository.
    - Create a new pipeline in Jenkins that will clone the code from the selected GitHub repository.
6. Testing
    - Check if the website hosted on the web server is accessible via the domain.
    - Run the pipeline in Jenkins and confirm that the code has been correctly cloned from the GitHub repository.

---


# Day 05/06
---
## Day off

### I worked on [Lisp-language](https://github.com/glish315/Lisp-language)

---


# Day 07
---
## Automated Triggers for Git Actions

### Scope of the Task

1. After Push
    - Create a Jenkins job that has a post-build action set as a trigger to activate automatically after a git push event.

2. After PR
    - Create another Jenkins job that has a post-build action set as a trigger to activate automatically after a pull request.

---


# Day 08/09
---
## Database and domains

### Scope of Task

1. Set up WordPress on your main domain, and configure MySQL using PHPMyAdmin.
    
2. Set up Jenkins on a subdomain. 

---


# Day 10/11
---
## Fixing the server

### There was a big issue with a server, so i must do everythink from 0.

---


# Day 12
---
## After fixing the server

### Configure my webiste with wordpress.

---

# Day 13
---
## Day off

### Learing the C language.

---


# Day 14
---
## Tor

### Trying to set up my website on tor (for fun).

---

