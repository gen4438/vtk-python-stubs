"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkPolyDataTangents(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkPolyDataTangents - compute tangents for triangulated polydata
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkPolyDataTangents is a filter that computes point and/or cell
    tangents for a triangulated polydata. This filter requires an input
    with both normals and tcoords on points.
    """
    def ComputeCellTangentsOff(self):
        """
        V.ComputeCellTangentsOff()
        C++: virtual void ComputeCellTangentsOff()
        
        Turn on/off the computation of cell tangents. Default is false.
        """
        ...
    
    def ComputeCellTangentsOn(self):
        """
        V.ComputeCellTangentsOn()
        C++: virtual void ComputeCellTangentsOn()
        
        Turn on/off the computation of cell tangents. Default is false.
        """
        ...
    
    def ComputePointTangentsOff(self):
        """
        V.ComputePointTangentsOff()
        C++: virtual void ComputePointTangentsOff()
        
        Turn on/off the computation of point tangents. Default is true.
        """
        ...
    
    def ComputePointTangentsOn(self):
        """
        V.ComputePointTangentsOn()
        C++: virtual void ComputePointTangentsOn()
        
        Turn on/off the computation of point tangents. Default is true.
        """
        ...
    
    def GetComputeCellTangents(self):
        """
        V.GetComputeCellTangents() -> bool
        C++: virtual bool GetComputeCellTangents()
        
        Turn on/off the computation of cell tangents. Default is false.
        """
        ...
    
    def GetComputePointTangents(self):
        """
        V.GetComputePointTangents() -> bool
        C++: virtual bool GetComputePointTangents()
        
        Turn on/off the computation of point tangents. Default is true.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPolyDataTangents
        C++: vtkPolyDataTangents *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPolyDataTangents
        C++: static vtkPolyDataTangents *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetComputeCellTangents(self, bool):
        """
        V.SetComputeCellTangents(bool)
        C++: virtual void SetComputeCellTangents(bool _arg)
        
        Turn on/off the computation of cell tangents. Default is false.
        """
        ...
    
    def SetComputePointTangents(self, bool):
        """
        V.SetComputePointTangents(bool)
        C++: virtual void SetComputePointTangents(bool _arg)
        
        Turn on/off the computation of point tangents. Default is true.
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

