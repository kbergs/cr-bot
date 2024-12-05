# cr-bot

This bot is intended to be used to automate repetetive, daily tasks in CR. Use at your own risk.

## Setup

Currently, we only support macOS and iOS, running CR on iOS and using iPhone Mirroring on macOS.

### uv

This project uses uv to manage Python distributions and dependencies. To install uv on mac, consult the [guide]("https://docs.astral.sh/uv/getting-started/installation/"). After cloning the repo locally, run `uv sync` to install the necessary dependencies. Booting the GUI can be done using `uv run main.py`.