# Stdlib
`stdlib` is a very important and useful module.
this module make the pashmak syntax easy.

this module not need to be import because it will import automaticaly.

look at this example:

```bash
# print
print "hello world"; # INSTEAD OF `mem 'hello world'; out ^;`

# import
import 'somefile.pashm';
import '@hash'; # INSTEAD OF `mem '@hash'; include ^`

# exit
exit; # exits program
exit 2; # exits with exit code
# INSTEAD OF `return;` and `return 2;`

# py
py "print('hello world from python')"; # INSTEAD OF `mem "print('hello world from python')"; python ^`

# sys
sys 'ls /tmp'; # INSTEAD OF `mem 'ls /tmp'; system ^;`

# std.chdir
std.chdir "/tmp"; # INSTEAD OF `mem '/tmp'; chdir ^;`

# std.eval
std.eval 'mem "hi"\; out ^\;'; # INSTEAD OF `mem 'mem "hi"\; out ^\;'; eval ^`
```

##### raising errors
```bash
print 'program started\n';

raise ['MyError' , 'this is my error'];

print 'this will not print\n';
```

output:

```
progrma started
MyError:
	this is my error
```

the `raise` alias can raise errors in program

first argument `'TheError'` is error type and second error `'this is my error'` is error message.

##### finish

this module includes some aliases to make the pashmak syntax better.

also look at this example about print:

```bash
print 'enter your name: ';
set $name; read $name;

print 'hello ' + $name + '\n';

```