import asyncio 
async def func(): 
    print("Hey....") 
    await asyncio.sleep(1) 
    print("I am here...") 
asyncio.run(func())