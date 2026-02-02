# License Layer Maintenance

This document defines how automated tools (IDE agents, scripts) should maintain the licensing and attribution layer.

## 1. Files to maintain

Tools SHOULD be aware of and help maintain:

- `LICENSE_CORE`  
- `LICENSE_CLIENTS`  
- `CONTENT_LICENSE.md`  
- `AUTHORS.md`  
- `THIRD_PARTY_NOTICES.md`

## 2. What tools MAY do automatically

- Check that the above files exist in the repository.  
- Propose additions to `THIRD_PARTY_NOTICES.md` when new third-party dependencies are detected.  
- Propose additions to `AUTHORS.md` based on significant contributions (to be confirmed by a human).  
- Add or update short license notes in `README` files inside subdirectories (e.g. “This module is licensed under AGPL-3.0, see LICENSE_CORE”).

## 3. What tools MUST NOT do automatically

- Change the type of license (e.g. AGPL -> Apache, or vice versa).  
- Remove existing authors or third-party notices.  
- Move code between core/clients/content layers without confirmation.

## 4. Folder classification rules

- If a new directory contains executable code or configuration that affects system behavior, it SHOULD be classified as either **core** or **client**, and linked to `LICENSE_CORE` or `LICENSE_CLIENTS` respectively.  
- If a new directory contains media, narratives, or identity assets, it SHOULD be classified as **content** and linked to `CONTENT_LICENSE.md`.

## 5. PR review assistance

During PR review, tools MAY:

- Classify changes by layer (core / clients / content).  
- Highlight potential license conflicts when new dependencies are added.  
- Suggest appropriate attribution entries for `AUTHORS.md` and `THIRD_PARTY_NOTICES.md`.  
- Help with partial merges by listing which files/commits belong to which layer.
