"""
This type stub file was generated by pyright.
"""

from .vtkResliceCursorLineRepresentation import vtkResliceCursorLineRepresentation

class vtkResliceCursorThickLineRepresentation(vtkResliceCursorLineRepresentation):
    """
    vtkResliceCursorThickLineRepresentation - represents a thick slab of
    the reslice cursor widget
    
    Superclass: vtkResliceCursorLineRepresentation
    
    This class respresents a thick reslice cursor, that can be used to
    perform interactive thick slab MPR's through data. The class
    internally uses vtkImageSlabReslice to do its reslicing. The slab
    thickness is set interactively from the widget. The slab resolution
    (ie the number of blend points) is set as the minimum spacing along
    any dimension from the dataset.
    @sa
    vtkImageSlabReslice vtkResliceCursorLineRepresentation
    vtkResliceCursorWidget
    """
    def CreateDefaultResliceAlgorithm(self):
        """
        V.CreateDefaultResliceAlgorithm()
        C++: void CreateDefaultResliceAlgorithm() override;
        
        INTERNAL - Do not use Create the thick reformat class. This
        overrides the superclass implementation and creates a
        vtkImageSlabReslice instead of a vtkImageReslice.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkResliceCursorThickLineRepresentation
        C++: vtkResliceCursorThickLineRepresentation *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkResliceCursorThickLineRepresentation
        C++: static vtkResliceCursorThickLineRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetResliceParameters(self, p_float, p_float_1, p_int, p_int_1):
        """
        V.SetResliceParameters(float, float, int, int)
        C++: void SetResliceParameters(double outputSpacingX,
            double outputSpacingY, int extentX, int extentY) override;
        
        INTERNAL - Do not use Reslice parameters which are set from
        vtkResliceCursorWidget based on user interactions.
        """
        ...
    
    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    
    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    
    __this__ = ...
    __dict__ = ...
    __vtkname__ = ...


