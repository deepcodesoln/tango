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

## HTML Styling

The Japanese sentence may contain furigana embedded in
[ruby](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) elements. Assuming
the Japanese sentence is a child of

```html
<div class="front">...</div>
```

then you can hide the furigana if desired via

```css
.front rt {
  display: none;
}
```

This way you can hide furigana in certain presentations and render it in others.

## Modification

You can make modifications to lists manually, or, for an example of working with lists
programmatically, see [interface.py](./interface.py). If building a new list
programmatically from scratch, use `Vocabulary` from `interface.py` to conform to the
standard schema.

Vet new lists by parsing them with the checked-in implementation of `interface.py` to
make sure there are no parsing errors.

## Lists

1. [artificial\_intelligence.csv](./lists/artificial_intelligence.csv): a list of
   vocabulary related to artificial intelligence and neural networks
1. [computer\_hardware\_circuits.csv](./lists/computer_hardware_circuits.csv): a list of
   vocabulary relating to computer hardware and circuitry
1. [core\_2k.csv](./lists/core_2k.csv): a modified version of
   [コア2.3k v3](https://anacreondjt.gitlab.io/docs/coredeck/), itself a modified
   version of [core6000](https://core6000.neocities.org/); adjusted
   definitions, formatting, removed images and audio
1. [population\_decrease.csv](./lists/population_decrease.csv): a list of vocabulary
   relating to the phenomenon of population decrease
1. [real\_estate\_housing.csv](./lists/real_estate_housing.csv): a list of vocabulary
   relating to real estate, housing, renting, etc.; includes casual terms and formal
   terms you would find in things like contracts
1. [self\_actualization.csv](./lists/self_actualization.csv): a list of vocabulary
   relating to the concept of self-actualization
1. [software\_engineering.csv](./lists/software_engineering.csv): a list of vocabulary
   relating to software engineering; many terms are in kana, but it's useful to see
   how such terms might be used in context

## License

[MIT license](./LICENSE).
