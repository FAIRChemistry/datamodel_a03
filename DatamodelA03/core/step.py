import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Step(sdRDM.DataModel):

    """Describes a part of a workflow that includes free text description as well as parameters that were"""

    description: Optional[str] = Field(
        description="Free text description of the step",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="13944dc93cd3f3cd0ca43f90838c16476cc85df0"
    )
