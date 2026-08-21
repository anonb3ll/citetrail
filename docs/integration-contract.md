# Optional integration with Runroom

Citetrail and [Runroom](https://github.com/anonb3ll/runroom) are independent products. An optional
integration contract lives in the third repo
[citetrail-runroom-contract](https://github.com/anonb3ll/citetrail-runroom-contract):

- Spec: [CONTRACT.md](https://github.com/anonb3ll/citetrail-runroom-contract/blob/main/CONTRACT.md)
- Demo: `examples/demo.sh` in that repository
- Evidence kind: `citetrail-reference-v1`

Neither repo lists the other as a packaging dependency. The contract consumes
`citetrail_search` output and projects it into a governed Runroom run via
documented interfaces only — no shared database or ledger.
