
import typing

from ...types.business_sender_v2 import BusinessSenderV2
from ...types.individual_sender_v2 import IndividualSenderV2

CreateSendersRequest = typing.Union[IndividualSenderV2, BusinessSenderV2]
