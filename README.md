# Console Replica Functionality Guide

This project is a static mock of the OCI console. It focuses on a handful of Exadata
pages and does **not** implement real back-end services. Use this guide to understand
what is interactive today and what remains a visual placeholder.

## Global Navigation

- **Top nav bar / mega menu**: The hamburger button opens a mocked mega menu. Links
  point to the static pages in this repo; most nested links are placeholders.
- **Profile/Help/Region buttons**: Decorative only.
- **Search bar**: Non-functional.
- **Announcements / Dev tools icons**: Non-functional.

## Exadata VM Clusters List (`exadbd.html`)

- **Cluster table**: Static data. The “SSOExaVMCluster” row links to the detail
  template (`vm-cluster-template.html?id=ssoexavmcluster`). Other rows link to the
  same template with different IDs but currently reuse mocked data.
- **Sorting / filters / search**: Visual only.
- **Row action menu (⋮)**: Decorative.
- **Create Exadata VM cluster button**: Non-functional.

## VM Cluster Detail (`vm-cluster-template.html`)

- **URL parameter**: The page reads `?id=<clusterId>` to select mocked cluster data.
  Supported IDs:
  - `ssoexavmcluster`
  - `vmcluster-202601141706`
  - `vmcluster-2025082110355n`
  - `vmcluster-202507281139`
  - `vmcluster-202503311639`
- **Header**: Name, status badge, Actions dropdown, and Scale button are visual only.
- **Copy buttons**: OCID and network fields include “Copy” buttons that write the value
  to the clipboard.
- **General information / Network / Storage cards**: Render mocked values depending on
  the cluster ID.
- **Tabs (Databases, Virtual Machines, etc.)**: Currently show placeholder content.
- **Actions dropdown**: Non-functional.

## Exadata VM Clusters (Cloud@Customer) (`exadbcc.html`) and Exascale (`exadbxs.html`)

- Follow the same interaction model as `exadbd.html`. Tables and filters are static.
- Navigation links jump between the static HTML files in this project.

## Base DB (`basedb.html`) and Home Page (`index.html`)

- These pages are visual mockups. Buttons, links, and filters do not trigger behaviour
  beyond simple anchor navigation when URLs are provided.

## Styling & Data Notes

- **Session storage**: When you open a VM cluster detail page from the list, the mocked
  data is cached in `sessionStorage` for the duration of the browser session. Refreshing
  clears any temporary changes.
- **No back-end**: All data is hard-coded in the HTML/JS. There is no API or persistence
  beyond the optional session storage described above.

## Known Limitations

- Tabs beyond “VM Cluster information” are placeholders.
- Table rows cannot be sorted or filtered.
- The “Create” button and “Actions” menus are non-functional.
- Navigation icons (profile, help, region) do not open menus.
- No authentication, security, or real API calls are implemented.

Use this documentation when exploring or extending the mock so you know which elements
are interactive and which are purely visual.
