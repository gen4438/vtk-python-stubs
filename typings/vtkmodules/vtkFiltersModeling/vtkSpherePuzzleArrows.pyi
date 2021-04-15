"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSpherePuzzleArrows(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkSpherePuzzleArrows - Visualize permutation of the sphere puzzle.
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkSpherePuzzleArrows creates
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
    
    def GetPermutation(self):
        """
        V.GetPermutation() -> (int, int, int, int, int, int, int, int,
            int, int, int, int, int, int, int, int, int, int, int, int,
            int, int, int, int, int, int, int, int, int, int, int, int)
        C++: virtual int *GetPermutation()
        
        Permutation is an array of puzzle piece ids. Arrows will be
        generated for any id that does not contain itself. Permutation[3]
        = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow
        from location 3 to 10.
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
        V.NewInstance() -> vtkSpherePuzzleArrows
        C++: vtkSpherePuzzleArrows *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSpherePuzzleArrows
        C++: static vtkSpherePuzzleArrows *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetPermutation(self, int_tuple):
        """
        V.SetPermutation((int, ...))
        C++: virtual void SetPermutation(const int data[])
        V.SetPermutation(vtkSpherePuzzle)
        C++: void SetPermutation(vtkSpherePuzzle *puz)
        
        Permutation is an array of puzzle piece ids. Arrows will be
        generated for any id that does not contain itself. Permutation[3]
        = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow
        from location 3 to 10.
        """
        ...
    
    def SetPermutationComponent(self, p_int, p_int_1):
        """
        V.SetPermutationComponent(int, int)
        C++: void SetPermutationComponent(int comp, int val)
        
        Permutation is an array of puzzle piece ids. Arrows will be
        generated for any id that does not contain itself. Permutation[3]
        = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow
        from location 3 to 10.
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

