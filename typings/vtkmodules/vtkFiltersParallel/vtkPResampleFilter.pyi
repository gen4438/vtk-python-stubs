"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkPResampleFilter(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkPResampleFilter - probe dataset in parallel using a vtkImageData
    
    Superclass: vtkImageAlgorithm
    """
    def GetController(self):
        """
        V.GetController() -> vtkMultiProcessController
        C++: virtual vtkMultiProcessController *GetController()
        
        Set and get the controller.
        """
        ...
    
    def GetCustomSamplingBounds(self):
        """
        V.GetCustomSamplingBounds() -> (float, float, float, float, float,
             float)
        C++: virtual double *GetCustomSamplingBounds()
        
        Set/Get sampling bounds. If (UseInputBounds == 1) then the
        sampling bounds won't be used.
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
    
    def GetSamplingDimension(self):
        """
        V.GetSamplingDimension() -> (int, int, int)
        C++: virtual int *GetSamplingDimension()
        
        Set/Get sampling dimension along each axis. Default will be
        [10,10,10]
        """
        ...
    
    def GetUseInputBounds(self):
        """
        V.GetUseInputBounds() -> int
        C++: virtual vtkTypeBool GetUseInputBounds()
        
        Set/Get if the filter should use Input bounds to sub-sample the
        data. By default it is set to 1.
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
        V.NewInstance() -> vtkPResampleFilter
        C++: vtkPResampleFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPResampleFilter
        C++: static vtkPResampleFilter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetController(self, vtkMultiProcessController):
        """
        V.SetController(vtkMultiProcessController)
        C++: virtual void SetController(vtkMultiProcessController *)
        
        Set and get the controller.
        """
        ...
    
    def SetCustomSamplingBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetCustomSamplingBounds(float, float, float, float, float,
            float)
        C++: virtual void SetCustomSamplingBounds(double _arg1,
            double _arg2, double _arg3, double _arg4, double _arg5,
            double _arg6)
        V.SetCustomSamplingBounds((float, float, float, float, float,
            float))
        C++: virtual void SetCustomSamplingBounds(const double _arg[6])
        
        Set/Get sampling bounds. If (UseInputBounds == 1) then the
        sampling bounds won't be used.
        """
        ...
    
    def SetSamplingDimension(self, p_int, p_int_1, p_int_2):
        """
        V.SetSamplingDimension(int, int, int)
        C++: virtual void SetSamplingDimension(int _arg1, int _arg2,
            int _arg3)
        V.SetSamplingDimension((int, int, int))
        C++: virtual void SetSamplingDimension(const int _arg[3])
        
        Set/Get sampling dimension along each axis. Default will be
        [10,10,10]
        """
        ...
    
    def SetUseInputBounds(self, p_int):
        """
        V.SetUseInputBounds(int)
        C++: virtual void SetUseInputBounds(vtkTypeBool _arg)
        
        Set/Get if the filter should use Input bounds to sub-sample the
        data. By default it is set to 1.
        """
        ...
    
    def UseInputBoundsOff(self):
        """
        V.UseInputBoundsOff()
        C++: virtual void UseInputBoundsOff()
        
        Set/Get if the filter should use Input bounds to sub-sample the
        data. By default it is set to 1.
        """
        ...
    
    def UseInputBoundsOn(self):
        """
        V.UseInputBoundsOn()
        C++: virtual void UseInputBoundsOn()
        
        Set/Get if the filter should use Input bounds to sub-sample the
        data. By default it is set to 1.
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


