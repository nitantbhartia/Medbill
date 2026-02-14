# CLAUDE.md

## Core Philosophy

Write the simplest code that works. Every line must earn its place. If you can solve it in 10 lines, don't write 50. If a standard library does it, don't build a custom solution. Complexity is a bug.

## Rules

### Before Writing Any Code

1. **Understand the full requirement before typing.** Ask clarifying questions if the task is ambiguous. Don't guess and build the wrong thing.
1. **Plan the approach in 2-3 sentences.** State what you're going to build and why. If you can't explain it simply, you don't understand it yet.
1. **Check if something already exists.** Before creating a new file, function, or module, check the existing codebase. Don't duplicate what's already there.

### Writing Code

1. **One function does one thing.** If a function has "and" in its description, split it.
1. **No premature abstraction.** Don't create a class when a function works. Don't create a framework when a script works. Don't add generics, factories, or patterns "in case we need them later." Build for today's requirements.
1. **Use standard libraries first.** Python stdlib > pip package > custom code. Always.
1. **Flat is better than nested.** If you're more than 3 levels of indentation deep, refactor. Use early returns to avoid nesting.
1. **Name things clearly.** `get_medicare_rate(cpt_code, zip_code)` not `fetch_data(code, loc)`. Variable names should make comments unnecessary.
1. **No dead code.** Don't leave commented-out code, unused imports, unused functions, or TODO placeholders. If it's not used right now, delete it.
1. **Keep files short.** If a file exceeds 300 lines, it's doing too much. Split it.
1. **No magic numbers.** Put constants in config.py with descriptive names.

### Error Handling

1. **Handle errors where they happen.** Don't let exceptions bubble up silently. Catch specific exceptions, not bare `except:`.
1. **Fail loudly in development, gracefully in production.** Log the full error with context (what was being attempted, what input caused it), then return a clear error message to the user.
1. **Validate inputs at the boundary.** Check user input, API responses, and file contents at the point they enter your system. Don't trust anything external.
1. **Never swallow errors.** No empty `except: pass` blocks. Ever.

### Testing

1. **Test the happy path and the most likely failure.** Don't write 50 edge case tests for a simple function. But DO test: valid input works, invalid input fails gracefully, empty/null input doesn't crash.
1. **Test with real-ish data.** Don't test a bill scanner with `{"amount": 1}`. Use realistic medical bill data, realistic CPT codes, realistic dollar amounts.
1. **Run the code before saying it works.** Execute it. Check the output. Don't just write it and declare victory.

### Database

1. **Use SQLite simply.** No ORMs unless the project already uses one. Raw SQL with parameterized queries is fine and easier to debug.
1. **Always use parameterized queries.** Never f-string or format SQL with user input. `cursor.execute("SELECT * FROM bills WHERE id = ?", (bill_id,))` always.
1. **Add indexes for columns you query on.** But don't over-index. If you WHERE or JOIN on it, index it.
1. **Migrations are just SQL files.** Don't build a migration framework. A numbered SQL file that runs once is fine.

### API Design

1. **Endpoints do one thing.** `POST /validate/all` runs all validators. Don't make the caller figure out which 6 endpoints to call.
1. **Return consistent shapes.** Every endpoint returns `{"status": "ok"|"error", "data": {...}}`. No surprises.
1. **Use HTTP status codes correctly.** 200 = success, 400 = bad input, 500 = our fault. Don't return 200 with `{"error": "something broke"}`.

### Dependencies

1. **Minimize dependencies.** Every pip package is a liability. If you only need one function from a library, consider writing it yourself.
1. **Pin versions.** `requests==2.31.0` not `requests>=2.31.0`. Reproducible builds matter.
1. **No dependency is better than a bad dependency.** If a package hasn't been updated in 2 years, has 12 open security issues, or does way more than you need — skip it.

## Code Style

### Python

```python
# YES: Simple, readable, obvious
def get_medicare_rate(cpt_code: str, locality: str) -> float | None:
    with get_db() as db:
        row = db.execute(
            "SELECT facility_rate FROM medicare_rates WHERE cpt_code = ? AND locality = ?",
            (cpt_code, locality)
        ).fetchone()
    return row["facility_rate"] if row else None


# NO: Over-engineered, abstract, hard to follow
class MedicareRateProvider(BaseRateProvider):
    def __init__(self, db_connection_factory, cache_strategy=None):
        self._db_factory = db_connection_factory
        self._cache = cache_strategy or NoOpCache()

    def get_rate(self, code: str, locality: str, rate_type: RateType = RateType.FACILITY) -> Optional[Decimal]:
        cache_key = f"medicare:{code}:{locality}:{rate_type.value}"
        cached = self._cache.get(cache_key)
        if cached is not None:
            return cached
        # ... 40 more lines
```

