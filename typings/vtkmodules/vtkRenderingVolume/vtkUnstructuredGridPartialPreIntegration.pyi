"""
This type stub file was generated by pyright.
"""

from .vtkUnstructuredGridVolumeRayIntegrator import vtkUnstructuredGridVolumeRayIntegrator

class vtkUnstructuredGridPartialPreIntegration(vtkUnstructuredGridVolumeRayIntegrator):
    """
    vtkUnstructuredGridPartialPreIntegration - performs piecewise linear
    ray integration.
    
    Superclass: vtkUnstructuredGridVolumeRayIntegrator
    
    vtkUnstructuredGridPartialPreIntegration performs piecewise linear
    ray integration.  This will give the same results as
    vtkUnstructuredGridLinearRayIntegration (with potentially a error due
    to table lookup quantization), but should be notably faster.  The
    algorithm used is given by Moreland and Angel, "A Fast High Accuracy
    Volume Renderer for Unstructured Data."
    
    This class is thread safe only after the first instance is created.
    """
    def BuildPsiTable(self):
        """
        V.BuildPsiTable()
        C++: static void BuildPsiTable()
        
        Looks up Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data") in a table.  The
        table must be created first, which happens on the first
        instantiation of this class or when BuildPsiTable is first
        called.
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
    
    def GetPsiTable(self, p_int):
        """
        V.GetPsiTable(int) -> (float, ...)
        C++: static float *GetPsiTable(int &size)
        
        Looks up Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data") in a table.  The
        table must be created first, which happens on the first
        instantiation of this class or when BuildPsiTable is first
        called.
        """
        ...
    
    def Initialize(self, vtkVolume, vtkDataArray):
        """
        V.Initialize(vtkVolume, vtkDataArray)
        C++: void Initialize(vtkVolume *volume, vtkDataArray *scalars)
            override;
        
        Set up the integrator with the given properties and scalars.
        """
        ...
    
    def Integrate(self, vtkDoubleArray, vtkDataArray, vtkDataArray_1, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.Integrate(vtkDoubleArray, vtkDataArray, vtkDataArray, [float,
            float, float, float])
        C++: void Integrate(vtkDoubleArray *intersectionLengths,
            vtkDataArray *nearIntersections,
            vtkDataArray *farIntersections, float color[4]) override;
        
        Given a set of intersections (defined by the three arrays),
        compute the piecewise integration of the array in front to back
        order. /c intersectionLengths holds the lengths of each piecewise
        segment. /c nearIntersections and /c farIntersections hold the
        scalar values at the front and back of each segment.  /c color
        should contain the RGBA value of the volume in front of the
        segments passed in, and the result will be placed back into /c
        color.
        """
        ...
    
    def IntegrateRay(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.IntegrateRay(float, float, float, float, float, [float, float,
            float, float])
        C++: static void IntegrateRay(double length,
            double intensity_front, double attenuation_front,
            double intensity_back, double attenuation_back,
            float color[4])
        V.IntegrateRay(float, (float, float, float), float, (float, float,
             float), float, [float, float, float, float])
        C++: static void IntegrateRay(double length,
            const double color_front[3], double attenuation_front,
            const double color_back[3], double attenuation_back,
            float color[4])
        
        Integrates a single ray segment.  color is blended with the
        result (with color in front).  The result is written back into
        color.
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
        V.NewInstance() -> vtkUnstructuredGridPartialPreIntegration
        C++: vtkUnstructuredGridPartialPreIntegration *NewInstance()
        """
        ...
    
    def Psi(self, p_float, p_float_1):
        """
        V.Psi(float, float) -> float
        C++: static float Psi(float taufD, float taubD)
        
        Looks up Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data") in a table.  The
        table must be created first, which happens on the first
        instantiation of this class or when BuildPsiTable is first
        called.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkUnstructuredGridPartialPreIntegration
        C++: static vtkUnstructuredGridPartialPreIntegration *SafeDownCast(
            vtkObjectBase *o)
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


