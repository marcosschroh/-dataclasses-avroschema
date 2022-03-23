# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.27.2] - 2022-03-23

### Fixed

- Generate wheel package [162](https://github.com/marcosschroh/dataclasses-avroschema/pull/162)

## [0.27.1] - 2022-03-22

### Fixed

- bump `fastavro` from 1.4.9 to 1.4.10
- bump `inflect` from 5.3.0 to 5.4.0 

## [0.27.0] - 2022-02-18

### Added

- `types.Enum` replaced by `enum.Enum` [153](https://github.com/marcosschroh/dataclasses-avroschema/pull/153/files)

## [0.26.1] - 2021-12-07

### Fixed

- Use root reference to generate valid schemas in multiple inheritance levels [148](https://github.com/marcosschroh/dataclasses-avroschema/pull/148)

## [0.26.0] - 2021-12-06

### Added

- `validate` method added to `AvroModel` [144](https://github.com/marcosschroh/dataclasses-avroschema/pull/144)

## [0.25.3] - 2021-11-26

### Fixed

- Generate valid avro schemas when inheritance has multiple levels [140](https://github.com/marcosschroh/dataclasses-avroschema/pull/140)

## [0.25.2] - 2021-10-09

### Fixed

- api `get_fields` now returns all rendered fields [134](https://github.com/marcosschroh/dataclasses-avroschema/pull/134)

## [0.25.1] - 2021-10-09

### Fixed

- Support for default `null` decimals added [130](https://github.com/marcosschroh/dataclasses-avroschema/pull/130)

## [0.25.0] - 2021-09-27

### Added

- New style type annotations support added (`tuple`, `list` and `dict`) [122](https://github.com/marcosschroh/dataclasses-avroschema/pull/122)
- Case schemas added [95](https://github.com/marcosschroh/dataclasses-avroschema/pull/95)

Available cases:

|Case| Example|
|----|--------|
|camelcase |'foo_bar_baz' # => "fooBarBaz"|
|capitalcase|'foo_bar_baz' # => "Foo_bar_baz"|
|constcase|'FooBarBaz' # => "_FOO_BAR_BAZ"|
|lowercase|'FooBarBaz' # => "foobarbaz"|
|pascalcase|'FooBarBaz' # => "FooBarBaz"|
|pathcase|'foo_bar_baz' # => "foo/bar/baz"|
|snakecase|'FooBarBaz' # => "foo_bar_baz"|
|spinalcase|'FooBarBaz' # => "-foo-bar-baz"|
|trimcase|'FooBarBaz' # => "FooBarBaz"|
|uppercase|'FooBarBaz' # => "FOOBARBAZ|
|alphanumcase|'Foo_123 Bar!' # =>'Foo123Bar'|

## [0.24.0] - 2021-09-24

### Added

- `int` and `float` Avro type support [119](https://github.com/marcosschroh/dataclasses-avroschema/pull/119)

## [0.23.2] - 2021-09-04

### Fixed

- Use `namespaces` on repeated user types with complex types [117](https://github.com/marcosschroh/dataclasses-avroschema/pull/117)

## [0.23.1] - 2021-09-03

### Fixed

- Use `namespaces` for repeated types in arrays and maps [116](https://github.com/marcosschroh/dataclasses-avroschema/pull/116)

## [0.23.0] - 2021-08-26

### Added

- Use `namespaces` for repeated types [115](https://github.com/marcosschroh/dataclasses-avroschema/pull/115)
- Record names now are generated using `class.__name__` instead of `class.__name__.lower()_record`

## [0.22.1] - 2021-07-05

### Fixed

- Cleanup [112](https://github.com/marcosschroh/dataclasses-avroschema/pull/112)

## [0.22.0] - 2021-07-01

### Added

- Alias for nested items (`nested records`, `arrays` and `maps`) [110](https://github.com/marcosschroh/dataclasses-avroschema/pull/110)
- Improve type annotations [109](https://github.com/marcosschroh/dataclasses-avroschema/pull/109)

## [0.21.0] - 2021-06-17

### Added

- Mitration to GithubCI
- `GenericAlias` test in Python `3.9`
- Add Python `3.8` and `3.9` in the `CI build`
- Add `schema_name` attribute to `SchemaMetadata`
- Add optional writer_schema in `deserialization`

### Added

## [0.20.4] - 2021-05-05

### Fixed

- Unpin install_requires with version ranges [99](https://github.com/marcosschroh/dataclasses-avroschema/pull/99)

## [0.20.3] - 2021-04-29

### Fixed

- Improve error message in unknown type: https://github.com/marcosschroh/dataclasses-avroschema/issues/88
- dependencies updated

## [0.20.2] - 2021-01-27

### Fixed

- avro-json serialization with defaults [89](https://github.com/marcosschroh/dataclasses-avroschema/pull/89)

## [0.20.1] - 2020-12-04

### Fixed

- Correct out-of-spec Avro schemas with typing.Union [#87](https://github.com/marcosschroh/dataclasses-avroschema/pull/87)

## [0.20.0] - 2020-11-24

### Added

- Support for decimal logical type added [#86](https://github.com/marcosschroh/dataclasses-avroschema/pull/86)

## [0.19.0] - 2020-11-12

### Added

- Default Avro type for Python ints has been changed from `int` to `long` and `float` to `double` [83](https://github.com/marcosschroh/dataclasses-avroschema/pull/83). Reason:
  - [Integers have unlimited precision](https://docs.python.org/3.4/library/stdtypes.html#typesnumeric)
  - Floating point numbers are usually implemented using `double` in C
  - [almost all platforms map Python floats to IEEE-754 `double` precision](https://docs.python.org/3/tutorial/floatingpoint.html#representation-error)

## [0.18.0] - 2020-10-10

### Added

- Allow multiple references to the same class in record relationships
- Correct name generation for nested records [81](https://github.com/marcosschroh/dataclasses-avroschema/pull/81)

## [0.17.0] - 2020-09-04

### Added

- Fake instances generation added

## [0.16.0] - 2020-08-27

### Added

- Deserialization process generate class instances instead a pythn dict
- In order to get a python dict in the deserialiation process the flag `create_instance=False` should be used
- Example with usage with kafka drivers added

## [0.15.2] - 2020-08-25

### Fixed

- `pytz` added as requirement

## [0.15.1] - 2020-08-22

### Fixed

- `UUID` type fixed

## [0.15.0] - 2020-08-16

### Added

- replaced `null` string with `avro null` (json)
- code improvement

## [0.14.6] - 2020-07-11

### Changed

- `SelfReferenceField` when is used inn `array` and `maps`
- `SelfReferenceField` default value fixed

## [0.14.5] - 2020-07-09

### Changed

- `null` should not be included when a default value is defined for premitive types

## [0.14.4] - 2020-07-03

### Changed

- `typing.Optional` union fixed
- `typing.Union` with complex types (sequeces and Dict) fixed

## [0.14.3] - 2020-06-29

### Changed

- documentation of `dataclasses.field` descriptor added
- support for aware datetime added
- `serialization` fixed for complex types

## [0.14.2] - 2020-06-16

### Changed

- `to_json` method fixed. [issue 47](https://github.com/marcosschroh/dataclasses-avroschema/issues/47)

## [0.14.1] - 2020-06-09

### Changed

- bytes type fixed
- null with Schema Logical Types and Relationships supported

## [0.14.0] - 2020-06-01

### Added

- inheritance approach adopted over composition

### Removed

- SchemaGenerator class

## [0.13.1] - 2020-05-29

### Changed

- `enum` type now is represented by `types.Enum`

## [0.13.0] - 2020-05-28

### Added

- json payload generated from class instance

## [0.12.0] - 2020-05-25

### Added

- import of SchemaGenetor improved
- Documentation updated

## [0.11.0] - 2020-05-20

### Added

- Serialization/deserialization added

## [0.10.0] - 2020-02-16

### Added

- fixed type support

## [0.9.0] - 2020-01-24

### Added

- Ability to store metadata into fields
- More type checks
- isort package added

## [0.8.0] - 2020-01-06

### Added

- Support `typing.Optional` added

## [0.7.4] - 2019-11-21

### Changed

- Union types can be included in sequences types

## [0.7.3] - 2019-11-16

### Changed

- Logical types now are allowed in Sequences and Maps

## [0.7.2] - 2019-11-07

### Changed

- Union type now allows logical and primitive types

## [0.7.1] - 2019-10-21

### Changed

- Support for Sequences and Mappings added

| Avro Type | Python Type |
|-----------|-------------|
| arrays    |   typing.Sequence, typing.MutableSequence      |
| maps      |  typing.Mapping, typing.MutableMapping      |

## [0.7.0] - 2019-10-23

### Added

- Faust support: Now is possible to generate Avro Schemas from a Faust Records

## [0.6.1] - 2019-10-21

### Changed

- Now default values are validated according to the field type

## [0.6.0] - 2019-10-17

### Added

- Avro Union support added

## [0.5.0] - 2019-10-13

### Added

- Support for some logical types

| Avro Type | Logical Type |Python Type |
|-----------|--------------|-------------|
| int       |  date        | datetime.date
| int       |  time-millis | datetime.time     |
| long      |  timestamp-millis | datetime.datetime |
| string    |  uuid        | uuid.uuid4 |

## [0.4.1] - 2019-10-11

### Changed

- Code refactor: Field have been devided into several field classes to make the code more redeable

## [0.4.0] - 2019-09-02

### Added

- Recursive Schema Relationships:
  - Recursive OneToOne relationship added
  - Recursive OneToMany relationship added

## [0.3.0] - 2019-09-05

### Changed

- Code refator and improvements

## [0.3.0] - 2019-09-03

### Added

- Singular name for array's child name
- Singular name for map's child name
- Singular name for nested relationship OneToMany

## [0.2.0] - 2019-09-02

### Added

- Schema Relationships:
  - OneToOne relationship added
  - OneToMany relationship added (array and map)

## [0.1.1] - 2019-09-02

### Added

- Enum, Array and Map fields fixed
- Schema Parse tests added using fastavro

## [0.1.0] - 2019-08-29

### Added

- First release
