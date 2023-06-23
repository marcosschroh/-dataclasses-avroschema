import pydantic

pydantic_fields = (
    pydantic.FilePath,
    pydantic.DirectoryPath,
    pydantic.EmailStr,
    pydantic.NameEmail,
    pydantic.AnyUrl,
    pydantic.AnyHttpUrl,
    pydantic.HttpUrl,
    pydantic.FileUrl,
    pydantic.PostgresDsn,
    pydantic.CockroachDsn,
    pydantic.AmqpDsn,
    pydantic.RedisDsn,
    pydantic.MongoDsn,
    pydantic.KafkaDsn,
    pydantic.SecretStr,
    pydantic.IPvAnyAddress,
    pydantic.IPvAnyInterface,
    pydantic.IPvAnyNetwork,
    pydantic.NegativeFloat,
    pydantic.PositiveFloat,
    pydantic.NegativeInt,
    pydantic.PositiveInt,
    pydantic.UUID1,
    pydantic.UUID3,
    pydantic.UUID4,
    pydantic.UUID5,
)
