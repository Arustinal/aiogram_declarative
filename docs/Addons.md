# Addons

You are free to extend aiogram_declarative as needed.
Part of this ability is addon system.

Let's look at the following example code from built-in addon - aiogram-dialog:
```python
class DialogAddon(AbstractAddon):
    """Aiogram Dialog's support"""

    def __init__(self, dialog_registry: DialogRegistry) -> None:
        self.registry = dialog_registry

    @property
    def instance_type(self) -> Type[Dialog]:
        """This property should return a type of class, which instance should be executed with that addon."""
        return Dialog

    def register(self, router: Router, var_name: str, var_content: Any) -> None:
        """This method calls by Registry in a moment of construction whole bot structure."""
        self.registry.register(var_content, router=router)
```

*Note: abstract class is great tool! Refer to that!*

Any addon can use variables from outside through the `def __init__(self, ...)` method.
You can see it from "Registry" page.

In the same time, any addon should have a property with type of variable from joints, 
which needed to be registered using this addon.Don't forget to set types in the joints.

Finally, `def register(self, router: Router, var_name: str, var_content: Any)`.
This method receives the information about found variables and registers them.

That's it.Refer to abstract class for more information.