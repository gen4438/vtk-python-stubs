"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkMeanValueCoordinatesInterpolator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkMeanValueCoordinatesInterpolator - compute interpolation computes
    for closed triangular mesh
    
    Superclass: vtkObject
    
    vtkMeanValueCoordinatesInterpolator computes interpolation weights
    for a closed, manifold polyhedron mesh.  Once computed, the
    interpolation weights can be used to interpolate data anywhere
    interior or exterior to the mesh. This work implements two MVC
    algorithms. The first one is for triangular meshes which is
    documented in the Siggraph 2005 paper by Tao Ju, Scot Schaefer and
    Joe Warren from Rice University "Mean Value Coordinates for Closed
    Triangular Meshes". The second one is for general polyhedron mesh
    which is documented in the Eurographics Symposium on Geometry
    Processing 2006 paper by Torsten Langer, Alexander Belyaev and
    Hans-Peter Seidel from MPI Informatik "Spherical Barycentric
    Coordinates". The filter will automatically choose which algorithm to
    use based on whether the input mesh is triangulated or not.
    
    In VTK this class was initially created to interpolate data across
    polyhedral cells. In addition, the class can be used to interpolate
    data values from a polyhedron mesh, and to smoothly deform a mesh
    from an associated control mesh.
    
    @sa
    vtkPolyhedralCell
    """
    def ComputeInterpolationWeights(self, , vtkPoints, vtkIdList, *float):
        """
        V.ComputeInterpolationWeights((float, float, float), vtkPoints,
            vtkIdList, [float, ...])
        C++: static void ComputeInterpolationWeights(const double x[3],
            vtkPoints *pts, vtkIdList *tris, double *weights)
        V.ComputeInterpolationWeights((float, float, float), vtkPoints,
            vtkCellArray, [float, ...])
        C++: static void ComputeInterpolationWeights(const double x[3],
            vtkPoints *pts, vtkCellArray *tris, double *weights)
        
        Method to generate interpolation weights for a point x[3] from a
        list of triangles.  In this version of the method, the triangles
        are defined by a vtkPoints array plus a vtkIdList, where the
        vtkIdList is organized such that three ids in order define a
        triangle.  Note that number of weights must equal the number of
        points.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard instantiable class methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard instantiable class methods.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard instantiable class methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard instantiable class methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkMeanValueCoordinatesInterpolator
        C++: vtkMeanValueCoordinatesInterpolator *NewInstance()
        
        Standard instantiable class methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkMeanValueCoordinatesInterpolator
        C++: static vtkMeanValueCoordinatesInterpolator *SafeDownCast(
            vtkObjectBase *o)
        
        Standard instantiable class methods.
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


