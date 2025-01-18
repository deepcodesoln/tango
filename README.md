# 単語 (tango)

This repository contains lists of Japanese vocabulary stored as CSV files.

## CSV Schema

All lists use the same schema. Quotes are escaped by doubling them, equivalent to
Python3's `csv.Dialect.doublequote = true`
([ref](https://docs.python.org/3/library/csv.html#csv.Dialect.doublequote)). Strings
may have embedded HTML, typically for inline text styling. List content is intentionally
minimal, with no references to things such as audio or images.

Each row contains the following elements.

1. Japanese vocabulary
1. kana reading
1. English meaning
1. Japanese sentence
1. English sentence

## Modification

You can make modifications to lists manually, or, for an example of working with lists
programmatically, see [interface.py](./interface.py). If building a new list
programmatically from scratch, use `Vocabulary` from `interface.py` to conform to the
standard schema.

## Lists

1. [core\_2k.csv](./lists/core_2k.csv): a modified version of
   [コア2.3k v3](https://anacreondjt.gitlab.io/docs/coredeck/), itself a modified
   version of [core6000](https://core6000.neocities.org/); adjusted
   definitions, formatting, removed images and audio
1. [real\_estate\_housing.csv](./lists/real_estate_housing.csv): a list of vocabulary
   relating to real estate, housing, renting, etc.; includes casual terms and formal
   terms you would find in things like contracts

## License

[MIT license](./LICENSE).
