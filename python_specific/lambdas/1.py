
arr = [
    {"status": "done"},
    {"status": "done"},
    {"status": "done"},
    {"status": "done"},
    {"status": "done"},
    {"status": "pending"}
]


all_done = all(i["status"] == 'done' for i in arr)
print(all_done)