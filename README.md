# My daily python 3.6 workout 💪

Set of incomplete files used to practice python 3.6. Tests are included 🎉

## Getting Started

The goal of these exercises is to make you/me remember the basics of python3 using repetition, lots of it.

My suggestion is to complete all the files once a day and run the tests until your code passes them all.

It may seem like a hard and time consuming task, but it should get easier the more you do it.

Just keep in mind this is not intended to learn python3, nor it provides all the tools python3 has to give. This is just practice.

### Prerequisites

- Latest version of python 3
- pytest (kind of optional)

### Installing

Apart from python3 you shouldn't need to install anything else. Although I recommend installing `pytest` using something like `pipenv` since one of the exercises consists in implementing a couple of tests using this module.

## Running the tests
In order to test your code I implemented tests both in *unittest* and *pytest*.

There's no real advantage of one over the other in this project, since both modules test the code in the same way, I just wanted to practice.

You can run every test from the root directory:
- *pytest:* `python3 -m pytest`
- *unittest:* `python3 -m unittest discover -p "*_unittest_test.py"`

Or you can test each exercise individually, just cd into its directory and run:
- *pytest:* `python3 -m pytest`
- *unittest:* `python3 -m unittest discover -p -t .. "*_unittest_test.py"`

## Built With

* ♥️

## Contributing

Feel free to fork and make pull requests to this repository.

## Authors

* **Marco Nila** - *Initial work* - [sainoba](https://github.com/sainoba)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* James Powell
* Dan Bader
