# Homework
- Name: Andrew Porasl

## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: Unit tests check one piece of a program in an isolated setting. You'd use this when you want to make sure that each individual part of a program works properly before integrating it with the rest of the program.
- Integration test: Integration tests check how units work together with other units. You'd use this to make sure different parts of your code combine as intended and work clearly as intended with other parts of your program.
- Regression test: Regression tests re run previous tests to make sure that the latest code added doesn't break anything. You'd use this when you add a new feature, fix bugs, or change anything in the code that might affect the larger program.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.

pytest discovery finds tests by looking for files named test_{name}.py or {name}_test.py and for functions that go test_{name}:

A fixture is a defined, reliable and consistent context for tests. It's a set up function that can be used repeatedly without having to, for example, fill out an entire set up each time.

PYTEST features used:

@pytest.fixture
@pytest.mark.parametrize
pytest.approx