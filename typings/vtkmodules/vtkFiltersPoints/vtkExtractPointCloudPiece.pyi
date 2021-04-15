"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractPointCloudPiece(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkExtractPointCloudPiece - Return a piece of a point cloud
    
    Superclass: vtkPolyDataAlgorithm
    
    This filter takes the output of a vtkHierarchicalBinningFilter and
    allows the pipeline to stream it. Pieces are determined from an
    offset integral array associated with the field data of the input.
    """
    def GetModuloOrdering(self):
        """
        V.GetModuloOrdering() -> bool
        C++: virtual bool GetModuloOrdering()
        
        Turn on or off modulo sampling of the points. By default this is
        on and the points in a given piece will be reordered in an
        attempt to reduce spatial coherency.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def ModuloOrderingOff(self):
        """
        V.ModuloOrderingOff()
        C++: virtual void ModuloOrderingOff()
        
        Turn on or off modulo sampling of the points. By default this is
        on and the points in a given piece will be reordered in an
        attempt to reduce spatial coherency.
        """
        ...
    
    def ModuloOrderingOn(self):
        """
        V.ModuloOrderingOn()
        C++: virtual void ModuloOrderingOn()
        
        Turn on or off modulo sampling of the points. By default this is
        on and the points in a given piece will be reordered in an
        attempt to reduce spatial coherency.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkExtractPointCloudPiece
        C++: vtkExtractPointCloudPiece *NewInstance()
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractPointCloudPiece
        C++: static vtkExtractPointCloudPiece *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiation, printing, and type
        information.
        """
        ...
    
    def SetModuloOrdering(self, bool):
        """
        V.SetModuloOrdering(bool)
        C++: virtual void SetModuloOrdering(bool _arg)
        
        Turn on or off modulo sampling of the points. By default this is
        on and the points in a given piece will be reordered in an
        attempt to reduce spatial coherency.
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


