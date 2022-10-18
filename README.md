# key-search-nested-object

## Use-case
- This utility helps retreiving search key from the nested python object

## How to set-up and run
- Clone this repository
    - `git clone https://github.com/sumitroy2611/key_search`
- Open the repository on your instance
    - `cd key_search`
- Open the `src` folder
  - `cd key_search/src`
- Run whichever script you need:
  - `python3 key_search.py`  
        This prompts with following messages:
        `Please enter the json object to be parsed:`
        `Please enter the key to be searched in the object:`

## How it works
- It makes use of recursion to slice the search key that is already matched with the object key and send the remaining search keys for further round of iteration until all the keys are search and final value is attained

## Unit tests
- Unit tests has been written in tests/tests.py and is executed using python unittest module.
- To run the tests following command needs to be executed from the root folder: 
       - python -m unittest
