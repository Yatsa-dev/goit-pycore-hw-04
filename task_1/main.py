from typing import TypedDict,Tuple

class Data(TypedDict):
    name: str
    salary: int

def total_salary(path:str)->Tuple[int, int] | None:
    try:
        if not isinstance(path, str):
            print(f"Error: Invalid input type for path. Expected str format, but got {type(path).__name__}. ")
            return None

        prepareData:list[Data]=[]
        
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data=line.strip().split(',')
            prepareData.append({"name":data[0],"salary":int(data[1])})

        total = sum(item['salary'] for item in prepareData) 
        average = int(total / len(prepareData))

        return total, average
    
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'.")
        return None 
    
# total, average = total_salary('task_1/data.txt') 
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")