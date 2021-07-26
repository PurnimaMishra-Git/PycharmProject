def function_args(normal,*args,**kwargs):
    for item in args:
        print(item)

    for key, value in kwargs.items():
            print(f"{key} is a {value}")
normal="this is students"
list=["neema","meena","teena","jeena","peena"]
dict={"rohan":"monitor","mohan":"coordinator","alex":"label cordinator","pheena":"teacher"}

function_args(normal,*list,**dict)

