# Matrix Builder

So that you can paste in to Wolfram Alpha quicker

# How to Use

## 1) Create a Matrix

Simply edit the `temp.csv` in a text editor to enter a comma delimited matrix

## 2) Choose an operation

I'll build a better CLI for this, but at the time of writing you can choose between `['row reduce', 'determinant', 'null space']`

> Note no matter what operation you choose you can easily change this once in Wolfram


## 3) Click on the Wolfram Alpha link

You'll output similar to the following, of which all you need to do is [click on the URL](https://www.wolframalpha.com/input/?i=row+reduce+%7B%7B1%2C2%2C0%7D%2C%7B0%2C5%2C-4%7D%2C%7B-1%2C1%2C3%7D%7D) to see the results in Wolfram Alpha

```
You passed in this list: ['1,2,0', '0,5,-4', '-1,1,3']
Suggested command: row reduce {{1,2,0},{0,5,-4},{-1,1,3}}
Go to Wolfram: https://www.wolframalpha.com/input/?i=row+reduce+%7B%7B1%2C2%2C0%7D%2C%7B0%2C5%2C-4%7D%2C%7B-1%2C1%2C3%7D%7D
```
