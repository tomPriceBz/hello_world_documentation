name = "hello_world_test"

version = "1.0.1"

authors = [
    "ajohns"
]

description = \
    """
    Python-based hello world example package.
    """

tools = [
    "hello"
]

requires = [
    "python"
]

uuid = "examples.hello_world_py"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
