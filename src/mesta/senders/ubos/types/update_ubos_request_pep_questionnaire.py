
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_ubos_request_pep_questionnaire_association import UpdateUbosRequestPepQuestionnaireAssociation
from .update_ubos_request_pep_questionnaire_declaration_type import UpdateUbosRequestPepQuestionnaireDeclarationType
from .update_ubos_request_pep_questionnaire_self import UpdateUbosRequestPepQuestionnaireSelf


class UpdateUbosRequestPepQuestionnaire(UniversalBaseModel):
    """
    Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.
    """

    declaration_type: typing_extensions.Annotated[
        typing.Optional[UpdateUbosRequestPepQuestionnaireDeclarationType],
        FieldMetadata(alias="declarationType"),
        pydantic.Field(alias="declarationType", description="PEP declaration type."),
    ] = None
    """
    PEP declaration type.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[UpdateUbosRequestPepQuestionnaireSelf],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="Required when declarationType is SELF."),
    ] = None
    """
    Required when declarationType is SELF.
    """

    association: typing.Optional[UpdateUbosRequestPepQuestionnaireAssociation] = pydantic.Field(default=None)
    """
    Required when declarationType is IMMEDIATE_FAMILY or CLOSE_ASSOCIATE.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
