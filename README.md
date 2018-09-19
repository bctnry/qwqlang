# qwqlang
Lambda calculus DBI style in Forth-like manner. (esoteric)

## Command list
* `qwq` - the number of consecutive `qwq`s denotes the index.
* `qnq` - delimiter between two different index.
* `qaq` - abstraction.
* `qxq` - application.

## Example

### SKI
```
S = λx. λy. λz. x z (y z) = λ λ λ 3 1 (2 1) = λ λ λ (3 1) (2 1)
  = qwq qnq qwq qwq qxq qwq qnq qwq qwq qwq qxq qxq qaq qaq qaq
K = λx. λy. x = λ λ 2 = qwq qwq qaq qaq
I = λx. x = λ 1 = qwq qaq
```

damn this is so stupid.

## Usage
After loading the python module:
```
>>> qwq_dbi_conv("qwq qnq qwq qwq qxq qwq qnq qwq qwq qwq qxq qxq qaq qaq qaq")
'λλλ((3 1) (2 1))'
```

## Why don't you do the rest

I'm tired okay, this esolang is just for a joke.