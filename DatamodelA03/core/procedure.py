import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .analysis import Analysis
from .step import Step


@forge_signature
class Procedure(sdRDM.DataModel):

    """Describes a procedure that was applied for a particular part of the COF preparation or the preparation as whole. Preliminary specification according to the example PDF provided.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("procedureINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Descriptive name of the method (e.g. work-up)",
    )

    steps: List[Step] = Field(
        description="Independent steps that make up the procedure",
        default_factory=ListPlus,
    )

    reference: Optional[str] = Field(
        description=(
            "Reference to the original publication from which the method was adapted"
            " from."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e6210b0bb348d4e702c45e110ebed1af95ca0423"
    )

    def add_to_steps(
        self,
        description: str,
        analysis: Optional[Analysis] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Step' to the attribute 'steps'.

        Args:
            id (str): Unique identifier of the 'Step' object. Defaults to 'None'.
            description (str): Free text description of the step.
            analysis (Optional[Analysis]): Analysis performed in the step. Defaults to None
        """

        params = {
            "description": description,
            "analysis": analysis,
        }

        if id is not None:
            params["id"] = id

        steps = [Step(**params)]

        self.steps = self.steps + steps
