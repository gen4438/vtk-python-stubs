"""
This type stub file was generated by pyright.
"""

from .vtkDepthImageProcessingPass import vtkDepthImageProcessingPass

class vtkPointFillPass(vtkDepthImageProcessingPass):
    """
    vtkPointFillPass - Implement a post-processing fillpass
    
    Superclass: vtkDepthImageProcessingPass
    
    This pass is designed to fill in rendering of sparse point
    sets/coulds The delegate is used once and is usually set to a
    vtkCameraPass or to a post-processing pass.
    
    @sa
    vtkRenderPass
    """
    def GetCandidatePointRatio(self):
        """
        V.GetCandidatePointRatio() -> float
        C++: virtual float GetCandidatePointRatio()
        
        How far in front of a point must a neighboring point be to be
        used as a filler candidate.  Expressed as a multiple of the
        points distance from the camera. Defaults to 0.95
        """
        ...
    
    def GetMinimumCandidateAngle(self):
        """
        V.GetMinimumCandidateAngle() -> float
        C++: virtual float GetMinimumCandidateAngle()
        
        How large of an angle must the filler candidates span before a
        point will be filled. Expressed in radians. A value of pi will
        keep edges from growing out. Large values require more support,
        lower values less.
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
        V.NewInstance() -> vtkPointFillPass
        C++: vtkPointFillPass *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        
        Release graphics resources and ask components to release their
        own resources.
        \pre w_exists: w!=0
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPointFillPass
        C++: static vtkPointFillPass *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCandidatePointRatio(self, p_float):
        """
        V.SetCandidatePointRatio(float)
        C++: virtual void SetCandidatePointRatio(float _arg)
        
        How far in front of a point must a neighboring point be to be
        used as a filler candidate.  Expressed as a multiple of the
        points distance from the camera. Defaults to 0.95
        """
        ...
    
    def SetMinimumCandidateAngle(self, p_float):
        """
        V.SetMinimumCandidateAngle(float)
        C++: virtual void SetMinimumCandidateAngle(float _arg)
        
        How large of an angle must the filler candidates span before a
        point will be filled. Expressed in radians. A value of pi will
        keep edges from growing out. Large values require more support,
        lower values less.
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

