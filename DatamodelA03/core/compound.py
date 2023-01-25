import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import PositiveFloat


@forge_signature
class Compound(sdRDM.DataModel):
    """Describes a chemical compound. Preliminary specification according to the example PDF provided.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("compoundINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Descriptive name of the compound")

    quantity: Optional[str] = Field(
        description="Quantity of compound (N, m, V, ...)", default=None
    )

    inchi: Optional[str] = Field(
        description="InChI code that uniquely identifies the structure of a molecule",
        default=None,
    )

    cas_number: Optional[str] = Field(
        description=(
            "A CAS Registry Number also referred to as CAS RN or informally CAS Number,"
            " is a unique numerical identifier assigned by the Chemical Abstracts"
            " Service (CAS), US to every chemical substance described in the open"
            " scientific literature."
        ),
        default=None,
    )

    amount: Optional[PositiveFloat] = Field(
        description="Amount of the quantity of compound (numerical value)", default=None
    )

    unit: Optional[str] = Field(
        description="Unit of the quantity of compound (SI unit)", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="fc9cdaaabba4884d1a0e974a7c6579f3a74a8252"
    )
