=========
Changelog
=========

v3.0.2 (2023-09-28)
===================

- added `AppConfig.default_auto_field` to lock ID-fields in order to avoid
  migrations if projects use a different field in their settings

v3.0.1 (2023-01-13)
===================

- added missing migration due to updated `holidays` version
- fixed `holidays` on version `0.18` -> newer versions may result in new
  migrations which may be problematic if this app is integrated as a
  third-party-app

v3.0.0 (2023-01-13)
===================

- updated the testing environment
- dropped django<3.0 support
- added support for django 4.0 and 4.1
- enabled newer versions for `holidays` dependency