```python
# YES: Early return, flat structure
def analyze_line_item(item):
    if not item.get("cpt_code"):
        return {"status": "skip", "reason": "no CPT code"}

    rate = get_medicare_rate(item["cpt_code"], locality)
    if not rate:
        return {"status": "skip", "reason": "no Medicare rate found"}

    markup = item["charged_amount"] / rate
    if markup <= 3:
        return {"status": "ok", "markup": markup}

    return {
        "status": "flagged",
        "markup": markup,
        "potential_savings": item["charged_amount"] - (rate * 3),
    }


# NO: Nested, hard to follow
def analyze_line_item(item):
    if item.get("cpt_code"):
        rate = get_medicare_rate(item["cpt_code"], locality)
        if rate:
            markup = item["charged_amount"] / rate
            if markup > 3:
                return {
                    "status": "flagged",
                    "markup": markup,
                    "potential_savings": item["charged_amount"] - (rate * 3),
                }
            else:
                return {"status": "ok", "markup": markup}
        else:
            return {"status": "skip", "reason": "no Medicare rate found"}
    else:
        return {"status": "skip", "reason": "no CPT code"}
```

```python
# YES: Simple config
MIN_READABILITY_SCORE = 60
MAX_WORD_COUNT = 1800
MEDICARE_MARKUP_THRESHOLD = 3.0


# NO: Config class with inheritance
class BaseConfig:
    class Meta:
        abstract = True

class ProductionConfig(BaseConfig):
    READABILITY_SCORE = ConfigValue(default=60, type=int, validator=range_validator(0, 100))
```

## Project Structure

Keep it flat. Don't create deeply nested folder hierarchies for small projects.

```
project/
├── config.py              # all configuration
├── db.py                  # database connection + helpers
├── main.py                # entry point
├── scanner.py             # bill scanning (Gemini Vision)
├── analyzer.py            # analysis engine (all checks)
├── validators/
│   ├── duplicates.py
│   ├── unbundling.py
│   ├── upcoding.py
│   └── pricing.py
├── api.py                 # FastAPI endpoints
├── templates/             # HTML templates if needed
├── data/
│   └── app.db             # SQLite database
├── reference/
│   ├── PRODUCT_CONTEXT.md
│   └── BILLING_RULES.md
├── tests/
│   ├── test_scanner.py
│   ├── test_analyzer.py
│   └── test_data/         # sample bills for testing
├── requirements.txt
└── README.md
```

Not this:

```
project/
├── src/
│   ├── core/
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   ├── value_objects/
│   │   │   └── interfaces/
│   │   ├── application/
│   │   │   ├── use_cases/
│   │   │   ├── services/
│   │   │   └── ports/
│   │   └── infrastructure/
│   │       ├── persistence/
│   │       ├── adapters/
│   │       └── factories/
```

## Common Mistakes to Avoid

1. **Don't build a framework.** You're building a product. Ship features, not abstractions.
1. **Don't add caching until you have a measured performance problem.** Premature caching creates bugs.
1. **Don't create base classes and interfaces for things that only have one implementation.** You'll never build that second implementation.
1. **Don't add type hints to the point of unreadability.** `def process(data: dict) -> dict` is fine. `def process(data: Mapping[str, Union[str, int, List[Optional[Tuple[str, ...]]]]) -> ProcessResult` is not.
1. **Don't refactor working code because it's "not clean enough."** If it works, is readable, and is tested — move on.
1. **Don't add logging for everything.** Log errors, log important state transitions, log nothing else.
1. **Don't create utility files that become junk drawers.** If `utils.py` has 20 unrelated functions, split them into the modules that actually use them.
1. **Don't write docstrings for obvious functions.** `get_user_by_id(user_id)` doesn't need a docstring. `calculate_unbundling_savings(items, ncci_edits)` does.
1. **Don't handle errors you can't do anything about.** If the database is down, crash. Don't write 50 lines of retry logic for a SQLite database running on the same machine.
1. **Don't create environment-specific config files for a single-environment app.** You're deploying to Railway. You don't need dev/staging/prod config classes.

## When in Doubt

- Fewer files is better than more files
- Fewer abstractions is better than more abstractions
- Fewer dependencies is better than more dependencies
- Readable code is better than clever code
- Working code is better than perfect code
- 80% solution shipped today beats 100% solution shipped never
