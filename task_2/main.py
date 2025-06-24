from typing import TypedDict,List

class Data(TypedDict):
    id: str
    name: str
    age: str

def get_cats_info(path:str)->List[Data] | None:
    try:
        if not isinstance(path, str):
            print(f"Error: Invalid input type for path. Expected str format, but got {type(path).__name__}. ")
            return None

        result:list[Data]=[]
        
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data=line.strip().split(',')
            result.append({"id":data[0],"name":data[1],"age":data[2]})

        return result
    
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'.")
        return None 
     
# cats_info = get_cats_info('task_2/data.txt') 
# print(cats_info)
