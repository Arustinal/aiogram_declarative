# Concept

Usually, people use templates for their aiogram bots.
But many of them have something like this:

https://github.com/MasterGroosha/telegram-feedback-bot/blob/master/bot/handlers/__init__.py
```python
import ...


def setup_routers() -> Router:
    from . import unsupported_reply, admin_no_reply, bans, adminmode, message_edit, usermode

    router = Router()
    router.include_router(unsupported_reply.router)
    router.include_router(bans.router)
    router.include_router(admin_no_reply.router)
    router.include_router(adminmode.router)
    router.include_router(message_edit.router)
    router.include_router(usermode.router)

    return router
```

1) Terrible copy of the code.
And we can't add all pack in single command call, so there is no alternative.
2) Can I see connected middlewares and filters? There - no, go to implementation files
3) Imagine you wrote this code a time ago? Can you remember original structure fast?

This is everywhere:
1) https://github.com/prostmich/simplecaptcha-bot/blob/master/app/handlers/__init__.py
2) https://github.com/den10b/KitaiBot/blob/24597a538628381795bf1cd81b53cc4e6729eab7/tgbot/handlers/user/__init__.py
3) etc
 
Sometimes this looks little stranger: https://github.com/den10b/KitaiBot/blob/master/tgbot/handlers/__init__.py
```python
from aiogram import Dispatcher

from .user import setup as user_setup
from .admin import setup as admin_setup


def setup(main_dp: Dispatcher):
    user_setup(main_dp)
    admin_setup(main_dp)
```
Global non-clean functions.Meh.

What about tool, which can solve this problem?
My solve for this mess - aiogram_declarative

Cons:
1) We will have one declarative-style file, which describes 
the whole structure of bot in one place
2) We can see all structure in one place.No sprint of "Go To" more.
3) No walls of "include_router/setup/etc" more
4) No hard connection between substructures.
You are able to split files relations and routers relations
5) Connect routers using inheritance of classes
6) Group your handlers/middlewares/filters and routers using classes.
Using IDE, you can focus your vision on specific class, hide every another.
7) Built-in support for aiogram-dialog @Tishka17
It means you can easily connect dialogs to your structure without pain.

Pros:
1) Additional requirement
2) Some time for apply this library to your structure

Let's look how is works.