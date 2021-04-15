"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkEuclideanClusterExtraction(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkEuclideanClusterExtraction - perform segmentation based on
    geometric proximity and optional scalar threshold
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkEuclideanClusterExtraction is a filter that extracts points that
    are in close geometric proximity, and optionally satisfies a scalar
    threshold criterion. (Points extracted in this way are referred to as
    clusters.) The filter works in one of five ways: 1) extract the
    largest cluster in the dataset; 2) extract specified cluster
    number(s); 3) extract all clusters containing specified point ids; 4)
    extract the cluster closest to a specified point; or 5) extract all
    clusters (which can be used for coloring the clusters).
    
    Note that geometric proximity is defined by setting the Radius
    instance variable. This variable defines a local sphere around each
    point; other points contained in this sphere are considered
    "connected" to the point. Setting this number too large will connect
    clusters that should not be; setting it too small will fragment the
    point cloud into myriad clusters. To accelerate the geometric
    proximity operations, a point locator may be specified. By default, a
    vtkStaticPointLocator is used, but any vtkAbstractPointLocator may be
    specified.
    
    The behavior of vtkEuclideanClusterExtraction can be modified by
    turning on the boolean ivar ScalarConnectivity. If this flag is on,
    the clustering algorithm is modified so that points are considered
    part of a cluster if they satisfy both the geometric proximity
    measure, and the points scalar values falls into the scalar range
    specified. This use of ScalarConnectivity is particularly useful for
    data with intensity or color information, serving as a simple "connected
    segmentation" algorithm. For example, by using a seed point in a
    known cluster, clustering will pull out all points "representing" the
    local structure.
    
    @sa
    vtkConnectivityFilter vtkPolyDataConnectivityFilter
    """
    def AddSeed(self, p_int):
        """
        V.AddSeed(int)
        C++: void AddSeed(vtkIdType id)
        
        Add a seed id (point id). Note: ids are 0-offset.
        """
        ...
    
    def AddSpecifiedCluster(self, p_int):
        """
        V.AddSpecifiedCluster(int)
        C++: void AddSpecifiedCluster(int id)
        
        Add a cluster id to extract. Note: ids are 0-offset.
        """
        ...
    
    def ColorClustersOff(self):
        """
        V.ColorClustersOff()
        C++: virtual void ColorClustersOff()
        
        Turn on/off the coloring of connected clusters.
        """
        ...
    
    def ColorClustersOn(self):
        """
        V.ColorClustersOn()
        C++: virtual void ColorClustersOn()
        
        Turn on/off the coloring of connected clusters.
        """
        ...
    
    def DeleteSeed(self, p_int):
        """
        V.DeleteSeed(int)
        C++: void DeleteSeed(vtkIdType id)
        
        Delete a seed id.a
        """
        ...
    
    def DeleteSpecifiedCluster(self, p_int):
        """
        V.DeleteSpecifiedCluster(int)
        C++: void DeleteSpecifiedCluster(int id)
        
        Delete a cluster id to extract.
        """
        ...
    
    def GetClosestPoint(self):
        """
        V.GetClosestPoint() -> (float, float, float)
        C++: virtual double *GetClosestPoint()
        
        Used to specify the x-y-z point coordinates when extracting the
        cluster closest to a specified point.
        """
        ...
    
    def GetColorClusters(self):
        """
        V.GetColorClusters() -> bool
        C++: virtual bool GetColorClusters()
        
        Turn on/off the coloring of connected clusters.
        """
        ...
    
    def GetExtractionMode(self):
        """
        V.GetExtractionMode() -> int
        C++: virtual int GetExtractionMode()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def GetExtractionModeAsString(self):
        """
        V.GetExtractionModeAsString() -> string
        C++: const char *GetExtractionModeAsString()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def GetExtractionModeMaxValue(self):
        """
        V.GetExtractionModeMaxValue() -> int
        C++: virtual int GetExtractionModeMaxValue()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def GetExtractionModeMinValue(self):
        """
        V.GetExtractionModeMinValue() -> int
        C++: virtual int GetExtractionModeMinValue()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkAbstractPointLocator
        C++: virtual vtkAbstractPointLocator *GetLocator()
        
        Specify a point locator. By default a vtkStaticPointLocator is
        used. The locator performs efficient proximity searches near a
        specified interpolation position.
        """
        ...
    
    def GetNumberOfExtractedClusters(self):
        """
        V.GetNumberOfExtractedClusters() -> int
        C++: int GetNumberOfExtractedClusters()
        
        Obtain the number of connected clusters. This value is valid only
        after filter execution.
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
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Specify the local search radius.
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        Specify the local search radius.
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        Specify the local search radius.
        """
        ...
    
    def GetScalarConnectivity(self):
        """
        V.GetScalarConnectivity() -> bool
        C++: virtual bool GetScalarConnectivity()
        
        Turn on/off connectivity based on scalar value. If on, points are
        connected only if the are proximal AND the scalar value of a
        candidate point falls in the scalar range specified. Of course
        input point scalar data must be provided.
        """
        ...
    
    def GetScalarRange(self):
        """
        V.GetScalarRange() -> (float, float)
        C++: virtual double *GetScalarRange()
        
        Set the scalar range used to extract points based on scalar
        connectivity.
        """
        ...
    
    def InitializeSeedList(self):
        """
        V.InitializeSeedList()
        C++: void InitializeSeedList()
        
        Initialize the list of point ids used to seed clusters.
        """
        ...
    
    def InitializeSpecifiedClusterList(self):
        """
        V.InitializeSpecifiedClusterList()
        C++: void InitializeSpecifiedClusterList()
        
        Initialize the list of cluster ids to extract.
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
        V.NewInstance() -> vtkEuclideanClusterExtraction
        C++: vtkEuclideanClusterExtraction *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkEuclideanClusterExtraction
        C++: static vtkEuclideanClusterExtraction *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def ScalarConnectivityOff(self):
        """
        V.ScalarConnectivityOff()
        C++: virtual void ScalarConnectivityOff()
        
        Turn on/off connectivity based on scalar value. If on, points are
        connected only if the are proximal AND the scalar value of a
        candidate point falls in the scalar range specified. Of course
        input point scalar data must be provided.
        """
        ...
    
    def ScalarConnectivityOn(self):
        """
        V.ScalarConnectivityOn()
        C++: virtual void ScalarConnectivityOn()
        
        Turn on/off connectivity based on scalar value. If on, points are
        connected only if the are proximal AND the scalar value of a
        candidate point falls in the scalar range specified. Of course
        input point scalar data must be provided.
        """
        ...
    
    def SetClosestPoint(self, p_float, p_float_1, p_float_2):
        """
        V.SetClosestPoint(float, float, float)
        C++: virtual void SetClosestPoint(double _arg1, double _arg2,
            double _arg3)
        V.SetClosestPoint((float, float, float))
        C++: virtual void SetClosestPoint(const double _arg[3])
        
        Used to specify the x-y-z point coordinates when extracting the
        cluster closest to a specified point.
        """
        ...
    
    def SetColorClusters(self, bool):
        """
        V.SetColorClusters(bool)
        C++: virtual void SetColorClusters(bool _arg)
        
        Turn on/off the coloring of connected clusters.
        """
        ...
    
    def SetExtractionMode(self, p_int):
        """
        V.SetExtractionMode(int)
        C++: virtual void SetExtractionMode(int _arg)
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetExtractionModeToAllClusters(self):
        """
        V.SetExtractionModeToAllClusters()
        C++: void SetExtractionModeToAllClusters()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetExtractionModeToClosestPointCluster(self):
        """
        V.SetExtractionModeToClosestPointCluster()
        C++: void SetExtractionModeToClosestPointCluster()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetExtractionModeToLargestCluster(self):
        """
        V.SetExtractionModeToLargestCluster()
        C++: void SetExtractionModeToLargestCluster()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetExtractionModeToPointSeededClusters(self):
        """
        V.SetExtractionModeToPointSeededClusters()
        C++: void SetExtractionModeToPointSeededClusters()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetExtractionModeToSpecifiedClusters(self):
        """
        V.SetExtractionModeToSpecifiedClusters()
        C++: void SetExtractionModeToSpecifiedClusters()
        
        Control the extraction of connected surfaces.
        """
        ...
    
    def SetLocator(self, vtkAbstractPointLocator):
        """
        V.SetLocator(vtkAbstractPointLocator)
        C++: void SetLocator(vtkAbstractPointLocator *locator)
        
        Specify a point locator. By default a vtkStaticPointLocator is
        used. The locator performs efficient proximity searches near a
        specified interpolation position.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Specify the local search radius.
        """
        ...
    
    def SetScalarConnectivity(self, bool):
        """
        V.SetScalarConnectivity(bool)
        C++: virtual void SetScalarConnectivity(bool _arg)
        
        Turn on/off connectivity based on scalar value. If on, points are
        connected only if the are proximal AND the scalar value of a
        candidate point falls in the scalar range specified. Of course
        input point scalar data must be provided.
        """
        ...
    
    def SetScalarRange(self, p_float, p_float_1):
        """
        V.SetScalarRange(float, float)
        C++: virtual void SetScalarRange(double _arg1, double _arg2)
        V.SetScalarRange((float, float))
        C++: void SetScalarRange(const double _arg[2])
        
        Set the scalar range used to extract points based on scalar
        connectivity.
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


