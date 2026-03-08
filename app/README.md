

# Pi Digit Calculator

**Live Preview** — https://pidigitcalculator.vercel.app

**GitHub Repo** — https://github.com/nishchup489-afk/pidigitcalculator

---

## Project 1 of 100 Python Live Projects

This project calculates **π to the Nth decimal place** using Python.

It started as a raw **CLI math experiment** and later evolved into a small **FastAPI web application** with a user interface. The goal was not just to print a number, but to understand:

- which methods work
- which methods fail
- why floating point precision becomes a problem
- why high precision arithmetic is necessary for serious π calculation

So this project is not just a calculator. It is a small journey through **algorithm choice, numerical limits, backend integration, and precision handling**.

---

## What this project contains

This project has **two forms**:

### 1. CLI version

If you only want the raw Python logic, go to `sample.py` in the GitHub repository.

That file focuses on the mathematical side of the project without the web layer.

### 2. Website version

The website version takes input from the user, sends it to a FastAPI backend, runs the π calculation in Python, and renders the result in the browser using Jinja templating.

---

## Stack used

- **Python 3.14.0**
- **FastAPI 0.135.1**  
  Used for the website version. Flask could also be used. FastAPI was chosen for practice.
- **HTML**
- **Tailwind CSS via browser CDN**  
  Optional. Normal CSS would also work.
- **Poetry**  
  Used for environment and dependency practice. A normal `venv` setup is also fine.
- **Vercel**  
  Used for deployment.

---

## If you only want the raw Python version

Go to `sample.py` in the GitHub repository.

You can either:

- open it directly in the repo
- clone the project
- run `sample.py` from the terminal

---

# Code journey

This project did not begin with the final solution immediately.

Three different methods were tried in `sample.py`.

That matters, because this project is not only about getting an output. It is also about understanding **why some methods are limited** and why the final method is the correct one for this goal.

---

## Method 1 — Bailey–Borwein–Plouffe formula (BBP formula)

Formula:

```text
π = Σ from k = 0 to ∞ of (1 / 16^k) × (4 / (8k + 1) - 2 / (8k + 4) - 1 / (8k + 5) - 1 / (8k + 6))
```

This was one of the first methods attempted.

### Idea

* take input `n`
* create a loop
* apply the BBP formula in each iteration
* sum all the values

### What was attempted

* user gives input `n`
* loop runs through terms
* each term is computed using the formula
* all values are added together

### Problem

In this implementation, it did not give the level of precision needed for deeper π calculation.

It was interesting mathematically, but for this project it was not the most practical choice for large precision output.

### Verdict

Good for experimentation.
Not the final solution for serious high precision π calculation in this project.

---

## Method 2 — Using Python built-in `math.pi`

This method is simple.

Example:

```python
f"{math.pi:.{n}f}"
```

### Idea

* import `math`
* use `math.pi`
* format it up to the Nth decimal place

### Problem

This looks flexible, but the underlying value of `math.pi` is still limited by Python floating point precision.

That means formatting it to more digits does **not** magically create more true precision. It only displays what already exists inside the float.

### Verdict

Useful for small display tasks.
Not good for real high precision π calculation.

---

## Method 3 — Chudnovsky algorithm

Formula:

```text
1 / π = 12 × Σ from k = 0 to ∞ of [((-1)^k × (6k)! × (545140134k + 13591409)) / ((3k)! × (k!)^3 × 640320^(3k + 3/2))]
```

This is the method that solved the actual problem.

The **Chudnovsky algorithm** is famous because it converges very fast. Each iteration contributes about **14.18 correct digits of π**.

That makes it much more practical than the previous methods.

### Why it works better

* fast convergence
* fewer iterations needed
* suitable for high precision π calculation

### Important note

Normal data types like:

* `float`
* standard floating point values

cannot safely handle that many digits for this kind of calculation.

So high precision arithmetic is required.

Two common choices are:

* `gmpy`
* `Decimal`

This project uses **Decimal** because it is easier to understand and already available in Python’s standard library.

### Verdict

This became the final method because it is fast, precise, and suitable for the real goal of the project.

