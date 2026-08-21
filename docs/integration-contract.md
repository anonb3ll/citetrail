# Optional integration with Runroom

Citetrail and [Runroom](../../runroom) are independent products. An optional
integration contract lives in the third repo
[`integration-contract`](../../integration-contract):

- Spec: [`integration-contract/CONTRACT.md`](../../integration-contract/CONTRACT.md)
- Demo: `integration-contract/examples/demo.sh`
- Evidence kind: `citetrail-reference-v1`

Neither repo lists the other as a packaging dependency. The contract consumes
`citetrail_search` output and projects it into a governed Runroom run via
documented interfaces only — no shared database or ledger.
