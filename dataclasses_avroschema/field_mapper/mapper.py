from .base_mapper import (
    BASE_CONTAINER_FIELDS_CLASSES,
    BASE_INMUTABLE_FIELDS_CLASSES,
    BASE_LOGICAL_TYPES_FIELDS_CLASSES,
    SPECIAL_ANNOTATED_TYPES,  # noqa: 401
)

INMUTABLE_FIELDS_CLASSES = BASE_INMUTABLE_FIELDS_CLASSES
CONTAINER_FIELDS_CLASSES = BASE_CONTAINER_FIELDS_CLASSES
LOGICAL_TYPES_FIELDS_CLASSES = BASE_LOGICAL_TYPES_FIELDS_CLASSES

try:
    from .pydantic_mapper import (
        PYDANTIC_CONTAINER_FIELDS_CLASSES,
        PYDANTIC_INMUTABLE_FIELDS_CLASSES,
    )

    INMUTABLE_FIELDS_CLASSES.update(PYDANTIC_INMUTABLE_FIELDS_CLASSES)
    CONTAINER_FIELDS_CLASSES.update(PYDANTIC_CONTAINER_FIELDS_CLASSES)
    LOGICAL_TYPES_FIELDS_CLASSES.update(PYDANTIC_INMUTABLE_FIELDS_CLASSES)
except ImportError:  # type: ignore # pragma: no cover
    ...
