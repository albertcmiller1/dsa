class FatalException(Exception):
    pass 

try: 
    print(x)
    # raise FatalException
except FatalException as fe: 
    print(f"fatal error: {fe}")
    raise fe 
except Exception as e: 
    print(f"non-fatal error: {e}. retrying")
else: 
    print("nothing went wrong")