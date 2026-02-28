# AI Agent Guidelines

You are a senior Python developer writing code:
- idiomatic
- type-safe
- testable
- maintainable
- strictly follows the conventions of this project

## Project Configuration

- Read project configuration from `pyproject.toml`.
- Use modern Python features based on the `requires-python` setting.
- Respect tool configurations defined in `pyproject.toml` (ruff, pyright, etc.).

## Package Management

- This project uses **uv** for dependency management and running commands.
- Use `uv add <package>` to add dependencies.
- Use `uv add --group dev <package>` to add dev dependencies.
- Use `uv sync` to sync dependencies.
- Use `uv run <command>` to run tools (pytest, ruff, basedpyright, etc.).
- Use `uv pip install <package>` only if uv add is not suitable.

## Code Style

### PEP 8 Compliance

- Follow **PEP 8** style guidelines for all Python code.
- Use **ruff** to enforce PEP 8 compliance automatically.

### Comments and Documentation

- Write all comments and documentation in **English**.
- Use clear, concise language.

### Type Checking

- Fix type errors according to **basedpyright** recommendations.
- **Do not** use `# type: ignore` — solve the actual problem instead.
- For types imported only for type checking:
  - Use `if TYPE_CHECKING:` block for imports.
  - Use string literals (forward references) when applying these types.

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from some_module import SomeClass

def func(obj: "SomeClass") -> None:
    ...
```

### Formatting

- Format code and reorganize imports with **ruff** using settings from `pyproject.toml`.

## Testing

- Write tests for all new functionality; place them in the `tests/` directory mirroring the source structure.
- Use `pytest` fixtures for shared setup; avoid repetitive boilerplate in test functions.
- Mock external dependencies (HTTP calls, DB, filesystem) — tests must run offline and without side effects.
- Run tests with coverage to spot untested paths:
  ```bash
  uv run pytest --cov
  ```
- Prefer `assert` with descriptive messages over bare assertions.
- Test file names must start with `test_`, e.g. `test_utils.py`.

## Error Handling

- Use specific exception types instead of bare `except Exception`.
- Never silently swallow exceptions — log or re-raise them.
- Use `logging` (not `print`) for runtime diagnostics; configure it via `logging.getLogger(__name__)`.
- Do not use `print` for debug output in production code.

## Security & Secrets

- Never hard-code secrets, API keys, or passwords in source files.
- Read sensitive values from environment variables or a `.env` file (loaded via `python-dotenv` or similar).
- Add `.env` to `.gitignore`; provide a `.env.example` with placeholder values instead.

## Project Structure

- Follow the existing directory layout; do not create new top-level directories without discussion.
- Keep modules focused — one clear responsibility per file.
- Place shared utilities in a dedicated `utils` or `common` module rather than duplicating code.

## Workflow

### After Creating or Editing Files

Always run type checking and formatting after creating or modifying Python files:

1. **Fix imports and linting issues:**
   ```bash
   uv run ruff check <file_path> --fix
   ```
   This sorts imports (isort) and fixes other linting issues.

2. **Format the file:**
   ```bash
   uv run ruff format <file_path>
   ```

3. **Run type checker:**
   ```bash
   uv run basedpyright <file_path>
   ```

4. **Fix any errors** reported by basedpyright (do not use `# type: ignore`).

5. **Run tests** if the file is a test file or affects tested functionality:
   ```bash
   uv run pytest <test_file_or_path>
   ```

This ensures all code meets the project's quality standards before committing.

### Before Finishing a Task

- Confirm there are no outstanding linting, type, or test failures.
- Remove any debug prints or temporary code introduced during development.
- If you added a new dependency, verify it appears correctly in `pyproject.toml` and `uv.lock`.