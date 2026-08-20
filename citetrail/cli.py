import argparse
import json
import os
from pathlib import Path
from typing import Sequence

from citetrail.mcp import run_stdio, search_tool
from citetrail.native_host import run as run_native_host
from citetrail.store import Store

DEFAULT_STORE = Path(os.environ.get("CITETRAIL_STORE", Path.home() / ".local/share/citetrail"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="citetrail")
    subcommands = parser.add_subparsers(dest="command", required=True)
    init = subcommands.add_parser("init", help="create a local Citetrail store")
    init.add_argument("--store", type=Path, default=DEFAULT_STORE)
    search = subcommands.add_parser("search", help="search a local Citetrail store")
    search.add_argument("query")
    search.add_argument("--store", type=Path, default=DEFAULT_STORE)
    block = subcommands.add_parser("block", help="add a hostname to the local blocklist")
    block.add_argument("host")
    block.add_argument("--store", type=Path, default=DEFAULT_STORE)
    mcp = subcommands.add_parser("mcp", help="run the local MCP server over standard input/output")
    mcp.add_argument("--store", type=Path, default=DEFAULT_STORE)
    mcp.add_argument("--stdio", action="store_true", required=True)
    native_host = subcommands.add_parser(
        "native-host", help="run the Chromium native-message capture endpoint"
    )
    native_host.add_argument("--store", type=Path, default=DEFAULT_STORE)
    args = parser.parse_args(argv)

    if args.command == "init":
        Store.create(args.store)
        print(f"Initialized local Citetrail store at {args.store}")
        return 0
    if args.command == "search":
        print(json.dumps(search_tool(Store.create(args.store), args.query), indent=2))
        return 0
    if args.command == "block":
        Store.create(args.store).block_host(args.host)
        print(f"Blocked {args.host}")
        return 0
    if args.command == "mcp":
        run_stdio(Store.create(args.store))
        return 0
    if args.command == "native-host":
        run_native_host(Store.create(args.store))
        return 0
    return 1
