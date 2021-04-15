"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkCirclePackLayoutStrategy(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkCirclePackLayoutStrategy - abstract superclass for all circle
    packing layout strategies.
    
    Superclass: vtkObject
    
    All subclasses of this class perform a circle packing layout on a
    vtkTree. This involves assigning a circle to each vertex in the tree,
    and placing that information in a data array with three components
    per tuple representing (Xcenter, Ycenter, Radius).
    
    Instances of subclasses of this class may be assigned as the layout
    strategy to vtkCirclePackLayout
    
    @par Thanks: Thanks to Thomas Otahal from Sandia National
    Laboratories for help developing this class.
    """
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
    
    def Layout(self, vtkTree, vtkDataArray, vtkDataArray_1):
        """
        V.Layout(vtkTree, vtkDataArray, vtkDataArray)
        C++: virtual void Layout(vtkTree *inputTree,
            vtkDataArray *areaArray, vtkDataArray *sizeArray)
        
        Perform the layout of the input tree, and store the circle bounds
        of each vertex as a tuple in a data array. (Xcenter, Ycenter,
        Radius).
        
        * The sizeArray may be nullptr, or may contain the desired
        * size of each vertex in the tree.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCirclePackLayoutStrategy
        C++: vtkCirclePackLayoutStrategy *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCirclePackLayoutStrategy
        C++: static vtkCirclePackLayoutStrategy *SafeDownCast(
            vtkObjectBase *o)
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

