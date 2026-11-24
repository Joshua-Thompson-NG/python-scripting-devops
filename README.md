# Python for DevOps Scripting

A 2-week practice repo for turning "I know Python" into "I reach for Python instead of Bash." Every day ends with a small, working script committed to this repo.

**Goal:** write clean, reusable, safe automation scripts: CLI tools that handle files, processes, APIs and failures properly.

**Rule:** Bash for one-liners and glue. Python for anything with logic, loops, data parsing or error handling.

## Repo layout

```
python-devops-scripting/
├── README.md
├── .gitignore
├── requirements.txt
├── week1/
│   ├── day01_cli_basics/
│   ├── day02_files_paths/
│   └── ...
├── week2/
│   └── ...
├── capstone/
```

## Week 1: The scripting toolkit

| Day | Topic | Learn | Mini project |
|-----|-------|-------|--------------|
| 1 | Script foundations | venv, `pip`, shebang, `if __name__ == "__main__"`, `sys.argv`, exit codes, `argparse` | `greet.py` with flags and proper exit codes |
| 2 | Files and paths | `pathlib`, `shutil`, `glob`, `tempfile`, reading and writing safely | Downloads-folder organizer (sort by extension, dry-run flag) |
| 3 | Running commands | `subprocess.run`, `check`, `capture_output`, `timeout`, `shlex`, never `shell=True` with user input | System info reporter wrapping `df`, `free`, `uptime` |
| 4 | Text and data formats | `re`, `json`, `csv`, `yaml` (PyYAML), `tomllib` | Log parser: count errors per hour from a sample log |
| 5 | Logging and CLI polish | `logging` (levels, formatters, file handlers), subcommands with `argparse` (or `typer`) | Refactor days 2-4 into one CLI with subcommands |
| 6 | HTTP and APIs | `requests`/`httpx`, headers, auth tokens, pagination, timeouts | Script that lists your GitHub repos via the API |
| 7 | Review | Clean up, add docstrings, write notes | Website health checker (status, latency, report to JSON) |

## Week 2: DevOps-flavored scripting

| Day | Topic | Learn | Mini project |
|-----|-------|-------|--------------|
| 8 | Reliability | Exceptions, `try/except/finally`, retries with backoff, context managers, idempotency | Add retry logic to the health checker |
| 9 | Config and secrets | `os.environ`, `python-dotenv`, config files, never hardcoding secrets | Make all scripts configurable via env and YAML |
| 10 | System and remote | `psutil`, `socket`, `platform`, SSH with `paramiko` or `fabric` | Run a command across several servers/VMs |
| 11 | Concurrency | `concurrent.futures` (ThreadPoolExecutor), intro to `asyncio` | Check 50 URLs or ports in parallel |
| 12 | Testing | `pytest`, fixtures, mocking `subprocess` and HTTP | Tests for your log parser and health checker |
| 13 | Packaging and quality | `pyproject.toml`, entry points, `ruff`, type hints, `Makefile` | Install a script as a real command (`pipx install .`) |
| 14 | Capstone | Combine everything | See below |

## Capstone ideas (pick one)

- **Server health monitor:** checks disk, memory, services and URLs, logs results, sends a Slack/Discord webhook on failure.
- **Backup tool:** archives directories, rotates old backups, verifies checksums, supports dry-run.
- **Log analyzer CLI:** parses nginx/auth logs, summarizes errors and suspicious IPs, outputs JSON or a table.

## Principles to practice

1. Every script supports `--help` and `--dry-run` where it changes things.
2. Meaningful exit codes (0 = ok, non-zero = failure).
3. Use `logging`, not `print`, for anything beyond a quick test.
4. Handle failures: timeouts, missing files, bad input.
5. No secrets in code or in git.

## Later in the roadmap

Boto3/cloud SDKs, Docker SDK and Ansible all build on these skills, so save them until after networking and Git.

## Progress

- [ ] Day 1
- [ ] Day 2
- [ ] Day 3
- [ ] Day 4
- [ ] Day 5
- [ ] Day 6
- [ ] Day 7
- [ ] Day 8
- [ ] Day 9
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12
- [ ] Day 13
- [ ] Day 14
- [ ] Capstone
