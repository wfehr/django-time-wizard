=========
Changelog
=========

v4.1.0 (2025-02-04)
===================

- made holiday choices (countries) dynamic - no more migrations for updated
  dependencies
- updated handling for country/province - only holidays use a Javascript-request
  now
- removed version fixation for holidays dependency (at least v.0.23 required)

v4.0.1 (2025-01-15)
===================

- fixed typo in django requirement -> 5.1 is not yet tested

v4.0.0 (2025-01-15)
===================

- adjusted testing environment
- require minimum django 3.0 (older version are not tested)
- added support for django v5.0
- removed support for python 3.6 - 3.8 (may work, but not tested anymore)

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
