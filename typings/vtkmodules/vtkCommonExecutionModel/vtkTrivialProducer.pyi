"""
This type stub file was generated by pyright.
"""

from .vtkAlgorithm import vtkAlgorithm

class vtkTrivialProducer(vtkAlgorithm):
    """
    vtkTrivialProducer - Producer for stand-alone data objects.
    
    Superclass: vtkAlgorithm
    
    vtkTrivialProducer allows stand-alone data objects to be connected as
    inputs in a pipeline.  All data objects that are connected to a
    pipeline involving vtkAlgorithm must have a producer.  This trivial
    producer allows data objects that are hand-constructed in a program
    without another vtk producer to be connected.
    """
    def FillOutputDataInformation(self, vtkDataObject, vtkInformation):
        """
        V.FillOutputDataInformation(vtkDataObject, vtkInformation)
        C++: static void FillOutputDataInformation(vtkDataObject *output,
            vtkInformation *outInfo)
        
        This method can be used to copy meta-data from an existing data
        object to an information object. For example, whole extent, image
        data spacing, origin etc.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        The modified time of this producer is the newer of this object or
        the assigned output.
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
    
    def GetWholeExtent(self):
        """
        V.GetWholeExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetWholeExtent()
        
        Set the whole extent to use for the data this producer is
        producing. This may be different than the extent of the output
        data when the trivial producer is used in parallel.
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
        V.NewInstance() -> vtkTrivialProducer
        C++: vtkTrivialProducer *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTrivialProducer
        C++: static vtkTrivialProducer *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetOutput(self, vtkDataObject):
        """
        V.SetOutput(vtkDataObject)
        C++: virtual void SetOutput(vtkDataObject *output)
        
        Set the data object that is "produced" by this producer.  It is
        never really modified.
        """
        ...
    
    def SetWholeExtent(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetWholeExtent(int, int, int, int, int, int)
        C++: virtual void SetWholeExtent(int _arg1, int _arg2, int _arg3,
            int _arg4, int _arg5, int _arg6)
        V.SetWholeExtent((int, int, int, int, int, int))
        C++: virtual void SetWholeExtent(const int _arg[6])
        
        Set the whole extent to use for the data this producer is
        producing. This may be different than the extent of the output
        data when the trivial producer is used in parallel.
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

