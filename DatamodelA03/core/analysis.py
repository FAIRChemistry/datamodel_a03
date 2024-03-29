import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Analysis(sdRDM.DataModel):
    """Describes an anlysis that was performed for the COF preparation. Preliminary specification according to the example PDF provided.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Descriptive name of the analysis")

    location: str = Field(
        ..., description="Location were the results of the analysis can be retrieved"
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="fc9cdaaabba4884d1a0e974a7c6579f3a74a8252"
    )
