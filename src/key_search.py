import ast
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ========================================================================================================
# This methods searches the keys from the nested object and returns the value to main method
# ========================================================================================================
def key_search(dict, search_keys):
    try:
        if len(search_keys)==1: 
            return dict[search_keys[0]]
        return key_search(dict[search_keys[0]],search_keys[1:])

    except Exception as exp:
        logger.error("Unsupported object search. Please read the read.me file")

# ========================================================================================================
# This methods converts the string object into dictionary and search item into list
# ========================================================================================================
def get_value(object, search):
        #Splitting the search keys based on '/'
        search = search.split('/')

        #Converting the string object to python dictionary object
        my_dict = ast.literal_eval(object)

        return key_search(my_dict, search)

# ========================================================================================================
# This main method takes 2 runtime parameters when prompted
# 1. Enter the nested object to be parsed and used for searching. e.g. : {"x":{"y":{"z":"a"}}}
# 2. Enter the key to be searched from the nested object. Format: "x/y/z" 
# ========================================================================================================
if __name__ == "__main__":
        #Input parameters
        object = input("Please enter the json object to be parsed:\n")
        search = input("Please enter the key to be searched in the object:\n")

        print(get_value(object, search))

