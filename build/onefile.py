#!/usr/bin/env python


import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    open(os.path.join(partial_path, "__init__.py"), "w").write("\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "w") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('sub1.py', 'def mean(a, b):\n    return (a+b)/2')
    __stickytape_write_module('folder/sub2.py', 'class Apple:\n\n    def __init__(self, value):\n        self.value = value')
    from sub1 import mean
    from folder.sub2 import Apple
    
    apple1 = Apple(value=100)
    apple2 = Apple(value=200)
    
    result = mean(apple1.value, apple2.value)
    print(result)