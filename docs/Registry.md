# Registry

This is a core object of aiogram declarative.

Registry "magically" knows about every joint classes, routers, and handlers.
On startup, Registry will inspect your structure, construct scheme into working objects.

Let's look at the example below:
```python
# some main.py:

import ...

async def main():
    bot: Bot = ...
    dp: Dispatcher = ...
    ...
    registry = Registry(
        dp, addons=(
            DialogAddon(dialog_registry=DialogRegistry(dp)),
        ),
        admins=[...]  # you know, there is a bunch of IDs of admins.Refer to "Joints.md"
    )
    registry.construct()
    

if __name__ == '__main__':
    asyncio.run(main())
```

First of all, Registry require dispatcher instance.
After dispatcher, we need to give the addons collection.
In example we can see built-in addon - for library named "aiogram-dialog" by @Tishka17

After that - any keyword attributes will be granted to Routers `def __init__(self, ...)` method.
You can define your custom addons too.