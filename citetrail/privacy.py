from collections.abc import Mapping
from dataclasses import dataclass, field
from urllib.parse import urlparse


@dataclass(frozen=True)
class PrivacyPolicy:
    blocked_hosts: frozenset[str] = field(default_factory=frozenset)
    rules_available: bool = True

    @classmethod
    def from_mapping(cls, values: Mapping[str, object]) -> "PrivacyPolicy":
        blocked_hosts = values.get("blocked_hosts", [])
        if not isinstance(blocked_hosts, list) or not all(
            isinstance(host, str) for host in blocked_hosts
        ):
            return cls(rules_available=False)
        return cls(blocked_hosts=frozenset(host.lower() for host in blocked_hosts))

    def allows(self, url: str) -> bool:
        if not self.rules_available:
            return False
        host = urlparse(url).hostname
        return host is not None and host.lower() not in self.blocked_hosts
