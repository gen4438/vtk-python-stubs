"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSuperquadricSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkSuperquadricSource - create a polygonal superquadric centered at
    the origin
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkSuperquadricSource creates a superquadric (represented by
    polygons) of specified size centered at the origin. The alignment of
    the axis of the superquadric along one of the global axes can be
    specified. The resolution (polygonal discretization) in both the
    latitude (phi) and longitude (theta) directions can be specified.
    Roundness parameters (PhiRoundness and ThetaRoundness) control the
    shape of the superquadric.  The Toroidal boolean controls whether a
    toroidal superquadric is produced.  If so, the Thickness parameter
    controls the thickness of the toroid:  0 is the thinnest allowable
    toroid, and 1 has a minimum sized hole.  The Scale parameters allow
    the superquadric to be scaled in x, y, and z (normal vectors are
    correctly generated in any case).  The Size parameter controls size
    of the superquadric.
    
    This code is based on "Rigid physically based superquadrics", A. H.
    Barr, in "Graphics Gems III", David Kirk, ed., Academic Press, 1992.
    
    @warning
    Resolution means the number of latitude or longitude lines for a
    complete superquadric. The resolution parameters are rounded to the
    nearest 4 in phi and 8 in theta.
    
    @warning
    Texture coordinates are not equally distributed around all
    superquadrics.
    
    @warning
    The Size and Thickness parameters control coefficients of
    superquadric generation, and may do not exactly describe the size of
    the superquadric.
    """
    def GetAxisOfSymmetry(self):
        """
        V.GetAxisOfSymmetry() -> int
        C++: virtual int GetAxisOfSymmetry()
        
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: virtual double *GetCenter()
        
        Set the center of the superquadric. Default is 0,0,0.
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
    
    def GetOutputPointsPrecision(self):
        """
        V.GetOutputPointsPrecision() -> int
        C++: virtual int GetOutputPointsPrecision()
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def GetPhiResolution(self):
        """
        V.GetPhiResolution() -> int
        C++: virtual int GetPhiResolution()
        
        Set the number of points in the latitude direction. Initial value
        is 16.
        """
        ...
    
    def GetPhiRoundness(self):
        """
        V.GetPhiRoundness() -> float
        C++: virtual double GetPhiRoundness()
        
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
        ...
    
    def GetScale(self):
        """
        V.GetScale() -> (float, float, float)
        C++: virtual double *GetScale()
        
        Set the scale factors of the superquadric. Default is 1,1,1.
        """
        ...
    
    def GetSize(self):
        """
        V.GetSize() -> float
        C++: virtual double GetSize()
        
        Set/Get Superquadric isotropic size. Initial value is 0.5;
        """
        ...
    
    def GetThetaResolution(self):
        """
        V.GetThetaResolution() -> int
        C++: virtual int GetThetaResolution()
        
        Set the number of points in the longitude direction. Initial
        value is 16.
        """
        ...
    
    def GetThetaRoundness(self):
        """
        V.GetThetaRoundness() -> float
        C++: virtual double GetThetaRoundness()
        
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
        ...
    
    def GetThickness(self):
        """
        V.GetThickness() -> float
        C++: virtual double GetThickness()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
        ...
    
    def GetThicknessMaxValue(self):
        """
        V.GetThicknessMaxValue() -> float
        C++: virtual double GetThicknessMaxValue()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
        ...
    
    def GetThicknessMinValue(self):
        """
        V.GetThicknessMinValue() -> float
        C++: virtual double GetThicknessMinValue()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
        ...
    
    def GetToroidal(self):
        """
        V.GetToroidal() -> int
        C++: virtual vtkTypeBool GetToroidal()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
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
        V.NewInstance() -> vtkSuperquadricSource
        C++: vtkSuperquadricSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSuperquadricSource
        C++: static vtkSuperquadricSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAxisOfSymmetry(self, p_int):
        """
        V.SetAxisOfSymmetry(int)
        C++: virtual void SetAxisOfSymmetry(int _arg)
        
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ...
    
    def SetCenter(self, p_float, p_float_1, p_float_2):
        """
        V.SetCenter(float, float, float)
        C++: virtual void SetCenter(double _arg1, double _arg2,
            double _arg3)
        V.SetCenter((float, float, float))
        C++: virtual void SetCenter(const double _arg[3])
        
        Set the center of the superquadric. Default is 0,0,0.
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def SetPhiResolution(self, p_int):
        """
        V.SetPhiResolution(int)
        C++: void SetPhiResolution(int i)
        
        Set the number of points in the latitude direction. Initial value
        is 16.
        """
        ...
    
    def SetPhiRoundness(self, p_float):
        """
        V.SetPhiRoundness(float)
        C++: void SetPhiRoundness(double e)
        
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
        ...
    
    def SetScale(self, p_float, p_float_1, p_float_2):
        """
        V.SetScale(float, float, float)
        C++: virtual void SetScale(double _arg1, double _arg2,
            double _arg3)
        V.SetScale((float, float, float))
        C++: virtual void SetScale(const double _arg[3])
        
        Set the scale factors of the superquadric. Default is 1,1,1.
        """
        ...
    
    def SetSize(self, p_float):
        """
        V.SetSize(float)
        C++: virtual void SetSize(double _arg)
        
        Set/Get Superquadric isotropic size. Initial value is 0.5;
        """
        ...
    
    def SetThetaResolution(self, p_int):
        """
        V.SetThetaResolution(int)
        C++: void SetThetaResolution(int i)
        
        Set the number of points in the longitude direction. Initial
        value is 16.
        """
        ...
    
    def SetThetaRoundness(self, p_float):
        """
        V.SetThetaRoundness(float)
        C++: void SetThetaRoundness(double e)
        
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
        ...
    
    def SetThickness(self, p_float):
        """
        V.SetThickness(float)
        C++: virtual void SetThickness(double _arg)
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
        ...
    
    def SetToroidal(self, p_int):
        """
        V.SetToroidal(int)
        C++: virtual void SetToroidal(vtkTypeBool _arg)
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
        """
        ...
    
    def SetXAxisOfSymmetry(self):
        """
        V.SetXAxisOfSymmetry()
        C++: void SetXAxisOfSymmetry()
        
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ...
    
    def SetYAxisOfSymmetry(self):
        """
        V.SetYAxisOfSymmetry()
        C++: void SetYAxisOfSymmetry()
        
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ...
    
    def SetZAxisOfSymmetry(self):
        """
        V.SetZAxisOfSymmetry()
        C++: void SetZAxisOfSymmetry()
        
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ...
    
    def ToroidalOff(self):
        """
        V.ToroidalOff()
        C++: virtual void ToroidalOff()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
        """
        ...
    
    def ToroidalOn(self):
        """
        V.ToroidalOn()
        C++: virtual void ToroidalOn()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
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

