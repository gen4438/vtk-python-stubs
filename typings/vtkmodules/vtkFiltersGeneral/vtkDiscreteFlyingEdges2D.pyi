"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDiscreteFlyingEdges2D(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkDiscreteFlyingEdges2D - generate isoline(s) from 2D image data
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkDiscreteFlyingEdges2D creates output representations of label maps
    (e.g., segmented images) using a variation of the flying edges
    algorithm. The input is a 2D image where each point is labeled
    (integer labels are preferred to real values), and the output data is
    polygonal data representing labeled regions. (Note that on output
    each region [corresponding to a different contour value] is
    represented independently; i.e., points are not shared between
    regions even if they are coincident.)
    
    @warning
    This filter is specialized to 2D images. This implementation can
    produce degenerate line segments (i.e., zero-length line segments).
    
    @warning
    Use vtkContourLoopExtraction if you wish to create polygons from the
    line segments.
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkDiscreteMarchingCubes vtkContourLoopExtraction
    """
    def ComputeScalarsOff(self):
        """
        V.ComputeScalarsOff()
        C++: virtual void ComputeScalarsOff()
        
        Option to set the point scalars of the output.  The scalars will
        be the label values.  By default this flag is on.
        """
        ...
    
    def ComputeScalarsOn(self):
        """
        V.ComputeScalarsOn()
        C++: virtual void ComputeScalarsOn()
        
        Option to set the point scalars of the output.  The scalars will
        be the label values.  By default this flag is on.
        """
        ...
    
    def GenerateValues(self, p_int, p_float=..., p_float=...):
        """
        V.GenerateValues(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.GenerateValues(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        
        Generate numContours equally spaced contour values between
        specified range. Contour values will include min/max range
        values.
        """
        ...
    
    def GetArrayComponent(self):
        """
        V.GetArrayComponent() -> int
        C++: virtual int GetArrayComponent()
        
        Set/get which component of the scalar array to contour on;
        defaults to 0.
        """
        ...
    
    def GetComputeScalars(self):
        """
        V.GetComputeScalars() -> int
        C++: virtual int GetComputeScalars()
        
        Option to set the point scalars of the output.  The scalars will
        be the label values.  By default this flag is on.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Because we delegate to vtkContourValues.
        """
        ...
    
    def GetNumberOfContours(self):
        """
        V.GetNumberOfContours() -> int
        C++: vtkIdType GetNumberOfContours()
        
        Get the number of contours in the list of contour values.
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
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> float
        C++: double GetValue(int i)
        
        Get the ith contour value.
        """
        ...
    
    def GetValues(self):
        """
        V.GetValues() -> (float, ...)
        C++: double *GetValues()
        V.GetValues([float, ...])
        C++: void GetValues(double *contourValues)
        
        Get a pointer to an array of contour values. There will be
        GetNumberOfContours() values in the list.
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
        V.NewInstance() -> vtkDiscreteFlyingEdges2D
        C++: vtkDiscreteFlyingEdges2D *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDiscreteFlyingEdges2D
        C++: static vtkDiscreteFlyingEdges2D *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetArrayComponent(self, p_int):
        """
        V.SetArrayComponent(int)
        C++: virtual void SetArrayComponent(int _arg)
        
        Set/get which component of the scalar array to contour on;
        defaults to 0.
        """
        ...
    
    def SetComputeScalars(self, p_int):
        """
        V.SetComputeScalars(int)
        C++: virtual void SetComputeScalars(int _arg)
        
        Option to set the point scalars of the output.  The scalars will
        be the label values.  By default this flag is on.
        """
        ...
    
    def SetNumberOfContours(self, p_int):
        """
        V.SetNumberOfContours(int)
        C++: void SetNumberOfContours(int number)
        
        Set the number of contours to place into the list. You only
        really need to use this method to reduce list size. The method
        SetValue() will automatically increase list size as needed.
        """
        ...
    
    def SetValue(self, p_int, p_float):
        """
        V.SetValue(int, float)
        C++: void SetValue(int i, double value)
        
        Set a particular contour value at contour number i. The index i
        ranges between 0<=i<NumberOfContours.
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

