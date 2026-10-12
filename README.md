# taskcli

A simple command-line task tracker written in Python. No dependencies.

## Install

```bash
git clone https://github.com/<your-username>/taskcli.git
cd taskcli
pip install -e .
```

## Usage

```bash
taskcli add "Buy milk"
taskcli list
taskcli done 1
taskcli delete 1
```

Tasks are stored in `~/.taskcli.json`.

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT
