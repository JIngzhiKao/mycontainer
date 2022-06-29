import rhino3dm as rhino
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np


from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/median",
    name="median",
    description="find the median in this set",
    inputs=[
        hs.HopsNumber("set", "set", "the set to find with"),
    ],
    outputs=[
        hs.HopsNumber("median", "m", "the median")
    ]
)

def midian(set):
    n_num = set
    n = len(n_num) 
    n_num.sort()
    if n%2 == 0:
        median_1=n_num[n//2]
        median_2=n_num[n//2-1]
        median = (median_1+median_2)/2
        return(median)
    else:
        median = n_num[n//2]
        return(median)

if __name__ == "__main__":
    app.run()

