import pickle
import subprocess

def open_calculator():
    try:
        subprocess.run(["calc.exe"], check=True)
        print("Calculator opened")
    except Exception as e:
        print(f"Failed to open calculator: {e}")

def serialize_function():
    func = open_calculator
    with open('calc_serialized.pkl', 'wb') as file:
        pickle.dump(func, file)
        print("Function serialized.")

def deserialize_and_execute_function():
    try:
        with open('calc_serialized.pkl', 'rb') as file:
            func = pickle.load(file)
        func()
    except Exception as e:
        print(f"Failed to deserialize or execute function: {e}")
