import json
import struct
import sys
from typing import BinaryIO

from citetrail.bridge import NativeBridge
from citetrail.capture import CaptureRequest
from citetrail.store import Store


def _read_message(stream: BinaryIO) -> dict[str, object] | None:
    length_bytes = stream.read(4)
    if not length_bytes:
        return None
    length = struct.unpack("<I", length_bytes)[0]
    return json.loads(stream.read(length))


def _write_message(stream: BinaryIO, payload: dict[str, object]) -> None:
    encoded = json.dumps(payload).encode()
    stream.write(struct.pack("<I", len(encoded)))
    stream.write(encoded)
    stream.flush()


def run(
    store: Store,
    input_stream: BinaryIO = sys.stdin.buffer,
    output_stream: BinaryIO = sys.stdout.buffer,
) -> None:
    bridge = NativeBridge()
    while payload := _read_message(input_stream):
        try:
            request = CaptureRequest(
                url=str(payload["url"]),
                title=str(payload["title"]),
                text=str(payload["text"]),
                captured_at=str(payload["captured_at"]),
            )
        except KeyError as error:
            _write_message(
                output_stream,
                {"status": "unavailable", "error": f"missing {error.args[0]}"},
            )
            continue
        result = bridge.capture(store, request, policy=store.privacy_policy())
        reference = result.capture.reference if result.capture else None
        _write_message(
            output_stream,
            {
                "status": result.status,
                "truncated": result.truncated,
                "gap": result.gap,
                "reference": (
                    {
                        "url": reference.url,
                        "title": reference.title,
                        "captured_at": reference.captured_at,
                        "position": reference.position,
                    }
                    if reference
                    else None
                ),
            },
        )
