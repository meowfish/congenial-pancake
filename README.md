# congenial-pancake

## Interpreter branch
A tool to create recipe files.

### Example
"3 chopped onions" should become 
```json
{
    "name": "chopped onions",
    "operation": "chop",
    "ingredients": [
        {
            "name": "onion",
            "amount": 3,
            "unit": "item"
        }
    ]
}
```

There should be a comprehensive ui to create recipies quickly and easily.

