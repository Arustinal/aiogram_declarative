# Summary

I hope you read all doc files before this.

Now you can build your first bot with this tool.

I recommend using the following scheme:

```prettier
project/
├── app.py
└── bot/
    ├── __init__.py
    ├── __main__.py
    └── handling/
        ├── filters/
        ├── middlewares/
        ├── dialogs/
        ├── scheme.py
        └── *every handlers files*.py
```

Where scheme.py contains all joint classes.
In addition, I recommend use Registry from `bot\__main__.py`. 

If you have problems or questions, welcome to issue page on GitHub
