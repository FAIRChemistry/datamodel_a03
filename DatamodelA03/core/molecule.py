import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from pydantic.types import PositiveFloat
from typing import Optional


class Molecule(sdRDM.DataModel):

    """Describes a molecule according to the PDF"""

    id: Optional[str] = Field(
        description="Unique identifier for a molecule/stock",
        default=None,
    )

    inchi: Optional[str] = Field(
        description="InChI code that uniquely identifies the structure of a molecule",
        default=None,
    )

    cas_number: Optional[str] = Field(
        description="A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature.",
        default=None,
    )

    used_mass: Optional[PositiveFloat] = Field(
        description="Mass that was weighed in and used in the experiment.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="13944dc93cd3f3cd0ca43f90838c16476cc85df0"
    )
