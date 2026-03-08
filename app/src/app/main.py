from fastapi import FastAPI , Request , Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from math import factorial
from decimal import Decimal , getcontext

app = FastAPI()


import os
from pathlib import Path

# Get the current file's directory (app/src/app)
BASE_DIR = Path(__file__).resolve().parent

# Set the template directory relative to this file
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def chudnovsky(n):
    getcontext().prec = n + 10

    # IMPORTANT : chudnovsky gives 14.18 digits per iteration , but we need 1 digit per iteration
    iteration = ( n // 14) + 1

    sum_total = Decimal(0) # a bucket where currently no numbers

    for k in range(iteration):
        # Numerator: (-1)^k * (6k)! * (13591409 + 545140134k)
        num = ((-1)**k) * factorial(6*k) * (13591409 + 545140134*k)
        
        # Denominator: (3k)! * (k!)^3 * 640320^(3k)
        den = factorial(3*k) * (factorial(k)**3) * (640320**(3*k))

        sum_total += ( Decimal(num) / Decimal(den))

    constant = Decimal(426880) * Decimal(10005).sqrt()

    pi = constant / sum_total
    return pi


@app.get("/" , response_class=HTMLResponse)
async def home(request : Request):
    return templates.TemplateResponse(
        "index.html" , 
        {"request" : request}
    )


@app.post("/calc" , response_class=HTMLResponse)
async def calculate(request : Request , user_input : int =Form()):
    res = chudnovsky(user_input)
    result = f"{res:.{user_input}f}"

    return templates.TemplateResponse(
        "index.html", 
        {
            "request" : request ,
            "result" : result
        }
    )

@app.get("/about" , response_class=HTMLResponse)
async def About(request : Request):
    return templates.TemplateResponse(
        "about.html" , 
        {"request" : request}
    )