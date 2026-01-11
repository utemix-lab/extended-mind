# Cosmos Map Usage

Workflow:
1) Open Cosmos tab and switch to edit mode.
2) Make changes (nodes, edges, props).
3) Save draft locally (autosave) or export JSON.
4) Use Save to create a PR.

Draft + PR:
- Drafts are stored in localStorage for your browser.
- Save creates a PR in GitHub with the updated `cosmos-map.v0.2.json`.
- Requires Space secret `GH_TOKEN` with repo write access.

Props:
- Use Custom props to add structured fields.
- Keep `props_meta` aligned with `props` types.