---

# Why Decimal is required

The project uses Python’s `Decimal` module.

Example:

```python
getcontext().prec = n + 20
```

## What precision means

Precision means how many significant digits `Decimal` is allowed to keep during internal calculation.

This matters because if the precision is too low:

* the result rounds too early
* the later digits become wrong
* output may look precise but actually be false

So in this project, precision is set to:

```python
n + 20
```

That extra buffer gives the algorithm room to compute safely before trimming the final output to the user’s requested digit count.

That buffer is not random decoration. It is necessary.

---

# Why factorial is used

The Chudnovsky formula contains factorial-heavy terms such as:

* `(6k)!`
* `(3k)!`
* `(k!)³`

So Python’s built-in factorial function is used:

```python
from math import factorial
```

This is clean, readable, and reliable.

No need to reinvent factorial logic when the standard library already does the job properly.

---

# Algorithm flow in plain language

The project works like this:

### Step 1 — Take input

The user enters `n`, meaning how many decimal places of π they want.

### Step 2 — Set precision

Decimal precision is raised to:

```python
n + 20
```

so internal calculations stay accurate.

### Step 3 — Estimate the number of iterations

Each Chudnovsky iteration gives about **14.18 digits**.

So the program estimates how many terms are needed using:

```python
iterations = (n // 14) + 1
```

This is the practical idea.

### Step 4 — Compute π

The formula is applied term by term.

### Step 5 — Trim the result

After calculation, the result is formatted or sliced to exactly the requested number of decimal places.

---

# Iteration logic intuition

Because each Chudnovsky iteration gives about **14.18 digits**, the program does not need to loop blindly forever.

It estimates the number of needed terms based on the requested precision.

Practical version:

```python
iterations = (n // 14) + 1
```

That is the clean explanation.

---

# Website integration with FastAPI

After the CLI version worked, the project was expanded into a small web application using **FastAPI**.

The user enters a number in an HTML form.

That value is sent to a FastAPI route using a `POST` request.

The backend then:

* receives the form data
* runs the Chudnovsky function
* returns the result to the template

### Flow

```text
User → HTML form → FastAPI route → Python algorithm → template response
```

This made the project more usable than a terminal-only script.

---

## Example FastAPI route

```python
@app.post("/calc", response_class=HTMLResponse)
async def calc(request: Request, user_input: int = Form(...)):
    result = chudnovsky(user_input)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )
```

---

## Example HTML form

```html
<form action="/calc" method="post">
    <input type="number" name="user_input">
    <button type="submit">Calculate</button>
</form>
```

The browser sends the value. FastAPI receives it. Python calculates π. The template shows the result.

---

# About page

The project also includes an `/about` page.

This page exists for the same reason a good README exists:

because code alone is not enough.

A proper project should explain:

* what the project does
* which methods were tried
* which problems appeared
* why the final solution was chosen
* how the web implementation works

So the about page is basically the project story and technical explanation placed inside the app itself.

---

# Caution

Requesting too many digits can put heavy pressure on the CPU.

High precision math is expensive.

The more digits requested, the more computation is required.

So yes, π is beautiful, but it can absolutely bully weak hardware if you let it run wild.

---

# Project summary

This project is a practical exploration of mathematical precision in Python.

It began with simple and limited methods, moved through experimentation, and ended with a proper high precision implementation using:

* the **Chudnovsky algorithm**
* Python’s **Decimal** module
* a **FastAPI** web interface

It demonstrates:

* mathematical algorithm comparison
* precision handling
* limitations of floating point arithmetic
* backend integration with FastAPI
* HTML templating with Jinja
* web deployment

So this is not just “a π calculator”.

It is a small but meaningful project about:

* choosing the right algorithm
* understanding numerical limits
* implementing high precision computation
* turning a CLI script into a usable web app
* documenting the technical reasoning clearly

---

# Final note

If you are only interested in the raw Python logic, check `sample.py`.

If you want the full user-facing version, run the FastAPI app or visit the live preview.

---

**Powered by Python, precision, and a little mathematical stubbornness.**


