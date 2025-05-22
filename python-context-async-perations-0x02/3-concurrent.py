import aiosqlite     # Asynchronous SQLite library
import asyncio       # Built-in Python library for async operations

# Async function to fetch all users from the database
async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        await cursor.close()
        return results

# Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        results = await cursor.fetchall()
        await cursor.close()
        return results

# Function to run both queries concurrently using asyncio.gather
async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All Users:")
    print(all_users)

    print("\nUsers Older Than 40:")
    print(older_users)

# Run the async fetch
asyncio.run(fetch_concurrently())

