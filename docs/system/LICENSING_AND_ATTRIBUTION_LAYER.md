# Licensing and Attribution Layer

This document describes how licensing and attribution are structured across the project.

## Layers

The project is intentionally split into three main layers:

1. **Core (Orchestration, RAG, Agents)**  
   - License: GNU Affero General Public License v3.0 (AGPL-3.0).  
   - Files: everything under `core/` and other modules explicitly marked as part of the core engine.  
   - Purpose: ensure that improvements to the core remain open and available to the community, including in network-based usage.

2. **Clients and Integrations (SDKs, IDE plugins, adapters)**  
   - License: Apache License 2.0.  
   - Files: `clients/`, `plugins/ide/`, `sdk/` and similar.  
   - Purpose: make it easy to integrate the system into various tools and environments, including proprietary ones, while keeping the core protected.

3. **Content (Narratives, Worlds, Identity, Media)**  
   - License: see `CONTENT_LICENSE.md` (default: All Rights Reserved).  
   - Files: `content/`, `portfolio/`, `worlds/` and any other directories explicitly marked as containing creative assets.  
   - Purpose: protect authorial work, identity, and research output from uncontrolled reuse.

## Ownership

- Code in the **Core** and **Clients** layers is open source under the respective licenses.  
- Creative content is **not** open source by default and remains the property of its authors.

## Attributions

- Main authors are listed in `AUTHORS.md`.  
- Third-party libraries and projects are listed in `THIRD_PARTY_NOTICES.md`.  
- Within the content layer, metadata fields (`author`, `contributors`, etc.) SHOULD be used where possible.

## Invariants for tools and agents

Any automated tool or IDE-agent that modifies this repository SHOULD:

- Not change license types (AGPL/Apache/Content) without explicit human approval.  
- Respect the separation between code and content folders.  
- Update `THIRD_PARTY_NOTICES.md` when new third-party code is added.  
- Suggest updates to `AUTHORS.md` when a contributor’s impact becomes significant.
