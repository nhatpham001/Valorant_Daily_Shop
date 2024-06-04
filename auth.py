import asyncio
from riot_auth import RiotAuth

RiotAuth.RIOT_CLIENT_USER_AGENT = "RiotClient/86.0.3.1523.3366 %s (Windows;10;;Professional, x64)"

async def authenticate():
    auth = RiotAuth()
    try:
        await auth.authorize('your_username', 'your_password')
        print('Access Token:', auth.access_token)
        print('Entitlements Token:', auth.entitlements_token)
        print('User Info:', await auth.get_userinfo())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(authenticate())
