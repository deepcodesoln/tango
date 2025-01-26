# 単語 (tango)

This repository contains lists of Japanese vocabulary and grammar stored as CSV files.

## CSV Schema

### Vocabulary

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

### Grammar

All lists use the same schema. Quoting and embedded HTML are the same as that for
vocabulary (see above).

Each row contains the following elements.

1. Japanese grammar element
1. First example sentence in Japanese
1. First example sentence in English
1. Second example sentence in Japanese
1. Second example sentence in English
1. Explanation of grammar element

## HTML Styling

The Japanese sentences may contain furigana embedded in
[ruby](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) elements. Assuming
a Japanese sentence is a child of

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
programmatically from scratch, use the types in `interface.py` to conform to the
standard schema.

Vet new lists by parsing them with the checked-in implementation of `interface.py` to
make sure there are no parsing errors.

## Lists

### Vocabulary

1. [core\_2k.csv](./vocab/core_2k.csv): a modified version of
   [コア2.3k v3](https://anacreondjt.gitlab.io/docs/coredeck/), itself a modified
   version of [core6000](https://core6000.neocities.org/); adjusted
   definitions, formatting, removed images and audio
1. [population\_decrease.csv](./vocab/population_decrease.csv): a list of vocabulary
   relating to the phenomenon of population decrease
1. [real\_estate\_housing.csv](./vocab/real_estate_housing.csv): a list of vocabulary
   relating to real estate, housing, renting, etc.; includes casual terms and formal
   terms you would find in things like contracts
1. [software\_engineering.csv](./vocab/software_engineering.csv): a list of vocabulary
   relating to software engineering; many terms are in kana, but it's useful to see
   how such terms might be used in context

### Grammar

1. [JLPT N2](./grammar/n2.csv): a group of grammar elements of approximately JLPT N2
   level

## License

[MIT license](./LICENSE).
