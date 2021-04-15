"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkGraphLayout(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkGraphLayout - layout a graph in 2 or 3 dimensions
    
    Superclass: vtkGraphAlgorithm
    
    This class is a shell for many graph layout strategies which may be
    set using the SetLayoutStrategy() function.  The layout strategies do
    the actual work.
    
    Thanks:
    
    Thanks to Brian Wylie from Sandia National Laboratories for adding
    incremental layout capabilities.
    """
    def GetLayoutStrategy(self):
        """
        V.GetLayoutStrategy() -> vtkGraphLayoutStrategy
        C++: virtual vtkGraphLayoutStrategy *GetLayoutStrategy()
        
        The layout strategy to use during graph layout.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the modification time of the layout algorithm.
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
    
    def GetTransform(self):
        """
        V.GetTransform() -> vtkAbstractTransform
        C++: virtual vtkAbstractTransform *GetTransform()
        
        Transform the graph vertices after the layout.
        """
        ...
    
    def GetUseTransform(self):
        """
        V.GetUseTransform() -> bool
        C++: virtual bool GetUseTransform()
        
        Whether to use the specified transform after layout.
        """
        ...
    
    def GetZRange(self):
        """
        V.GetZRange() -> float
        C++: virtual double GetZRange()
        
        Set the ZRange for the output data. If the initial layout is
        planar (i.e. all z coordinates are zero), the coordinates will be
        evenly spaced from 0.0 to ZRange. The default is zero, which has
        no effect.
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
    
    def IsLayoutComplete(self):
        """
        V.IsLayoutComplete() -> int
        C++: virtual int IsLayoutComplete()
        
        Ask the layout algorithm if the layout is complete
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
        V.NewInstance() -> vtkGraphLayout
        C++: vtkGraphLayout *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGraphLayout
        C++: static vtkGraphLayout *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetLayoutStrategy(self, vtkGraphLayoutStrategy):
        """
        V.SetLayoutStrategy(vtkGraphLayoutStrategy)
        C++: void SetLayoutStrategy(vtkGraphLayoutStrategy *strategy)
        
        The layout strategy to use during graph layout.
        """
        ...
    
    def SetTransform(self, vtkAbstractTransform):
        """
        V.SetTransform(vtkAbstractTransform)
        C++: virtual void SetTransform(vtkAbstractTransform *t)
        
        Transform the graph vertices after the layout.
        """
        ...
    
    def SetUseTransform(self, bool):
        """
        V.SetUseTransform(bool)
        C++: virtual void SetUseTransform(bool _arg)
        
        Whether to use the specified transform after layout.
        """
        ...
    
    def SetZRange(self, p_float):
        """
        V.SetZRange(float)
        C++: virtual void SetZRange(double _arg)
        
        Set the ZRange for the output data. If the initial layout is
        planar (i.e. all z coordinates are zero), the coordinates will be
        evenly spaced from 0.0 to ZRange. The default is zero, which has
        no effect.
        """
        ...
    
    def UseTransformOff(self):
        """
        V.UseTransformOff()
        C++: virtual void UseTransformOff()
        
        Whether to use the specified transform after layout.
        """
        ...
    
    def UseTransformOn(self):
        """
        V.UseTransformOn()
        C++: virtual void UseTransformOn()
        
        Whether to use the specified transform after layout.
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

