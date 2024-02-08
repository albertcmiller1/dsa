class FatalException(Exception):
    pass 

def start():
    def with_retry(entry_fn, retry_cnt, *args, **kwargw):
        if retry_cnt < 0: 
            raise Exception("too many retries")
        retry_cnt -= 1

        try: 
            return entry_fn(*args, **kwargw)
        except FatalException as fe: 
            print(f"fatal error: {fe}")
            raise fe 
        except Exception as e: 
            print(f"non-fatal error: {e}. retrying")
            return with_retry()

start()


try: 
    print("hi")
    raise FatalException
except FatalException as fe: 
    print(f"fatal error: {fe}")
    raise fe 
except Exception as e: 
    print(f"non-fatal error: {e}. retrying")