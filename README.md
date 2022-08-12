If you tired of watching this:

```python
import ...


def setup_routers() -> Router:
    from . import unsupported_reply, admin_no_reply, bans, adminmode, message_edit, usermode

    router = Router()
1   router.include_router(unsupported_reply.router)
2   router.include_router(bans.router)
3   router.include_router(admin_no_reply.router)
4   router.include_router(adminmode.router)
5   router.include_router(message_edit.router)
6   router.include_router(usermode.router)
...

    return router
```

you found the way to fix it.

Check "docs" folder for more information