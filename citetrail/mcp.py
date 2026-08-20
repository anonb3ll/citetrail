import json
import sys
from typing import TextIO

from citetrail.recall import recall
from citetrail.store import Store


def search_tool(store: Store, query: str, source_state: str = "available") -> dict[str, object]:
    result = recall(store, query, source_state=source_state)
    return {
        "status": result.status,
        "matches": [
            {
                "text": match.text,
                "reference": {
                    "url": match.reference.url,
                    "title": match.reference.title,
                    "captured_at": match.reference.captured_at,
                    "position": match.reference.position,
                },
            }
            for match in result.matches
        ],
    }


def run_stdio(
    store: Store, input_stream: TextIO = sys.stdin, output_stream: TextIO = sys.stdout
) -> None:
    for line in input_stream:
        request = json.loads(line)
        method = request.get("method")
        if method == "initialize":
            result: dict[str, object] = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "citetrail", "version": "0.1.0"},
            }
        elif method == "tools/list":
            result = {
                "tools": [
                    {
                        "name": "citetrail_search",
                        "description": "Search local captures with inseparable provenance.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string"},
                                "source_state": {
                                    "type": "string",
                                    "enum": [
                                        "available",
                                        "offline",
                                        "unavailable",
                                        "privacy-blocked",
                                    ],
                                },
                            },
                            "required": ["query"],
                        },
                    }
                ]
            }
        elif method == "tools/call" and request.get("params", {}).get("name") == "citetrail_search":
            arguments = request["params"]["arguments"]
            result = {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            search_tool(
                                store,
                                arguments["query"],
                                arguments.get("source_state", "available"),
                            )
                        ),
                    }
                ]
            }
        else:
            output_stream.write(
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "error": {"code": -32601, "message": "method not found"},
                    }
                )
                + "\n"
            )
            output_stream.flush()
            continue
        response = {"jsonrpc": "2.0", "id": request.get("id"), "result": result}
        output_stream.write(json.dumps(response) + "\n")
        output_stream.flush()
