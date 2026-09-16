
import typing

from ...types.patch_business_sender import PatchBusinessSender
from ...types.patch_individual_sender import PatchIndividualSender

UpdateSendersRequestBody = typing.Union[PatchIndividualSender, PatchBusinessSender]
