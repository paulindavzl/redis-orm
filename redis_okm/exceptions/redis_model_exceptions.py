class RedisModelAttributeException(Exception):
    """
    Non-existent attribute in the Model.
    """


class RedisModelTypeValueException(Exception):
    """
    Invalid attribute value.
    """


class RedisModelForeignKeyException(Exception):
    """
    Foreign Key error
    """


class RedisModelInvalidNomenclatureException(Exception):
    """
    The attribute naming is invalid.
    """