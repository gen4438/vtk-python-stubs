"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkMoleculeAppend(__vtkmodules_vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    """
    vtkMoleculeAppend - Appends one or more molecules into a single
    molecule
    
    Superclass: vtkMoleculeAlgorithm
    
    vtkMoleculeAppend appends molecule into a single molecule. It also
    appends the associated atom data and edge data. Note that input data
    arrays should match (same number of arrays with same names in each
    input)
    
    Option MergeCoincidentAtoms specifies if coincident atoms should be
    merged or not. This may be useful in Parallel mode to remove ghost
    atoms when gather molecule on a rank. When merging, use the data of
    the non ghost atom. If none, use the data of the last coincident
    atom. This option is active by default.
    """
    def GetInput(self, p_int):
        """
        V.GetInput(int) -> vtkDataObject
        C++: vtkDataObject *GetInput(int num)
        V.GetInput() -> vtkDataObject
        C++: vtkDataObject *GetInput()
        
        Get one input to this filter. This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use vtkAlgorithm::GetInputConnection(0, num).
        """
        ...
    
    def GetMergeCoincidentAtoms(self):
        """
        V.GetMergeCoincidentAtoms() -> bool
        C++: virtual bool GetMergeCoincidentAtoms()
        
        Specify if coincident atoms (atom with exactly the same position)
        should be merged into one. True by default.
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
    
    def MergeCoincidentAtomsOff(self):
        """
        V.MergeCoincidentAtomsOff()
        C++: virtual void MergeCoincidentAtomsOff()
        
        Specify if coincident atoms (atom with exactly the same position)
        should be merged into one. True by default.
        """
        ...
    
    def MergeCoincidentAtomsOn(self):
        """
        V.MergeCoincidentAtomsOn()
        C++: virtual void MergeCoincidentAtomsOn()
        
        Specify if coincident atoms (atom with exactly the same position)
        should be merged into one. True by default.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkMoleculeAppend
        C++: vtkMoleculeAppend *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMoleculeAppend
        C++: static vtkMoleculeAppend *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetMergeCoincidentAtoms(self, bool):
        """
        V.SetMergeCoincidentAtoms(bool)
        C++: virtual void SetMergeCoincidentAtoms(bool _arg)
        
        Specify if coincident atoms (atom with exactly the same position)
        should be merged into one. True by default.
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


