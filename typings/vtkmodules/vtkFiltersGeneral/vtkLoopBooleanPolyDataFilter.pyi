"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkLoopBooleanPolyDataFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkLoopBooleanPolyDataFilter - Computes the boundary of the union,
    intersection, or difference volume computed from the volumes defined
    by two input surfaces.
    
    Superclass: vtkPolyDataAlgorithm
    
    The two surfaces do not need to be manifold, but if they are not,
    unexpected results may be obtained. The resulting surface is
    available in the first output of the filter. The second output
    contains a set of polylines that represent the intersection between
    the two input surfaces. The filter uses
    vtkIntersectionPolyDataFilter. Must have information about the cells
    on mesh that the intersection lines touch. Filter assumes this
    information is given. The output result will have data about the
    Original Surface, BoundaryPoints, Boundary Cells, Free Edges, and Bad
    Triangles
    """
    def GetNoIntersectionOutput(self):
        """
        V.GetNoIntersectionOutput() -> int
        C++: virtual int GetNoIntersectionOutput()
        
        ONLY USED IF NO INTERSECTION BETWEEN SURFACES Variable to
        determine what is output if no intersection occurs. 0 = neither
        (default), 1 = first, 2 = second, 3 = both
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
    
    def GetNumberOfIntersectionLines(self):
        """
        V.GetNumberOfIntersectionLines() -> int
        C++: virtual int GetNumberOfIntersectionLines()
        
        Integer describing the number of intersection points and lines
        """
        ...
    
    def GetNumberOfIntersectionPoints(self):
        """
        V.GetNumberOfIntersectionPoints() -> int
        C++: virtual int GetNumberOfIntersectionPoints()
        
        Integer describing the number of intersection points and lines
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
    
    def GetStatus(self):
        """
        V.GetStatus() -> int
        C++: virtual int GetStatus()
        
        Check the status of the filter after update. If the status is
        zero, there was an error in the operation. If status is one,
        everything went smoothly
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Set the tolerance for geometric tests
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
        V.NewInstance() -> vtkLoopBooleanPolyDataFilter
        C++: vtkLoopBooleanPolyDataFilter *NewInstance()
        """
        ...
    
    def NoIntersectionOutputOff(self):
        """
        V.NoIntersectionOutputOff()
        C++: virtual void NoIntersectionOutputOff()
        
        ONLY USED IF NO INTERSECTION BETWEEN SURFACES Variable to
        determine what is output if no intersection occurs. 0 = neither
        (default), 1 = first, 2 = second, 3 = both
        """
        ...
    
    def NoIntersectionOutputOn(self):
        """
        V.NoIntersectionOutputOn()
        C++: virtual void NoIntersectionOutputOn()
        
        ONLY USED IF NO INTERSECTION BETWEEN SURFACES Variable to
        determine what is output if no intersection occurs. 0 = neither
        (default), 1 = first, 2 = second, 3 = both
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLoopBooleanPolyDataFilter
        C++: static vtkLoopBooleanPolyDataFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetNoIntersectionOutput(self, p_int):
        """
        V.SetNoIntersectionOutput(int)
        C++: virtual void SetNoIntersectionOutput(int _arg)
        
        ONLY USED IF NO INTERSECTION BETWEEN SURFACES Variable to
        determine what is output if no intersection occurs. 0 = neither
        (default), 1 = first, 2 = second, 3 = both
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
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Set the tolerance for geometric tests
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
    NoIntersectionOutputType = ...
    OperationType = ...
    VTK_BOTH = ...
    VTK_DIFFERENCE = ...
    VTK_FIRST = ...
    VTK_INTERSECTION = ...
    VTK_NEITHER = ...
    VTK_SECOND = ...
    VTK_UNION = ...
    __dict__ = ...
    __vtkname__ = ...


