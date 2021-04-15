"""
This type stub file was generated by pyright.
"""

from .vtkGraphLayoutStrategy import vtkGraphLayoutStrategy

class vtkRandomLayoutStrategy(vtkGraphLayoutStrategy):
    """
    vtkRandomLayoutStrategy - randomly places vertices in 2 or 3
    dimensions
    
    Superclass: vtkGraphLayoutStrategy
    
    Assigns points to the vertices of a graph randomly within a bounded
    range.
    
    Thanks:
    
    Thanks to Brian Wylie from Sandia National Laboratories for adding
    incremental layout capabilities.
    """
    def AutomaticBoundsComputationOff(self):
        """
        V.AutomaticBoundsComputationOff()
        C++: virtual void AutomaticBoundsComputationOff()
        
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified GraphBounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
        ...
    
    def AutomaticBoundsComputationOn(self):
        """
        V.AutomaticBoundsComputationOn()
        C++: virtual void AutomaticBoundsComputationOn()
        
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified GraphBounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
        ...
    
    def GetAutomaticBoundsComputation(self):
        """
        V.GetAutomaticBoundsComputation() -> int
        C++: virtual vtkTypeBool GetAutomaticBoundsComputation()
        
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified GraphBounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
        ...
    
    def GetGraphBounds(self):
        """
        V.GetGraphBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetGraphBounds()
        
        Set / get the region in space in which to place the final graph.
        The GraphBounds only affects the results if
        AutomaticBoundsComputation is off.
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
    
    def GetRandomSeed(self):
        """
        V.GetRandomSeed() -> int
        C++: virtual int GetRandomSeed()
        
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
        ...
    
    def GetRandomSeedMaxValue(self):
        """
        V.GetRandomSeedMaxValue() -> int
        C++: virtual int GetRandomSeedMaxValue()
        
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
        ...
    
    def GetRandomSeedMinValue(self):
        """
        V.GetRandomSeedMinValue() -> int
        C++: virtual int GetRandomSeedMinValue()
        
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
        ...
    
    def GetThreeDimensionalLayout(self):
        """
        V.GetThreeDimensionalLayout() -> int
        C++: virtual vtkTypeBool GetThreeDimensionalLayout()
        
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
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
    
    def Layout(self):
        """
        V.Layout()
        C++: void Layout() override;
        
        Perform the random layout.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkRandomLayoutStrategy
        C++: vtkRandomLayoutStrategy *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRandomLayoutStrategy
        C++: static vtkRandomLayoutStrategy *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAutomaticBoundsComputation(self, p_int):
        """
        V.SetAutomaticBoundsComputation(int)
        C++: virtual void SetAutomaticBoundsComputation(vtkTypeBool _arg)
        
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified GraphBounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
        ...
    
    def SetGraph(self, vtkGraph):
        """
        V.SetGraph(vtkGraph)
        C++: void SetGraph(vtkGraph *graph) override;
        
        Set the graph to layout.
        """
        ...
    
    def SetGraphBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetGraphBounds(float, float, float, float, float, float)
        C++: virtual void SetGraphBounds(double _arg1, double _arg2,
            double _arg3, double _arg4, double _arg5, double _arg6)
        V.SetGraphBounds((float, float, float, float, float, float))
        C++: virtual void SetGraphBounds(const double _arg[6])
        
        Set / get the region in space in which to place the final graph.
        The GraphBounds only affects the results if
        AutomaticBoundsComputation is off.
        """
        ...
    
    def SetRandomSeed(self, p_int):
        """
        V.SetRandomSeed(int)
        C++: virtual void SetRandomSeed(int _arg)
        
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
        ...
    
    def SetThreeDimensionalLayout(self, p_int):
        """
        V.SetThreeDimensionalLayout(int)
        C++: virtual void SetThreeDimensionalLayout(vtkTypeBool _arg)
        
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
        """
        ...
    
    def ThreeDimensionalLayoutOff(self):
        """
        V.ThreeDimensionalLayoutOff()
        C++: virtual void ThreeDimensionalLayoutOff()
        
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
        """
        ...
    
    def ThreeDimensionalLayoutOn(self):
        """
        V.ThreeDimensionalLayoutOn()
        C++: virtual void ThreeDimensionalLayoutOn()
        
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
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

