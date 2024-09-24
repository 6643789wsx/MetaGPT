# -*- coding: utf-8 -*-
# @Date    : 6/26/2024 17:07 PM
# @Author  : didi
# @Desc    : prompts of operators

GENERATE_PROMPT = """
Generate Solution for the following problem: {problem_description}
"""

CONTEXTUAL_GENERATE_PROMPT = """
Generate Solution for the following problem: 

## Problem Description
{problem_description}

## Thought
{thought}
"""

GENERATE_CODE_SOLUTION_PROMPT = """
You are given a code contest problem, and a self-reflection on the problem:

### Problem Description
{problem_description}

### self reflection on the problem
{rephrase_problem}

Your goal is to come up with a possible text solution to the code contest problem.

Guidelines:
- Make sure solution fully addresses the problem goals, constraints, examples, and notes.
- Each solution must have reasonable runtime and memory complexity - less than three seconds on a modern computer, given the problem constraints for large inputs.
- Double-check the solutions. Each possible solution must be able to generalize to additional test cases, not just the ones provided in the problem description.
"""

CODE_CONTEXTUAL_GENERATE_PROMPT = """
Please provide a self-contained  Python script that solves the following problem in a markdown code block:

### Problem Description
{problem_description}

### reflection and possible solution on the problem
{thought}

When writing python script:
1. Consider all edge cases and boundary conditions.
2. Avoid oversimplification - address all aspects of the problem.
3. Ensure your logic covers all stated requirements.
4. Avoid adding additional test cases beyond those provided in the problem description.
"""

GENERATE_CODEBLOCK_PROMPT = """
Please provide a self-contained  Python script that solves the following problem in a markdown code block:

{problem_description}

When creating your solution:
1. Consider all edge cases and boundary conditions.
2. Avoid oversimplification - address all aspects of the problem.
3. Ensure your logic covers all stated requirements.
4. Avoid adding additional test cases beyond those provided in the problem description.
"""

GENERATE_ON_CONTEXT_PROMPT = """
Please generate a solution for the following problem based on the provided context:

### Problem Description
{problem_description}

### Context
{context}
"""

FORMAT_PROMPT = """
For the question described as {problem_description},
please extract a short and concise answer contains only one word/few words from the following solution: {solution}.
Make sure there are no additional comments or explanations in your response.
"""

REVIEW_PROMPT = """
For the question described as {problem_description},
please review the following solution: {solution}, and provide a review result in boolean format.
```
You will be reviewing the problem-solving process of another AI assistant that has answered a mathematical question. Your task is to evaluate the solution and provide a detailed review for refinement. Follow these steps:
<step1>
Carefully read through the original question and entire solution, paying close attention to the relevant concepts, thinking process, calculations, and final result. Assess whether the solution is clear, logical, and well-organized. Write your initial review in <initialReview> tags.
</step1>
<step2>
Evaluate the reasoning and logic behind the solution. Ensure that the thinking process is clear, coherent, and mathematically sound. If you find any areas that need clarification or improvement, provide your suggestions inside <reasoningFeedback> tags.
</step2>
<step3>
Re-do the calculations presented in the <calculation> section **carefully and step-by-step** to verify the accuracy. Break down the calculations into the simplest possible steps and check each step for errors. You must not be careless and treat every part with rigor. Don't neglect checking any calculation part of the solution process. If you find any mistakes, note them down inside <calculationErrors> tags.
</step3>
<step4>
Provide an overall assessment of the solution's thoroughness, accuracy, and clarity inside <overallAssessment> tags. Highlight the strengths and weaknesses of the solution and offer suggestions for improvement, if any.
</step4>
use XML tags to present your complete evaluation, including initial review, calculation errors, reasoning feedback, and overall assessment, in a well-organized and easy-to-follow format.
Remember to be thorough, constructive, and professional in your review. Your goal is to help improve the quality and accuracy of the mathematical problem-solving process.
```
If you believe the solution is capable of resolving the issue, return True; otherwise, return False, and include your comments
"""

REVISE_PROMPT = """
For the question described as {problem_description},
please evaluate and revise the solution provided: {solution}, taking into account the review feedbacks: {feedback}."
Then output the revised solution.
"""

FU_ENSEMBLE_PROMPT = """
### Given problem

{problem_description}

### We've got a list of solutions

<solutions>
{solutions}
</solutions>

### Instructions
Based on the given problem and solution candidates:

1. Analyze the pros and cons of each candidate solution
2. Consider how to integrate reasonable parts from different solutions
3. Formulate a more comprehensive and effective solution
"""

MD_ENSEMBLE_PROMPT = """
You are given a problem:
{problem_description}

Here is a list of possible solutions to the problem:
{solutions}

Using the inputs above, your goal is to choose the best solution to the problem.
The main consideration is that the solution can fully solve the problem in a correct and robust manner.
Provide your final decision by writing the chosen solution letter.

Please follow the required format in your response.
"""

SC_ENSEMBLE_PROMPT = """
I have generated the following solutions to the question: {problem_description}

{solutions}

Evaluate these solutions.
Select the most consistent solution based on majority consensus.
Give your answer with a single id of solution (without anything else).
"""

REPHRASE_ON_PROBLEM_PROMPT = """
You are given a code contest problem:

### problem
{problem_description}

### instrcutions
Given the problem, Your Goal is:
Reflect on the problem, and describe it in your own words, in bullet points. Pay attention to small details, nuances, notes and examples in the problem description.
"""

REPHRASE_ON_CODE_PROMPT = """
You are given a code contest problem:

### problem
{problem_description}

### instrcutions
Given the code contest problem, Your Goal is:
Reflect on the problem, and describe it in your own words, in bullet points. Pay attention to small details, nuances, notes and examples in the problem description.
"""

REFLECTION_ON_PUBLIC_TEST_PROMPT = """
You are given a code contest problem, and a self-reflection on the problem: 
### problem
{problem_description}


### self reflection on the problem
{rephrase_problem}


A Python code solution was generated for the problem:
### Code Solution
{code_solution}


This section of the code execution result is
### Execution Result
{exec_pass}


However, when running the following input example, the code solution above failed to produce the expected output:
#### Failed Test Case
{test_fail}

Your goal is to analyze the code solution and the error, and propose a fixed code which will produce the expected output for the provided test input.
The fixed code should keep the solution robust, and work for all other input examples as well.
Make sure the fixed code has a reasonable runtime - less than three seconds on a modern computer, given the problem constraints for large input.
"""

PYTHON_CODE_VERIFIER_PROMPT = """You are a professional Python programmer. Your task is to write Python code based on the user's request. Make sure to add appropriate explanations and your personal thought process to your code. Additionally, all code should be encapsulated in Python code blocks.

The packages you can use include: numpy, scipy, pandas, sympy, statsmodels, scikit-learn. If you attempt to import another external package and encounter an error, do not say it cannot be imported. Instead, try to write new code that avoids this issue.

Always output complete code rather than just giving suggestions or partial modifications, as your code will be executed directly. If immediate execution is required to check for possible errors, include test cases in the code.

In your response, only the code that needs to be run should be wrapped in multi-line code blocks. No other multi-line code blocks should appear. Your code needs to print the output after execution. Your code should not print error messages.

Problem description: {problem}
Please write Python code to solve this problem.
"""
