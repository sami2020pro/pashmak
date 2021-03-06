# `$__ismain__` variable
the `$__ismain__` variable, is a general Boolean variable. this variable is used to check the current file, is the **Main runed file** or not.

for example, we have two files, `my_program.pashm` and `lib.pashm`. we want to know that in our scripts **Is the current script main directly runed file?**.

when you run in terminal:

```bash
pashmak my_program.pashm
```

the `my_program.pashm` file is runed directly.

#### my_program.pashm:

```bash
println($__ismain__)

import('lib.pashm')
```

the above code, prints value of this variable and also imports `lib.pashm` file.

#### lib.pashm:

```bash
println($__ismain__)
```

when i run `my_program.pashm`, output is this:

```
True
False
```

actually, value of this variable in `my_program.pashm` is `True`, but in `lib.pashm` is `False`.

now, when i run `pashmak lib.pashm`, output is `True`.

**The `$__ismain__` variable says that the current file is main runed file or not and you can check this**.

for example, if we want to run a code only if our script is directly runed and is not imported from other script:

```bash
if $__ismain__
    # do something
endif
```
