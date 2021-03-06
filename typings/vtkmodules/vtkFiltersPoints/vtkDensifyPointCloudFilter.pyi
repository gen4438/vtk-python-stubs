"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDensifyPointCloudFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkDensifyPointCloudFilter - add points to a point cloud to make it
    denser
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkDensifyPointCloudFilter adds new points to an input point cloud.
    The new points are created in such a way that all points in any local
    neighborhood are within a target distance of one another. Optionally,
    attribute data can be interpolated from the input point cloud as
    well.
    
    A high-level overview of the algorithm is as follows. For each input
    point, the distance to all points in its neighborhood is computed. If
    any of its neighbors is further than the target distance, the edge
    connecting the point and its neighbor is bisected and a new point is
    inserted at the bisection point (optionally the attribute data is
    interpolated as well). A single pass is completed once all the input
    points are visited. Then the process repeats to the limit of the
    maximum number of iterations.
    
    @warning
    This class can generate a lot of points very quickly. The maximum
    number of iterations is by default set to =1.0 for this reason.
    Increase the number of iterations very carefully. Also the
    MaximumNumberOfPoints data member can be set to limit the explosion
    of points. It is also recommended that a N closest neighborhood is
    used.
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkVoxelGridFilter vtkEuclideanClusterExtraction
    vtkBoundedPointSource
    """
    def GetInterpolateAttributeData(self):
        """
        V.GetInterpolateAttributeData() -> bool
        C++: virtual bool GetInterpolateAttributeData()
        
        Turn on/off the interpolation of attribute data from the input
        point cloud to new, added points.
        """
        ...
    
    def GetMaximumNumberOfIterations(self):
        """
        V.GetMaximumNumberOfIterations() -> int
        C++: virtual int GetMaximumNumberOfIterations()
        
        The maximum number of iterations to run. By default the maximum
        is one.
        """
        ...
    
    def GetMaximumNumberOfIterationsMaxValue(self):
        """
        V.GetMaximumNumberOfIterationsMaxValue() -> int
        C++: virtual int GetMaximumNumberOfIterationsMaxValue()
        
        The maximum number of iterations to run. By default the maximum
        is one.
        """
        ...
    
    def GetMaximumNumberOfIterationsMinValue(self):
        """
        V.GetMaximumNumberOfIterationsMinValue() -> int
        C++: virtual int GetMaximumNumberOfIterationsMinValue()
        
        The maximum number of iterations to run. By default the maximum
        is one.
        """
        ...
    
    def GetMaximumNumberOfPoints(self):
        """
        V.GetMaximumNumberOfPoints() -> int
        C++: virtual vtkIdType GetMaximumNumberOfPoints()
        
        Set a limit on the maximum number of points that can be created.
        This data member serves as a crude barrier to explosive point
        creation; it does not guarantee that precisely these many points
        will be created. Once this limit is hit, it may result in
        premature termination of the algorithm. Consider it a pressure
        relief valve.
        """
        ...
    
    def GetMaximumNumberOfPointsMaxValue(self):
        """
        V.GetMaximumNumberOfPointsMaxValue() -> int
        C++: virtual vtkIdType GetMaximumNumberOfPointsMaxValue()
        
        Set a limit on the maximum number of points that can be created.
        This data member serves as a crude barrier to explosive point
        creation; it does not guarantee that precisely these many points
        will be created. Once this limit is hit, it may result in
        premature termination of the algorithm. Consider it a pressure
        relief valve.
        """
        ...
    
    def GetMaximumNumberOfPointsMinValue(self):
        """
        V.GetMaximumNumberOfPointsMinValue() -> int
        C++: virtual vtkIdType GetMaximumNumberOfPointsMinValue()
        
        Set a limit on the maximum number of points that can be created.
        This data member serves as a crude barrier to explosive point
        creation; it does not guarantee that precisely these many points
        will be created. Once this limit is hit, it may result in
        premature termination of the algorithm. Consider it a pressure
        relief valve.
        """
        ...
    
    def GetNeighborhoodType(self):
        """
        V.GetNeighborhoodType() -> int
        C++: virtual int GetNeighborhoodType()
        
        Specify how the local point neighborhood is defined. By default
        an N closest neighborhood is used. This tends to avoid explosive
        point creation.
        """
        ...
    
    def GetNumberOfClosestPoints(self):
        """
        V.GetNumberOfClosestPoints() -> int
        C++: virtual int GetNumberOfClosestPoints()
        
        Define a local neighborhood in terms of the N closest points. By
        default the number of the closest points is =6. This data member
        is relevant only if the neighborhood type is N_CLOSEST.
        """
        ...
    
    def GetNumberOfClosestPointsMaxValue(self):
        """
        V.GetNumberOfClosestPointsMaxValue() -> int
        C++: virtual int GetNumberOfClosestPointsMaxValue()
        
        Define a local neighborhood in terms of the N closest points. By
        default the number of the closest points is =6. This data member
        is relevant only if the neighborhood type is N_CLOSEST.
        """
        ...
    
    def GetNumberOfClosestPointsMinValue(self):
        """
        V.GetNumberOfClosestPointsMinValue() -> int
        C++: virtual int GetNumberOfClosestPointsMinValue()
        
        Define a local neighborhood in terms of the N closest points. By
        default the number of the closest points is =6. This data member
        is relevant only if the neighborhood type is N_CLOSEST.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Define a local neighborhood for each point in terms of a local
        radius. By default, the radius is 1.0. This data member is
        relevant only if the neighborhood type is RADIUS.
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        Define a local neighborhood for each point in terms of a local
        radius. By default, the radius is 1.0. This data member is
        relevant only if the neighborhood type is RADIUS.
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        Define a local neighborhood for each point in terms of a local
        radius. By default, the radius is 1.0. This data member is
        relevant only if the neighborhood type is RADIUS.
        """
        ...
    
    def GetTargetDistance(self):
        """
        V.GetTargetDistance() -> float
        C++: virtual double GetTargetDistance()
        
        Set / get the target point distance. Points will be created in an
        iterative fashion until all points in their local neighborhood
        are the target distance apart or less. Note that the process may
        terminate early due to the limit on the maximum number of
        iterations. By default the target distance is set to 0.5. Note
        that the TargetDistance should be less than the Radius or nothing
        will change on output.
        """
        ...
    
    def GetTargetDistanceMaxValue(self):
        """
        V.GetTargetDistanceMaxValue() -> float
        C++: virtual double GetTargetDistanceMaxValue()
        
        Set / get the target point distance. Points will be created in an
        iterative fashion until all points in their local neighborhood
        are the target distance apart or less. Note that the process may
        terminate early due to the limit on the maximum number of
        iterations. By default the target distance is set to 0.5. Note
        that the TargetDistance should be less than the Radius or nothing
        will change on output.
        """
        ...
    
    def GetTargetDistanceMinValue(self):
        """
        V.GetTargetDistanceMinValue() -> float
        C++: virtual double GetTargetDistanceMinValue()
        
        Set / get the target point distance. Points will be created in an
        iterative fashion until all points in their local neighborhood
        are the target distance apart or less. Note that the process may
        terminate early due to the limit on the maximum number of
        iterations. By default the target distance is set to 0.5. Note
        that the TargetDistance should be less than the Radius or nothing
        will change on output.
        """
        ...
    
    def InterpolateAttributeDataOff(self):
        """
        V.InterpolateAttributeDataOff()
        C++: virtual void InterpolateAttributeDataOff()
        
        Turn on/off the interpolation of attribute data from the input
        point cloud to new, added points.
        """
        ...
    
    def InterpolateAttributeDataOn(self):
        """
        V.InterpolateAttributeDataOn()
        C++: virtual void InterpolateAttributeDataOn()
        
        Turn on/off the interpolation of attribute data from the input
        point cloud to new, added points.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDensifyPointCloudFilter
        C++: vtkDensifyPointCloudFilter *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDensifyPointCloudFilter
        C++: static vtkDensifyPointCloudFilter *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetInterpolateAttributeData(self, bool):
        """
        V.SetInterpolateAttributeData(bool)
        C++: virtual void SetInterpolateAttributeData(bool _arg)
        
        Turn on/off the interpolation of attribute data from the input
        point cloud to new, added points.
        """
        ...
    
    def SetMaximumNumberOfIterations(self, p_int):
        """
        V.SetMaximumNumberOfIterations(int)
        C++: virtual void SetMaximumNumberOfIterations(int _arg)
        
        The maximum number of iterations to run. By default the maximum
        is one.
        """
        ...
    
    def SetMaximumNumberOfPoints(self, p_int):
        """
        V.SetMaximumNumberOfPoints(int)
        C++: virtual void SetMaximumNumberOfPoints(vtkIdType _arg)
        
        Set a limit on the maximum number of points that can be created.
        This data member serves as a crude barrier to explosive point
        creation; it does not guarantee that precisely these many points
        will be created. Once this limit is hit, it may result in
        premature termination of the algorithm. Consider it a pressure
        relief valve.
        """
        ...
    
    def SetNeighborhoodType(self, p_int):
        """
        V.SetNeighborhoodType(int)
        C++: virtual void SetNeighborhoodType(int _arg)
        
        Specify how the local point neighborhood is defined. By default
        an N closest neighborhood is used. This tends to avoid explosive
        point creation.
        """
        ...
    
    def SetNeighborhoodTypeToNClosest(self):
        """
        V.SetNeighborhoodTypeToNClosest()
        C++: void SetNeighborhoodTypeToNClosest()
        
        Specify how the local point neighborhood is defined. By default
        an N closest neighborhood is used. This tends to avoid explosive
        point creation.
        """
        ...
    
    def SetNeighborhoodTypeToRadius(self):
        """
        V.SetNeighborhoodTypeToRadius()
        C++: void SetNeighborhoodTypeToRadius()
        
        Specify how the local point neighborhood is defined. By default
        an N closest neighborhood is used. This tends to avoid explosive
        point creation.
        """
        ...
    
    def SetNumberOfClosestPoints(self, p_int):
        """
        V.SetNumberOfClosestPoints(int)
        C++: virtual void SetNumberOfClosestPoints(int _arg)
        
        Define a local neighborhood in terms of the N closest points. By
        default the number of the closest points is =6. This data member
        is relevant only if the neighborhood type is N_CLOSEST.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Define a local neighborhood for each point in terms of a local
        radius. By default, the radius is 1.0. This data member is
        relevant only if the neighborhood type is RADIUS.
        """
        ...
    
    def SetTargetDistance(self, p_float):
        """
        V.SetTargetDistance(float)
        C++: virtual void SetTargetDistance(double _arg)
        
        Set / get the target point distance. Points will be created in an
        iterative fashion until all points in their local neighborhood
        are the target distance apart or less. Note that the process may
        terminate early due to the limit on the maximum number of
        iterations. By default the target distance is set to 0.5. Note
        that the TargetDistance should be less than the Radius or nothing
        will change on output.
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
    NeighborhoodType = ...
    N_CLOSEST = ...
    RADIUS = ...
    __dict__ = ...
    __vtkname__ = ...


