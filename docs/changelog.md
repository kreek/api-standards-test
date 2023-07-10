# Changelog

## 1.2.0 - 2023-07-10

- Added a [Defaults](./defaults/index.md) section which lists the default rate limit, timeout, and request size limit.
- 'Availability' is renamed ['Performance and Availability'](./general-guidelines/performance-and-availability.md) with details about expected performance and timeouts.
- Updated the [security section](./security/index.md#rate-limit) to reference the rate limit.

## 1.1.0 - 2023-06-23

- Moved the errors page to the top-level navigation and added a [required errors section](./errors/index.md#required-errors).
- Added API expectations that were on [developer.va.gov](https://developer.va.gov/) and not covered elsewhere in the standards:
  - SLAs for sandbox and production are listed on a new [availability page](./general-guidelines/performance-and-availability.md) within the general guidelines.
  - Updated the [architecture requirements](./general-guidelines/architecture.md) to include that APIs must be stateless, cache compatible, and able to work as part of a layered system.

## 1.0.0 - 2023-04-01

- Added a [monitoring section](./monitoring/index.md).
- Added an example OAS doc to [general-guidelines/documentation](./general-guidelines/documentation.md#example-oas-document).
<!-- markdown-link-check-disable -->
- Changed style to match VA Design System via [material-va-lighthouse plugin](https://github.com/department-of-veterans-affairs/material-va-lighthouse).
<!-- markdown-link-check-enable -->

## 0.1.0 - 2022-09-28

- Initial release.
