# One Line, One Laugh: Roast Your Fridge

[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/TonyWanders/roast-your-fridge/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/TonyWanders/roast-your-fridge/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

A single-line roast of my fridge, written by a deterministic program for the
[One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
bounty on make.fun.

## The roast

> My fridge light died years ago, so every midnight snack is a lucky dip between dinner and a container running its own science experiment.

## How it works

`main.py` writes the roast, exactly one line of at most 200 characters, to
`/output/entry.txt`. The output is deterministic: every run produces the
same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
