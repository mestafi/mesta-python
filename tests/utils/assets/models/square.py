

import typing_extensions

from mesta.core.serialization import FieldMetadata


class SquareParams(typing_extensions.TypedDict):
    length_measurement: typing_extensions.Annotated[float, FieldMetadata(alias="lengthMeasurement")]
