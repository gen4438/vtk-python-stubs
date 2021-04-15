"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkPlaneCutter(__vtkmodules_vtkCommonExecutionModel.vtkDataSetAlgorithm):
    """
    vtkPlaneCutter - cut any dataset with a plane and generate a
    polygonal cut surface
    
    Superclass: vtkDataSetAlgorithm
    
    vtkPlaneCutter is a specialization of the vtkCutter algorithm to cut
    a dataset grid with a single plane. It is designed for performance
    and an exploratory, fast workflow. It produces output polygons that
    result from cutting the icnput dataset with the specified plane.
    
    This algorithm is fast because it is threaded, and may build (in a
    preprocessing step) a spatial search structure that accelerates the
    plane cuts. The search structure, which is typically a sphere tree,
    is used to quickly cull candidate cells.  (Note that certain types of
    input data are delegated to other, internal classes; for example
    image data is delegated to vtkFlyingEdgesPlaneCutter.)
    
    Because this filter may build an initial data structure during a
    preprocessing step, the first execution of the filter may take longer
    than subsequent operations. Typically the first execution is still
    faster than vtkCutter (especially with threading enabled), but for
    certain types of data this may not be true. However if you are using
    the filter to cut a dataset multiple times (as in an exploratory or
    interactive workflow) this filter typically works well.
    
    @warning
    This filter outputs a vtkMultiBlockeDataSet. Each piece in the
    multiblock output corresponds to the output from one thread.
    
    @warning
    This filter produces non-merged, potentially coincident points for
    all input dataset types except vtkImageData (which uses
    vtkFlyingEdgesPlaneCutter under the hood - which does merge points).
    
    @warning
    This filter delegates to vtkFlyingEdgesPlaneCutter to process image
    data, but output and input have been standardized when possible.
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkFlyingEdgesPlaneCutter vtk3DLinearGridPlaneCutter vtkCutter
    vtkPlane
    """
    def BuildHierarchyOff(self):
        """
        V.BuildHierarchyOff()
        C++: virtual void BuildHierarchyOff()
        
        Indicate whether to build tree hierarchy. Computing the tree
        hierarchy can take some time on the first computation but if the
        input does not change, the computation of all further slice will
        be faster. Default is on.
        """
        ...
    
    def BuildHierarchyOn(self):
        """
        V.BuildHierarchyOn()
        C++: virtual void BuildHierarchyOn()
        
        Indicate whether to build tree hierarchy. Computing the tree
        hierarchy can take some time on the first computation but if the
        input does not change, the computation of all further slice will
        be faster. Default is on.
        """
        ...
    
    def BuildTreeOff(self):
        """
        V.BuildTreeOff()
        C++: virtual void BuildTreeOff()
        
        Indicate whether to build the sphere tree. Computing the sphere
        will take some time on the first computation but if the input
        does not change, the computation of all further slice will be
        much faster. Default is on.
        """
        ...
    
    def BuildTreeOn(self):
        """
        V.BuildTreeOn()
        C++: virtual void BuildTreeOn()
        
        Indicate whether to build the sphere tree. Computing the sphere
        will take some time on the first computation but if the input
        does not change, the computation of all further slice will be
        much faster. Default is on.
        """
        ...
    
    def ComputeNormalsOff(self):
        """
        V.ComputeNormalsOff()
        C++: virtual void ComputeNormalsOff()
        
        Set/Get the computation of normals. The normal generated is
        simply the cut plane normal. The normal, if generated, is defined
        by cell data associated with the output polygons. By default
        computing of normals is disabled.
        """
        ...
    
    def ComputeNormalsOn(self):
        """
        V.ComputeNormalsOn()
        C++: virtual void ComputeNormalsOn()
        
        Set/Get the computation of normals. The normal generated is
        simply the cut plane normal. The normal, if generated, is defined
        by cell data associated with the output polygons. By default
        computing of normals is disabled.
        """
        ...
    
    def GeneratePolygonsOff(self):
        """
        V.GeneratePolygonsOff()
        C++: virtual void GeneratePolygonsOff()
        
        Indicate whether to generate polygons instead of triangles when
        cutting structured and rectilinear grid. No effect with other
        kinds of inputs, enabled by default.
        """
        ...
    
    def GeneratePolygonsOn(self):
        """
        V.GeneratePolygonsOn()
        C++: virtual void GeneratePolygonsOn()
        
        Indicate whether to generate polygons instead of triangles when
        cutting structured and rectilinear grid. No effect with other
        kinds of inputs, enabled by default.
        """
        ...
    
    def GetBuildHierarchy(self):
        """
        V.GetBuildHierarchy() -> bool
        C++: virtual bool GetBuildHierarchy()
        
        Indicate whether to build tree hierarchy. Computing the tree
        hierarchy can take some time on the first computation but if the
        input does not change, the computation of all further slice will
        be faster. Default is on.
        """
        ...
    
    def GetBuildTree(self):
        """
        V.GetBuildTree() -> bool
        C++: virtual bool GetBuildTree()
        
        Indicate whether to build the sphere tree. Computing the sphere
        will take some time on the first computation but if the input
        does not change, the computation of all further slice will be
        much faster. Default is on.
        """
        ...
    
    def GetComputeNormals(self):
        """
        V.GetComputeNormals() -> bool
        C++: virtual bool GetComputeNormals()
        
        Set/Get the computation of normals. The normal generated is
        simply the cut plane normal. The normal, if generated, is defined
        by cell data associated with the output polygons. By default
        computing of normals is disabled.
        """
        ...
    
    def GetGeneratePolygons(self):
        """
        V.GetGeneratePolygons() -> bool
        C++: virtual bool GetGeneratePolygons()
        
        Indicate whether to generate polygons instead of triangles when
        cutting structured and rectilinear grid. No effect with other
        kinds of inputs, enabled by default.
        """
        ...
    
    def GetInterpolateAttributes(self):
        """
        V.GetInterpolateAttributes() -> bool
        C++: virtual bool GetInterpolateAttributes()
        
        Indicate whether to interpolate attribute data. By default this
        is enabled. Note that both cell data and point data is
        interpolated and outputted, except for image data input where
        only point data are outputted.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        The modified time depends on the delegated cut plane.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard construction and print methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard construction and print methods.
        """
        ...
    
    def GetPlane(self):
        """
        V.GetPlane() -> vtkPlane
        C++: virtual vtkPlane *GetPlane()
        
        Specify the plane (an implicit function) to perform the cutting.
        The definition of the plane (its origin and normal) is controlled
        via this instance of vtkPlane.
        """
        ...
    
    def InterpolateAttributesOff(self):
        """
        V.InterpolateAttributesOff()
        C++: virtual void InterpolateAttributesOff()
        
        Indicate whether to interpolate attribute data. By default this
        is enabled. Note that both cell data and point data is
        interpolated and outputted, except for image data input where
        only point data are outputted.
        """
        ...
    
    def InterpolateAttributesOn(self):
        """
        V.InterpolateAttributesOn()
        C++: virtual void InterpolateAttributesOn()
        
        Indicate whether to interpolate attribute data. By default this
        is enabled. Note that both cell data and point data is
        interpolated and outputted, except for image data input where
        only point data are outputted.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard construction and print methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard construction and print methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPlaneCutter
        C++: vtkPlaneCutter *NewInstance()
        
        Standard construction and print methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPlaneCutter
        C++: static vtkPlaneCutter *SafeDownCast(vtkObjectBase *o)
        
        Standard construction and print methods.
        """
        ...
    
    def SetBuildHierarchy(self, bool):
        """
        V.SetBuildHierarchy(bool)
        C++: virtual void SetBuildHierarchy(bool _arg)
        
        Indicate whether to build tree hierarchy. Computing the tree
        hierarchy can take some time on the first computation but if the
        input does not change, the computation of all further slice will
        be faster. Default is on.
        """
        ...
    
    def SetBuildTree(self, bool):
        """
        V.SetBuildTree(bool)
        C++: virtual void SetBuildTree(bool _arg)
        
        Indicate whether to build the sphere tree. Computing the sphere
        will take some time on the first computation but if the input
        does not change, the computation of all further slice will be
        much faster. Default is on.
        """
        ...
    
    def SetComputeNormals(self, bool):
        """
        V.SetComputeNormals(bool)
        C++: virtual void SetComputeNormals(bool _arg)
        
        Set/Get the computation of normals. The normal generated is
        simply the cut plane normal. The normal, if generated, is defined
        by cell data associated with the output polygons. By default
        computing of normals is disabled.
        """
        ...
    
    def SetGeneratePolygons(self, bool):
        """
        V.SetGeneratePolygons(bool)
        C++: virtual void SetGeneratePolygons(bool _arg)
        
        Indicate whether to generate polygons instead of triangles when
        cutting structured and rectilinear grid. No effect with other
        kinds of inputs, enabled by default.
        """
        ...
    
    def SetInterpolateAttributes(self, bool):
        """
        V.SetInterpolateAttributes(bool)
        C++: virtual void SetInterpolateAttributes(bool _arg)
        
        Indicate whether to interpolate attribute data. By default this
        is enabled. Note that both cell data and point data is
        interpolated and outputted, except for image data input where
        only point data are outputted.
        """
        ...
    
    def SetPlane(self, vtkPlane):
        """
        V.SetPlane(vtkPlane)
        C++: virtual void SetPlane(vtkPlane *)
        
        Specify the plane (an implicit function) to perform the cutting.
        The definition of the plane (its origin and normal) is controlled
        via this instance of vtkPlane.
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


