# Contributing Guide

## Development Setup

### Prerequisites
- Python 3.9+
- pip or conda
- Git

### Installation

```bash
git clone https://github.com/Gourav-512/ai-image-analysis-api.git
cd ai-image-analysis-api
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running Tests

```bash
pytest tests/ -v
```

### Code Style

We use Black for code formatting and Pylint for linting:

```bash
black app/
pylint app/
```

## Commit Convention

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `test:` - Tests
- `perf:` - Performance improvement
- `refactor:` - Code refactoring
- `chore:` - Chores/maintenance

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "feat: add your feature"`
3. Push to branch: `git push origin feature/your-feature`
4. Create a Pull Request

## Code Review

All contributions require code review. Please ensure:
- Tests pass
- Code is formatted with Black
- Documentation is updated
