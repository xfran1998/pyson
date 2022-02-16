# Pyson
This is a funny project for creating a descriptive way to program a python bot using json. This way I can use it to easy make a visualy development web aplication to create a bot.

This bot actions are preprogramed an called from the pyson program though pyson.py at least for now.

This is meant to be used for people don't want don't how to program a multithread bot using python or just an easy and fast way to do it.

Anyone is free to help in this funny project.

## JSON Legend
- "start" : {}
- "vision": { "type" : \<vision type\>, "crop": true }
- "delete" : "\<vision type\>"
- "delay": x
- "loop" : {"time" : x, "start": [{}], "condition": true}
- "var" : { "x": 2, "y": 5.19 }
- "print" : "some vars: ${x}, ${y}"

<hr>

## Start 
Where bot start running

<hr>

## Vision
Will create a new vision object with defined vision type and crop space

### vision types:
what we want to search in img

- "orbit" : Ship in orbit
- "planet" : Ship arrive to planet
- "interp" : Look for interp in the panel
- "reco" : Look for reco in the panel
- "energy" : How many energy player have
- ...

### crop:
If crop is setted to true the program will search in crop_areas.json to get the area of the \<vision type\> with the same string

Crop coords from original we want out vision works on, smaller cropped img is faster will be the match template

- [x1, y1] : top-left corner
- [x2, y2] : bottom-rigth corner
- []: no need to crop

<hr>

## Delete
Will delete vision type created before

<hr>

## Loop
Will loop all inside start var x times

- times: how many times sould loop
- start: all the operations will do each iteration
- condition: condition have to met at the end of each iteration to continue looping

### condition:

conditions:
- "condition" : true -> always will iterate
- "condition" : {"check": "iqual", { "var1" : \<var type\>: , "var2" : \<var type\> } }

#### check
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

## How start the program:
main.json need to be in the same folder as pyson.py
