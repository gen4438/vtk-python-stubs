"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkBooleanOperationPolyDataFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkBooleanOperationPolyDataFilter - Computes the boundary of the
    union, intersection, or difference volume computed from the volumes
    defined by two input surfaces.
    
    Superclass: vtkPolyDataAlgorithm
    
    The two surfaces do not need to be manifold, but if they are not,
    unexpected results may be obtained. The resulting surface is
    available in the first output of the filter. The second output
    contains a set of polylines that represent the intersection between
    the two input surfaces.
    
    @warning This filter is not designed to perform 2D boolean
        operations,
    and in fact relies on the inputs having no co-planar, overlapping
    cells.
    
    This code was contributed in the VTK Journal paper: "Boolean Operations on Surfaces in VTK Without External
    Libraries" by Cory Quammen, Chris Weigle C., Russ Taylor
    http://hdl.handle.net/10380/3262
    http://www.midasjournal.org/browse/publication/797
    """
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
    
    def GetOperation(self):
        """
        V.GetOperation() -> int
        C++: virtual int GetOperation()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def GetOperationMaxValue(self):
        """
        V.GetOperationMaxValue() -> int
        C++: virtual int GetOperationMaxValue()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def GetOperationMinValue(self):
        """
        V.GetOperationMinValue() -> int
        C++: virtual int GetOperationMinValue()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def GetReorientDifferenceCells(self):
        """
        V.GetReorientDifferenceCells() -> int
        C++: virtual vtkTypeBool GetReorientDifferenceCells()
        
        Turn on/off cell reorientation of the intersection portion of the
        surface when the operation is set to DIFFERENCE. Defaults to on.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Set/get the tolerance used to determine when a point's absolute
        distance is considered to be zero. Defaults to 1e-6.
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
        V.NewInstance() -> vtkBooleanOperationPolyDataFilter
        C++: vtkBooleanOperationPolyDataFilter *NewInstance()
        """
        ...
    
    def ReorientDifferenceCellsOff(self):
        """
        V.ReorientDifferenceCellsOff()
        C++: virtual void ReorientDifferenceCellsOff()
        
        Turn on/off cell reorientation of the intersection portion of the
        surface when the operation is set to DIFFERENCE. Defaults to on.
        """
        ...
    
    def ReorientDifferenceCellsOn(self):
        """
        V.ReorientDifferenceCellsOn()
        C++: virtual void ReorientDifferenceCellsOn()
        
        Turn on/off cell reorientation of the intersection portion of the
        surface when the operation is set to DIFFERENCE. Defaults to on.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBooleanOperationPolyDataFilter
        C++: static vtkBooleanOperationPolyDataFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetOperation(self, p_int):
        """
        V.SetOperation(int)
        C++: virtual void SetOperation(int _arg)
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def SetOperationToDifference(self):
        """
        V.SetOperationToDifference()
        C++: void SetOperationToDifference()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def SetOperationToIntersection(self):
        """
        V.SetOperationToIntersection()
        C++: void SetOperationToIntersection()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def SetOperationToUnion(self):
        """
        V.SetOperationToUnion()
        C++: void SetOperationToUnion()
        
        Set the boolean operation to perform. Defaults to union.
        """
        ...
    
    def SetReorientDifferenceCells(self, p_int):
        """
        V.SetReorientDifferenceCells(int)
        C++: virtual void SetReorientDifferenceCells(vtkTypeBool _arg)
        
        Turn on/off cell reorientation of the intersection portion of the
        surface when the operation is set to DIFFERENCE. Defaults to on.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Set/get the tolerance used to determine when a point's absolute
        distance is considered to be zero. Defaults to 1e-6.
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
    OperationType = ...
    VTK_DIFFERENCE = ...
    VTK_INTERSECTION = ...
    VTK_UNION = ...
    __dict__ = ...
    __vtkname__ = ...


