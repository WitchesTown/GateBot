# GateBot
A small python bot that announce the opening / closing of the gates

## Usage

First you need to initialize your credentials :

```
$ python3 witchesGate.py --instance https://[your-instance-name] --login [your-login] --password [your-password]
```

Then you can choose one of the actions :

```
$ python3 witchesGate.py --instance https://[your-instance-name] --action {open,close,rules}
```

- `open` will send a random file found in `./data/open/` and jinx it with the message `#WitchesTown`
- `close` will send a random file found in `./data/close/` and jinx it with the message `#WitchesTown`
- `rules` will send a jinx with the content of the file `./data/rules.txt`
