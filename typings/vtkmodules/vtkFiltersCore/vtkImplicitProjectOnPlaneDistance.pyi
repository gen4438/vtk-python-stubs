"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonDataModel as __vtkmodules_vtkCommonDataModel

class vtkImplicitProjectOnPlaneDistance(__vtkmodules_vtkCommonDataModel.vtkImplicitFunction):
    """
    vtkImplicitProjectOnPlaneDistance - This class recieve a plannar
    polygon as input.
    
    Superclass: vtkImplicitFunction
    
    Given a point, it can evaluate the L0 or L2 norm between the
    projection of this point on the plan of the polygon and the polygon
    itself.
    
    An interesting use of this class is to enable the L0 norm and
    evaluate the "projected distance" between every vertex of a mesh and
    the given plannar polygon. As a reslut, all the vertices that project
    onto the polygon will corresond to the value 0 and ohter ones will
    recieve the value 1. From there, we can use a clip to keep only the
    part of the mesh "below" the polygon.
    
    TLDR: This filter allows to clip using the extrusion of any plannar
    polygon.
    """
    def EvaluateFunction(self, p_float=..., p_float=..., p_float=...):
        """
        V.EvaluateFunction([float, float, float]) -> float
        C++: double EvaluateFunction(double x[3]) override;
        V.EvaluateFunction(vtkDataArray, vtkDataArray)
        C++: virtual void EvaluateFunction(vtkDataArray *input,
            vtkDataArray *output)
        V.EvaluateFunction(float, float, float) -> float
        C++: virtual double EvaluateFunction(double x, double y, double z)
        
        Evaluate function at position x-y-z and return value.  You should
        generally not call this method directly, you should use
        FunctionValue() instead.  This method must be implemented by any
        derived class.
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double g[3]) override;
        
        Evaluate function gradient of nearest triangle to point x[3].
        WARNING: not implemented as it is of no use in this context.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkAbstractCellLocator
        C++: virtual vtkAbstractCellLocator *GetLocator()
        
        Set/get the Locator used by to compute the distance. A
        vtkStaticCellLocator is provided by default if none is given by
        the user.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the MTime also considering the Input dependency.
        """
        ...
    
    def GetNorm(self):
        """
        V.GetNorm() -> NormType
        C++: NormType GetNorm()
        
        Set the norm to use: L0: 0 when the projection is inside the
        input polygon, 1 otherwise L2: Euclidean distance between the
        projection and the polygon (default)
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
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Set/get the tolerance usued for the locator. Default is 0.01.
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
        V.NewInstance() -> vtkImplicitProjectOnPlaneDistance
        C++: vtkImplicitProjectOnPlaneDistance *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImplicitProjectOnPlaneDistance
        C++: static vtkImplicitProjectOnPlaneDistance *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetInput(self, vtkPolyData):
        """
        V.SetInput(vtkPolyData)
        C++: void SetInput(vtkPolyData *input)
        
        Set the input vtkPolyData used for the implicit function
        evaluation. This polydata needs to be planar.
        """
        ...
    
    def SetLocator(self, vtkAbstractCellLocator):
        """
        V.SetLocator(vtkAbstractCellLocator)
        C++: virtual void SetLocator(vtkAbstractCellLocator *_arg)
        
        Set/get the Locator used by to compute the distance. A
        vtkStaticCellLocator is provided by default if none is given by
        the user.
        """
        ...
    
    def SetNorm(self, NormType):
        """
        V.SetNorm(NormType)
        C++: void SetNorm(NormType n)
        V.SetNorm(int)
        C++: void SetNorm(int n)
        
        Set the norm to use: L0: 0 when the projection is inside the
        input polygon, 1 otherwise L2: Euclidean distance between the
        projection and the polygon (default)
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Set/get the tolerance usued for the locator. Default is 0.01.
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
    NormType = ...
    __dict__ = ...
    __vtkname__ = ...

