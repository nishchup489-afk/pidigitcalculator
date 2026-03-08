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