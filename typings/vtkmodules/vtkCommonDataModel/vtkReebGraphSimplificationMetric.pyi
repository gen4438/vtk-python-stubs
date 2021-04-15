"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkReebGraphSimplificationMetric(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkReebGraphSimplificationMetric - abstract class for custom Reeb
    graph simplification metric design.
    
    Superclass: vtkObject
    
    This class makes it possible to design customized simplification
    metric evaluation algorithms, enabling the user to control the
    definition of what should be considered as noise or signal in the
    topological filtering process.
    
    References: "Topological persistence and simplification", H.
    Edelsbrunner, D. Letscher, and A. Zomorodian, Discrete Computational
    Geometry, 28:511-533, 2002.
    
    "Extreme elevation on a 2-manifold", P.K. Agarwal, H. Edelsbrunner,
    J. Harer, and Y. Wang, ACM Symposium on Computational Geometry, pp.
    357-365, 2004.
    
    "Simplifying flexible isosurfaces using local geometric measures", H.
    Carr, J. Snoeyink, M van de Panne, IEEE Visualization, 497-504, 2004
    
    "Loop surgery for volumetric meshes: Reeb graphs reduced to contour
    trees", J. Tierny, A. Gyulassy, E. Simon, V. Pascucci, IEEE Trans. on
    Vis. and Comp. Graph. (Proc of IEEE VIS), 15:1177-1184, 2009.
    
    See Graphics/Testing/Cxx/TestReebGraph.cxx for an example of concrete
    implementation.
    """
    def ComputeMetric(self, vtkDataSet, vtkDataArray, p_int, vtkAbstractArray, p_int_1):
        """
        V.ComputeMetric(vtkDataSet, vtkDataArray, int, vtkAbstractArray,
            int) -> float
        C++: virtual double ComputeMetric(vtkDataSet *mesh,
            vtkDataArray *field, vtkIdType startCriticalPoint,
            vtkAbstractArray *vertexList, vtkIdType endCriticalPoint)
        
        Function to implement in your simplification metric algorithm.
        Given the input mesh and the Ids of the vertices living on the
        Reeb graph arc to consider for removal, you should return a value
        between 0 and 1 (the smallest the more likely the arc will be
        removed, depending on the user-defined simplification threshold).
        """
        ...
    
    def GetLowerBound(self):
        """
        V.GetLowerBound() -> float
        C++: virtual double GetLowerBound()
        
        Set the lowest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the ComputeMetric call to make sure the
        returned value of ComputeMetric call is indeed between 0 and 1.
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
    
    def GetUpperBound(self):
        """
        V.GetUpperBound() -> float
        C++: virtual double GetUpperBound()
        
        Set the highest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the ComputeMetric call to make sure the
        returned value of ComputeMetric call is indeed between 0 and 1.
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
        V.NewInstance() -> vtkReebGraphSimplificationMetric
        C++: vtkReebGraphSimplificationMetric *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkReebGraphSimplificationMetric
        C++: static vtkReebGraphSimplificationMetric *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetLowerBound(self, p_float):
        """
        V.SetLowerBound(float)
        C++: virtual void SetLowerBound(double _arg)
        
        Set the lowest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the ComputeMetric call to make sure the
        returned value of ComputeMetric call is indeed between 0 and 1.
        """
        ...
    
    def SetUpperBound(self, p_float):
        """
        V.SetUpperBound(float)
        C++: virtual void SetUpperBound(double _arg)
        
        Set the highest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the ComputeMetric call to make sure the
        returned value of ComputeMetric call is indeed between 0 and 1.
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


