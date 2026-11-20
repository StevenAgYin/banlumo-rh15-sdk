# Banlumo RH15 SDK

Selected C/C++ ROS 2 source and English integration notes for a 15-motor hand.

**Development source preview — not a standalone, tested SDK.**

## Contact Banlumo

For product selection and technical coordination: **yinaiguo@gmail.com** · https://www.banlumo.com/

Confirm the exact commercial model, left/right side, hardware revision, firmware and matching software with Banlumo. RH15 is the source package designation; it is not proof of compatibility with a similarly named RY-H product. No hardware or production performance has been validated by Banlumo.

## Contents

ROS 2 controller/kinematics sources, command and feedback interfaces, launch files and model descriptions from explicitly Apache-licensed packages. Runtime package names and protocols are preserved.

## Important build limitations

The upstream CMake build expects separately supplied vendor shared libraries and headers. They are **not included** because their redistribution terms have not been established. CAD meshes and unrelated folders are also omitted. A full workspace build will require those prerequisites; model visuals may be unavailable. Do not describe this repository as plug-and-play or ready for hardware use.

Run offline structural checks without importing or launching controllers:

```bash
python3 tools/validate_source.py
```

Do not run a motion test until wiring, mounting, supply, command units, current/force limits, feedback and stopping arrangements have been confirmed for the exact unit. See [integration checklist](docs/INTEGRATION.md).

## ROS 1

Public ROS 1 resources exist, but their full license notices and configuration mapping require clarification. ROS 1 code is not mirrored in this release. Contact Banlumo to discuss a ROS 1 requirement; availability and tested compatibility are not promised.

## License and provenance

Imported packages explicitly declare Apache License 2.0 in package.xml. Only that declared package scope is used; no license is inferred for the entire upstream repository. See [LICENSE](LICENSE), [NOTICE](NOTICE) and [UPSTREAM.json](UPSTREAM.json). Banlumo changes are listed in [CHANGELOG.md](CHANGELOG.md). Third-party dependencies and separately obtained binaries retain their own licenses.
