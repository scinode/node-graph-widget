"""
===========
Quick Start
===========

"""

# %%
# Installation
# ==================
# Let's first install ``node-graph`` via pip:
#
# .. code:: console
#
#    $ pip install node-graph
#
# First workflow
# ==================
# Suppose we want to calculate ``(x + y) * z`` in two steps.
#
# - step 1: add `x` and `y`
# - step 2: then multiply the result with `z`.
#

# %%
# Create task
# ------------------
# Task is the basic building block of a workflow. One can create a task from a Python function using the `decorator`:

# %%
from node_graph.decorator import task


@task()
def add(x, y):
    return x + y


@task()
def multiply(x, y):
    return x * y


@task.graph()
def AddMultiply(x, y, z):
    the_sum = add(x=x, y=y).result
    return multiply(x=the_sum, y=z).result


ng = AddMultiply.build(x=1, y=2, z=3)
ng.to_html()
