# Test Driven Development (TDD) Pairing Session

The simplest way to get started with TDD and/or pairing is writing tests for "pure" functions. (See Glossary)

### Contrived Example
Imagine a story needs to reject a GET /contacts?last-name={invalid-input} request to prevent unnecessary and potentially harmful queries of a database.  For this portion of the story we will develop a `validate_last_method` method that will be used by the Fast API route.  It will return a 400 (Bad Request) if this function returns False.

### Pre-requisites
* pytest installed
* vscode live share extension

## Excercise

1. Developer "A" writes one test to cover one portion of the stories "Acceptance Critieria" (`test_validator.py`). Run `pytest` to confirm the test passes.

1. Developer "B" makes the test pass by implementing code (`validator.py`). Run `pytest` to confirm the test passes.

1. Developer "B" writes one test to cover one portion of the stories "Acceptance Critieria" (`test_validator.py`). Run `pytest` to confirm the test passes.

1. Developer "A" makes the test pass by implementing code (`validator.py`). Run `pytest` to confirm the test passes.

1. Repeat until all of the "Acceptance Critieria" is met.

### Glossary

**Pure Function**
:   A pure function is a function that, given the same input, will always return the same output and does not have any observable side effects. This means it does not modify any external state or rely on any external state, making it deterministic and easier to test.

**TDD (Test-Driven Development)**
:   Test-Driven Development (TDD) is a software development process in which developers write tests for a function or feature before writing the code that implements the function or feature. The cycle typically follows these steps: write a test, run the test (which should fail), write the minimum code necessary to pass the test, and then refactor the code while keeping the test passing.
