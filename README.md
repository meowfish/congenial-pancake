# congenial-pancake

- Uses Django
- Elm front end
- Something cooking related

# TODO 

1. an interpreter. Something that transforms the text of a recipe to json form
  - nlp using ntlk, maybe some machine learning
  - object expansion. Chopped tomato |-> chopped(tomato)
  - filling in 

2. database of recipes
  - turn recipes into checklists

3. selection algorithm for distributing recipes
  - filter by ingredients you have at home
  - maybe shopping thing of checklist
  - amount of time you have

4. navigation through each recipe
  - click start
  - screen goes one color with big bold text: "Do this."
  - steps have to be ordered in some not stupid way
    - if baking for 8 hours maybe don't do that last

3 chopped onions and 2 cups of diced tomato -> json recipe
```json
{
"name": "broiled tomato",
"amount": 123,
"unit": "drops",
"duration": 12938,
"tempreture": 400,
"busy": false,
"operation": "broil",
"ingredients": [{"name":"chopped tomato", "amount": 3, "unit": "cups"}, {}, {}]
}
```
