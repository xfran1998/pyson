# Pyson
This is a funny project for creating a descriptive way to program only using Json. 

DISCLAIMER:
This is a side project complementing a visual detection bot made in python. This bot is made using classes implementing behaviors, this behaviors can be exuted in a descritive way using this "languaje".

Actions are preprogramed an called from the pyson program though pyson.py at least for now.

This is meant to be used for people don't want don't how to program a multithread bot using python or just an easy and fast way to do it making use of it and the bot library.

![Example Program](https://i.imgur.com/a54v2KQ.png 'Example Program1')

## JSON Legend
- "start" : {}
- "vision": { "type" : \<vision type\>, "crop": true }
- "delete" : "\<vision type\>"
- "delay": x
- "loop" : {"time" : x, "start": [{}], "condition": true}
- "condition" : ...
- "var" : { "x": 2, "y": 5.19 }
- "print" : "some vars: ${x}, ${y}"
- "operation" : "x = y + 1"

<br>
<hr>
<br>

## Start 
Where bot start running, all the code should be inside

```json
{
    "start": {
        "var": {
            "x": 1,
            "y": 0
        },
        "loop": {
            "times": 10,
            "start": [
                {
                    "operation": "y = y + x"
                }
            ]
        },
        "print": "y = ${y}"
    }
}
```

<br>
<hr>
<br>

## Vision
Will create a new vision object with defined vision type and crop space

### vision types:
What we want to search in img
(Future implementation)

### crop:
If crop is setted to true the program will search in crop_areas.json to get the area of the \<vision type\> with the same string

Crop coords from original we want out vision works on, smaller cropped img is faster will be the match template.

- [x1, y1] : top-left corner
- [x2, y2] : bottom-rigth corner
- []: no need to crop

<br>
<hr>
<br>

## Delete
Will delete vision type created before

<br>
<hr>
<br>

## Loop
Will loop all inside start var x times

- times: how many times sould loop
- start: all the operations will do each iteration
- condition: condition have to met at the end of each iteration to continue looping

<br>
<hr>
<br>

## condition:

conditions:
- "condition" : true -> always will iterate
- "condition" : {"check": "iqual", { "var1" : \<var type\>: , "var2" : \<var type\> } }

### check
var types:
- int, float, string, array, \<vision type\>

\<vision type\> params:
- matches : get how many matches has found
- times_search : get how many time has seached for matches
- not_found : get how many times have found 0 matches in arrow 

example \<vision type\>:
```json
    "condition" : 
    {
        "check": "iqual", 
        "variables":
        { 
            "var1" : 
            {
                "vision_type": "orbit",
                "param": "matches"
            }, 
            "var2" : 0 
        } 
    }

```
<br>
<hr>
<br>

## How start the program:
main.json need to be in the same folder as pyson.py

[Example program](#start)
<br>

call pyson program
```
python pyson.py
```
<br>
<hr>
<br>

## Operation
Will complete a basic operation using variables already declared

Valid operations:
- "+"
- "-"
- "*"
- "/"
- "^"

<br>
<hr>
<br>

## Error handling
For now there's a basic error handling in the features implemented

<br>
<hr>
<br>

## Features implemented

- Variables
- Loops
- Print
- Operation

TODO:
- Delay
- Conditions
- Functions

