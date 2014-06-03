# amsin

Not a ton to talk about here. This is a simple little Python program that takes
a regular long-as-shit amazon link and turns it into a shorter link based on the
asin on that page. It uses BeautifulSoup to extract this information.

The end result of the program is a link copied to your clipboard.

## Installation

```
pip install amsin
```

## Usage

```
$ amsin --help
Usage: amsin [OPTIONS] URL

  Turn a long amazon link into a short amzn link.

Options:
  --help  Show this message and exit.
```
