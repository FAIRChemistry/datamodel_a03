import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .analysis import Analysis


class Step(sdRDM.DataModel):
    """Describes a part of a workflow that includes free text description as well as parameters that were
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stepINDEX"),
        xml="@id",
    )

    description: str = Field(..., description="Free text description of the step")

    analysis: Optional[Analysis] = Field(
        description="Analysis performed in the step", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e6210b0bb348d4e702c45e110ebed1af95ca0423"
    )
