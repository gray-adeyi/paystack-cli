# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - May 11, 2024

### Fixed

- All request errors exits gracefully with exit code 1.

### Changed

- `--data-only` flag of all sub-commands now return json data
- Upgrade `pypaystack2` to `2.0.3`
- Upgrade `typer` to `0.12.3`
- Switched from poetry to rye

## [0.1.4] - Dec 1, 2023

### Fixed

- Incorrect project versioning

## [0.1.3] - Jul 29, 2023

### Fixed

- Incorrect binary link

## [0.1.2] - Jul 26, 2023

### Fixed

- Missing options for `paystack misc get-providers` sub-command
- Missing options for `paystack misc get-banks` sub-command
- Missing options for `paystack misc get-states` sub-command
- Missing options for `paystack transfer-ctrl resend-otp` sub-command

## [0.1.1] - Jul 24, 2023

### Added

- License to project
- Source code link to README

### Changed

- Binary download link

## [0.1.0] - Jul 24, 2023

### Added

- Commands and sub-commands for all methods supported by `pypaystack2`

[unreleased]: https://github.com/gray-adeyi/paystack-cli/compare/v0.1.4...HEAD

[0.2.0]: https://github.com/gray-adeyi/paystack-cli/compare/v0.1.4...v0.2.0

[0.1.4]: https://github.com/gray-adeyi/paystack-cli/compare/0.1.3...v0.1.4

[0.1.3]: https://github.com/gray-adeyi/paystack-cli/compare/0.1.2...0.1.3

[0.1.2]: https://github.com/gray-adeyi/paystack-cli/compare/0.1.1...0.1.2

[0.1.1]: https://github.com/gray-adeyi/paystack-cli/compare/0.1.0...0.1.1

[0.1.0]: https://github.com/gray-adeyi/paystack-cli/releases/tag/0.1.0
