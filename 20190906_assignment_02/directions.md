# Assignment 02: Input & Output
## Date: September 6, 2019

**Note:** All python programs and text files should start with:
~~~
Assignment #02
Your Name
Today's Date
~~~
as either text or comments.

**Directions:** Complete the following exercise, then answer each of the questions (question answers should be written in a separate *answers.txt* file).
1. Write the program [quadratic.py] which will prompt the user for the values of *a*, *b*, and *c* and output the solutions to the quadratic function: $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Hint:** Use *float()* to convert the text input from a user to a floating point value.

*If you want the above formula to display properly, you should install the "Markdown Enhanced Preview" extension in Visual Studio Code.*

**Questions:**

1. What does python do if you provide the value 0 for *a*?
2. What does python do if $b^2 - 4ac < 0$?
3. What does python do if you provide a value for *a*, *b*, or *c* that cannot be converted to a number?
4. Handling each of the above problems is an aspect of **data validation**. This is the process of ensuring data meets general specifications for a problem. Why is this process important when creating programs such as this one?

**Submission:**
To submit your solution, remember that you should be working in the git-initialized folder created last assignment. You can then use the following commands:
~~~
git add .
~~~
~~~
git commit -m "Complete Assignment #02."
~~~
~~~
git push origin name
~~~
*name should be replaced with the name of your repository (your last name)*