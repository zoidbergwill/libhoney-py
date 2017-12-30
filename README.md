# libhoney [![Build Status](https://travis-ci.org/honeycombio/libhoney-py.svg?branch=master)](https://travis-ci.org/honeycombio/libhoney-py) [![PyPi version](https://badge.fury.io/py/libhoney.svg)](https://badge.fury.io/py/libhoney)

Python library for sending events to [Honeycomb](https://honeycomb.io). (For more information, see the [Honeycomb documentation](https://honeycomb.io/docs) and [Python SDK guide](https://honeycomb.io/docs/connect/python).)

## Installation

```
pip install libhoney
```

## Documentation

An API reference is available at https://honeycombio.github.io/libhoney-py/

## Example

Honeycomb can calculate all sorts of statistics, so send the values you care about and let us crunch the averages, percentiles, lower/upper bounds, cardinality -- whatever you want -- for you.

```python
import libhoney

# Call init to configure libhoney
libhoney.init(writekey="YOUR_WRITE_KEY", dataset="honeycomb-python-example")

libhoney.send_now({
  "duration_ms": 153.12,
  "method": "get",
  "hostname": "appserver15",
  "payload_length": 27
})
```

You can find a more complete example demonstrating usage in [`example.py`](example.py)

## Django support

Add the middleware to your list of `MIDDLEWARE_CLASSES` in `settings.py`:

```
MIDDLEWARE_CLASSES = (
    # ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'libhoney.contrib.django.middleware.HoneyMiddleware',
)
```

And make sure you set these two environment variables:

`HONEY_WRITE_KEY`
`HONEY_DATASET`


## Contributions

Features, bug fixes and other changes to libhoney are gladly accepted. Please
open issues or a pull request with your change. Remember to add your name to the
CONTRIBUTORS file!

All contributions will be released under the Apache License 2.0.

## Releases
You may need to install the `bumpversion` utility by running `pip install bumpversion`.

To release a new version, run
```
bumpversion [major|minor|patch]
git push --tags
```
After a successful build, a new version will automatically be uploaded to PyPI.
