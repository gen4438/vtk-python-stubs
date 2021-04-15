"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonTransforms as __vtkmodules_vtkCommonTransforms

class vtkIterativeClosestPointTransform(__vtkmodules_vtkCommonTransforms.vtkLinearTransform):
    """
    vtkIterativeClosestPointTransform - Implementation of the ICP
    algorithm.
    
    Superclass: vtkLinearTransform
    
    Match two surfaces using the iterative closest point (ICP) algorithm.
    The core of the algorithm is to match each vertex in one surface with
    the closest surface point on the other, then apply the transformation
    that modify one surface to best match the other (in a least square
    sense). This has to be iterated to get proper convergence of the
    surfaces.@attention Use vtkTransformPolyDataFilter to apply the
    resulting ICP transform to your data. You might also set it to your
    actor's user transform.@attention This class makes use of
    vtkLandmarkTransform internally to compute the best fit. Use the
    GetLandmarkTransform member to get a pointer to that transform and
    set its parameters. You might, for example, constrain the number of
    degrees of freedom of the solution (i.e. rigid body, similarity,
    etc.) by checking the vtkLandmarkTransform documentation for its
    SetMode member.
    @sa
    vtkLandmarkTransform
    """
    def CheckMeanDistanceOff(self):
        """
        V.CheckMeanDistanceOff()
        C++: virtual void CheckMeanDistanceOff()
        
        Force the algorithm to check the mean distance between two
        iterations. Default is Off.
        """
        ...
    
    def CheckMeanDistanceOn(self):
        """
        V.CheckMeanDistanceOn()
        C++: virtual void CheckMeanDistanceOn()
        
        Force the algorithm to check the mean distance between two
        iterations. Default is Off.
        """
        ...
    
    def GetCheckMeanDistance(self):
        """
        V.GetCheckMeanDistance() -> int
        C++: virtual vtkTypeBool GetCheckMeanDistance()
        
        Force the algorithm to check the mean distance between two
        iterations. Default is Off.
        """
        ...
    
    def GetLandmarkTransform(self):
        """
        V.GetLandmarkTransform() -> vtkLandmarkTransform
        C++: virtual vtkLandmarkTransform *GetLandmarkTransform()
        
        Get the internal landmark transform. Use it to constrain the
        number of degrees of freedom of the solution (i.e. rigid body,
        similarity, etc.).
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkCellLocator
        C++: virtual vtkCellLocator *GetLocator()
        
        Set/Get a spatial locator for speeding up the search process. An
        instance of vtkCellLocator is used by default.
        """
        ...
    
    def GetMaximumMeanDistance(self):
        """
        V.GetMaximumMeanDistance() -> float
        C++: virtual double GetMaximumMeanDistance()
        
        Set/Get the maximum mean distance between two iteration. If the
        mean distance is lower than this, the convergence stops. The
        default is 0.01.
        """
        ...
    
    def GetMaximumNumberOfIterations(self):
        """
        V.GetMaximumNumberOfIterations() -> int
        C++: virtual int GetMaximumNumberOfIterations()
        
        Set/Get the maximum number of iterations. Default is 50.
        """
        ...
    
    def GetMaximumNumberOfLandmarks(self):
        """
        V.GetMaximumNumberOfLandmarks() -> int
        C++: virtual int GetMaximumNumberOfLandmarks()
        
        Set/Get the maximum number of landmarks sampled in your dataset.
        If your dataset is dense, then you will typically not need all
        the points to compute the ICP transform. The default is 200.
        """
        ...
    
    def GetMeanDistance(self):
        """
        V.GetMeanDistance() -> float
        C++: virtual double GetMeanDistance()
        
        Get the mean distance between the last two iterations.
        """
        ...
    
    def GetMeanDistanceMode(self):
        """
        V.GetMeanDistanceMode() -> int
        C++: virtual int GetMeanDistanceMode()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def GetMeanDistanceModeAsString(self):
        """
        V.GetMeanDistanceModeAsString() -> string
        C++: const char *GetMeanDistanceModeAsString()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def GetMeanDistanceModeMaxValue(self):
        """
        V.GetMeanDistanceModeMaxValue() -> int
        C++: virtual int GetMeanDistanceModeMaxValue()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def GetMeanDistanceModeMinValue(self):
        """
        V.GetMeanDistanceModeMinValue() -> int
        C++: virtual int GetMeanDistanceModeMinValue()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
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
    
    def GetNumberOfIterations(self):
        """
        V.GetNumberOfIterations() -> int
        C++: virtual int GetNumberOfIterations()
        
        Get the number of iterations since the last update
        """
        ...
    
    def GetSource(self):
        """
        V.GetSource() -> vtkDataSet
        C++: virtual vtkDataSet *GetSource()
        
        Specify the source and target data sets.
        """
        ...
    
    def GetStartByMatchingCentroids(self):
        """
        V.GetStartByMatchingCentroids() -> int
        C++: virtual vtkTypeBool GetStartByMatchingCentroids()
        
        Starts the process by translating source centroid to target
        centroid. The default is Off.
        """
        ...
    
    def GetTarget(self):
        """
        V.GetTarget() -> vtkDataSet
        C++: virtual vtkDataSet *GetTarget()
        
        Specify the source and target data sets.
        """
        ...
    
    def Inverse(self):
        """
        V.Inverse()
        C++: void Inverse() override;
        
        Invert the transformation.  This is done by switching the source
        and target.
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
    
    def MakeTransform(self):
        """
        V.MakeTransform() -> vtkAbstractTransform
        C++: vtkAbstractTransform *MakeTransform() override;
        
        Make another transform of the same type.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkIterativeClosestPointTransform
        C++: vtkIterativeClosestPointTransform *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkIterativeClosestPointTransform
        C++: static vtkIterativeClosestPointTransform *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetCheckMeanDistance(self, p_int):
        """
        V.SetCheckMeanDistance(int)
        C++: virtual void SetCheckMeanDistance(vtkTypeBool _arg)
        
        Force the algorithm to check the mean distance between two
        iterations. Default is Off.
        """
        ...
    
    def SetLocator(self, vtkCellLocator):
        """
        V.SetLocator(vtkCellLocator)
        C++: void SetLocator(vtkCellLocator *locator)
        
        Set/Get a spatial locator for speeding up the search process. An
        instance of vtkCellLocator is used by default.
        """
        ...
    
    def SetMaximumMeanDistance(self, p_float):
        """
        V.SetMaximumMeanDistance(float)
        C++: virtual void SetMaximumMeanDistance(double _arg)
        
        Set/Get the maximum mean distance between two iteration. If the
        mean distance is lower than this, the convergence stops. The
        default is 0.01.
        """
        ...
    
    def SetMaximumNumberOfIterations(self, p_int):
        """
        V.SetMaximumNumberOfIterations(int)
        C++: virtual void SetMaximumNumberOfIterations(int _arg)
        
        Set/Get the maximum number of iterations. Default is 50.
        """
        ...
    
    def SetMaximumNumberOfLandmarks(self, p_int):
        """
        V.SetMaximumNumberOfLandmarks(int)
        C++: virtual void SetMaximumNumberOfLandmarks(int _arg)
        
        Set/Get the maximum number of landmarks sampled in your dataset.
        If your dataset is dense, then you will typically not need all
        the points to compute the ICP transform. The default is 200.
        """
        ...
    
    def SetMeanDistanceMode(self, p_int):
        """
        V.SetMeanDistanceMode(int)
        C++: virtual void SetMeanDistanceMode(int _arg)
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def SetMeanDistanceModeToAbsoluteValue(self):
        """
        V.SetMeanDistanceModeToAbsoluteValue()
        C++: void SetMeanDistanceModeToAbsoluteValue()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def SetMeanDistanceModeToRMS(self):
        """
        V.SetMeanDistanceModeToRMS()
        C++: void SetMeanDistanceModeToRMS()
        
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
        ...
    
    def SetSource(self, vtkDataSet):
        """
        V.SetSource(vtkDataSet)
        C++: void SetSource(vtkDataSet *source)
        
        Specify the source and target data sets.
        """
        ...
    
    def SetStartByMatchingCentroids(self, p_int):
        """
        V.SetStartByMatchingCentroids(int)
        C++: virtual void SetStartByMatchingCentroids(vtkTypeBool _arg)
        
        Starts the process by translating source centroid to target
        centroid. The default is Off.
        """
        ...
    
    def SetTarget(self, vtkDataSet):
        """
        V.SetTarget(vtkDataSet)
        C++: void SetTarget(vtkDataSet *target)
        
        Specify the source and target data sets.
        """
        ...
    
    def StartByMatchingCentroidsOff(self):
        """
        V.StartByMatchingCentroidsOff()
        C++: virtual void StartByMatchingCentroidsOff()
        
        Starts the process by translating source centroid to target
        centroid. The default is Off.
        """
        ...
    
    def StartByMatchingCentroidsOn(self):
        """
        V.StartByMatchingCentroidsOn()
        C++: virtual void StartByMatchingCentroidsOn()
        
        Starts the process by translating source centroid to target
        centroid. The default is Off.
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


