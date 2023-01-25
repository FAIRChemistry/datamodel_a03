import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from pydantic.types import PositiveFloat
from sdRDM.base.utils import forge_signature, IDGenerator
from .positivefloat import PositiveFloat
from .step import Step
from .analysis import Analysis
from .compound import Compound
from .procedure import Procedure


class Report(sdRDM.DataModel):
    """Reports on a chemical experiment, that includes Reactants and Reactants as well as the method. The Data model will natively be exported to the AnIML data format used to track data from analytical instruments.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reportINDEX"),
        xml="@id",
    )

    products: List[Compound] = Field(
        description="List of products resulting from the COF preparation",
        default_factory=ListPlus,
    )

    reactants: List[Compound] = Field(
        description="List of reagents that were used in the COF preparation",
        default_factory=ListPlus,
    )

    solvents: List[Compound] = Field(
        description="List of solvents that were used in the COF preparation",
        default_factory=ListPlus,
    )

    procedures: List[Procedure] = Field(
        description="List of procedures that were applied to the COF preparation",
        default_factory=ListPlus,
    )

    observations: Optional[str] = Field(
        description="Free text for noting observations during the COF preparation",
        default=None,
    )

    analyses: List[Analysis] = Field(
        description="Analyses that were performed for the COF preparation",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e6210b0bb348d4e702c45e110ebed1af95ca0423"
    )

    def add_to_products(
        self,
        name: str,
        inchi: Optional[str] = None,
        cas_number: Optional[str] = None,
        quantity: Optional[str] = None,
        amount: Optional[PositiveFloat] = None,
        unit: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Compound' to the attribute 'products'.

        Args:


            id (str): Unique identifier of the 'Compound' object. Defaults to 'None'.


            name (str): Descriptive name of the compound.


            inchi (Optional[str]): InChI code that uniquely identifies the structure of a molecule. Defaults to None


            cas_number (Optional[str]): A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature. Defaults to None


            quantity (Optional[str]): Quantity of compound (N, m, V, ..). Defaults to None


            amount (Optional[PositiveFloat]): Amount of the quantity of compound (numerical value). Defaults to None


            unit (Optional[str]): Unit of the quantity of compound (SI unit). Defaults to None
        """

        params = {
            "name": name,
            "inchi": inchi,
            "cas_number": cas_number,
            "quantity": quantity,
            "amount": amount,
            "unit": unit,
        }
        if id is not None:
            params["id"] = id
        products = [Compound(**params)]
        self.products = self.products + products

    def add_to_reactants(
        self,
        name: str,
        inchi: Optional[str] = None,
        cas_number: Optional[str] = None,
        quantity: Optional[str] = None,
        amount: Optional[PositiveFloat] = None,
        unit: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Compound' to the attribute 'reactants'.

        Args:


            id (str): Unique identifier of the 'Compound' object. Defaults to 'None'.


            name (str): Descriptive name of the compound.


            inchi (Optional[str]): InChI code that uniquely identifies the structure of a molecule. Defaults to None


            cas_number (Optional[str]): A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature. Defaults to None


            quantity (Optional[str]): Quantity of compound (N, m, V, ..). Defaults to None


            amount (Optional[PositiveFloat]): Amount of the quantity of compound (numerical value). Defaults to None


            unit (Optional[str]): Unit of the quantity of compound (SI unit). Defaults to None
        """

        params = {
            "name": name,
            "inchi": inchi,
            "cas_number": cas_number,
            "quantity": quantity,
            "amount": amount,
            "unit": unit,
        }
        if id is not None:
            params["id"] = id
        reactants = [Compound(**params)]
        self.reactants = self.reactants + reactants

    def add_to_solvents(
        self,
        name: str,
        inchi: Optional[str] = None,
        cas_number: Optional[str] = None,
        quantity: Optional[str] = None,
        amount: Optional[PositiveFloat] = None,
        unit: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Compound' to the attribute 'solvents'.

        Args:


            id (str): Unique identifier of the 'Compound' object. Defaults to 'None'.


            name (str): Descriptive name of the compound.


            inchi (Optional[str]): InChI code that uniquely identifies the structure of a molecule. Defaults to None


            cas_number (Optional[str]): A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature. Defaults to None


            quantity (Optional[str]): Quantity of compound (N, m, V, ..). Defaults to None


            amount (Optional[PositiveFloat]): Amount of the quantity of compound (numerical value). Defaults to None


            unit (Optional[str]): Unit of the quantity of compound (SI unit). Defaults to None
        """

        params = {
            "name": name,
            "inchi": inchi,
            "cas_number": cas_number,
            "quantity": quantity,
            "amount": amount,
            "unit": unit,
        }
        if id is not None:
            params["id"] = id
        solvents = [Compound(**params)]
        self.solvents = self.solvents + solvents

    def add_to_procedures(
        self,
        name: str,
        steps: List[Step],
        reference: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Procedure' to the attribute 'procedures'.

        Args:


            id (str): Unique identifier of the 'Procedure' object. Defaults to 'None'.


            name (str): Descriptive name of the method (e.g. work-up).


            steps (List[Step]): Independent steps that make up the procedure.


            reference (Optional[str]): Reference to the original publication from which the method was adapted from. Defaults to None
        """

        params = {"name": name, "steps": steps, "reference": reference}
        if id is not None:
            params["id"] = id
        procedures = [Procedure(**params)]
        self.procedures = self.procedures + procedures

    def add_to_analyses(
        self, name: str, location: str, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Analysis' to the attribute 'analyses'.

        Args:


            id (str): Unique identifier of the 'Analysis' object. Defaults to 'None'.


            name (str): Descriptive name of the analysis.


            location (str): Location were the results of the analysis can be retrieved.
        """

        params = {"name": name, "location": location}
        if id is not None:
            params["id"] = id
        analyses = [Analysis(**params)]
        self.analyses = self.analyses + analyse


s
