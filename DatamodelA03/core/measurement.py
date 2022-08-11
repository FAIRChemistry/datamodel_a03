import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from pydantic.types import PositiveFloat
from typing import Optional


class Measurement(sdRDM.DataModel):

    """Describes a measurement that was made in a chemical experiment."""

    entry_id: Optional[str] = Field(
        description="Unique identifier of the measurement",
        default=None,
    )

    product_yield: Optional[PositiveFloat] = Field(
        description="Documented yield in mg",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="13944dc93cd3f3cd0ca43f90838c16476cc85df0"
    )
