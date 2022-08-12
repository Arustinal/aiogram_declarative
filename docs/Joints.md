# Joints

Joint - is brick-like object of aiogram_declarative

This is your tool for creating structures.

1) Basic joint is CoreJoint. Router of CoreJoint is connected to Dispatcher Router.

2) Routers connecting through inheritance of joints.
Like this:
```python
class Admin(CoreJoint):  # Equals Admin Router -> MainRouter -> Dispatcher.
    router = Router(...)
    ...

class RootAdmin(CoreJoint): # Equals RootAdmin Router -> Admin -_ ...
    router = Router(...)
    ...
```

3) Let's create a short example structure.

```python
class Admin(CoreJoint):
    router = Router()  # from aiogram_declarative import Router 

    # router.message.middleware(...)  - as usual
    # router.message.filter(...) - as usual

    management_panel: Dialog = dialogs.management_panel  # import
    # This is addon - aiogram_dialog by @Tishka17
    # don't forget to set typing - it used by Registry for registration

    def __init__(self, admins: list):
        """NEVER USER THIS APPROACH FOR REAL ADMIN CHECKING!
        THIS IS ONLY FOR DEMONSTRATION PURPOSES!
        USE DATABASES AND PROPER REQUESTS!
        """
        self.router.filter(F.from_user.id in admins)

    @router.message(Command(commands=['start']))
    async def hello_admin(self):
        """There is your code for admins sended /start"""
        ...
```

Usually, handlers shouldn't exists in structure files.
However, it's not prohibited. It's ok for hot handler with high
RPS when you want not to have additional router and increased time processing as result.

You are able to define middlewares, filters, dialogs and everything using two approaches.

1) As class variables.Same as router above.
2) As instance variables.Use `def __init__(self, **kwargs)` for that.

`__init__` function can ask for variables from the Registry. But that's for another time. Just know you are able to get
variables from the initial configuration, same as kwargs from basic aiogram Dispatcher.

*Note: use typing for addons objects.This is highly encouraged*