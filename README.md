# Test Driven Development (TDD) Pairing Session

The simplest way to get started with TDD and/or pairing is by writing tests for "pure" functions. (See [Glossary](#glossary))

### Contrived Example

Imagine a story that requires rejecting a `GET /contacts?last-name={invalid-input}` request to prevent unnecessary and potentially harmful queries of a database.

**For this portion of the story**, we will develop a `validate_last_name` method that will be used by the FastAPI route. The route will return a `400` (Bad Request) if this function returns `False`.

### "Acceptance Critieria"
Function returns `False` where:
1. Input is less than 3 characters
2. Input starts with a hyphen
3. Input ends with a hyphen
4. Input contains consecutive hyphens
5. Input contains characters OTHER than
    * Upper case alphbetic
    * Lower case alphabetic
    * Apostrophe 
    * Hyphen

### Pre-requisites
* `pytest` installed
* VSCode Live Share extension

## Exercise

1. **Developer "A"** writes one test to cover one portion of the story's "Acceptance Criteria" (`test_validator.py`). Run `pytest` to confirm the test fails.
2. **Developer "B"** makes the test pass by implementing code (`validator.py`). Run `pytest` to confirm the test passes.
3. **Developer "B"** writes one test to cover one portion of the story's "Acceptance Criteria" (`test_validator.py`). Run `pytest` to confirm the test fails.
4. **Developer "A"** makes the test pass by implementing code (`validator.py`). Run `pytest` to confirm the test passes.
5. Repeat until all of the "Acceptance Criteria" is met.

### Glossary

**Pure Function**
:   A pure function is a function that, given the same input, will always return the same output and does not have any observable side effects. This means it does not modify any external state or rely on any external state, making it deterministic and easier to test.

**TDD (Test-Driven Development)**
:   Test-Driven Development (TDD) is a software development process in which developers write tests for a function or feature before writing the code that implements the function or feature. The cycle typically follows these steps: write a test, run the test (which should fail), write the minimum code necessary to pass the test, and then refactor the code while keeping the test passing.
