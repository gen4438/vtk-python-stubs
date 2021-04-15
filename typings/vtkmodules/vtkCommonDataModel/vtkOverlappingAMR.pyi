"""
This type stub file was generated by pyright.
"""

from .vtkUniformGridAMR import vtkUniformGridAMR

class vtkOverlappingAMR(vtkUniformGridAMR):
    """
    vtkOverlappingAMR - hierarchical dataset of vtkUniformGrids
    
    Superclass: vtkUniformGridAMR
    
    vtkOverlappingAMR extends vtkUniformGridAMR by exposing access to the
    amr meta data, which stores all structural information represented by
    an vtkAMRInformation object
    
    @sa
    vtkAMRInformation
    """
    def Audit(self):
        """
        V.Audit()
        C++: void Audit()
        
        Check whether the data set is internally consistent, e.g. whether
        the meta data and actual data blocks match. Incorrectness will be
        reported as error messages
        """
        ...
    
    def FindGrid(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.FindGrid([float, float, float], int, int) -> bool
        C++: bool FindGrid(double q[3], unsigned int &level,
            unsigned int &gridId)
        
        Given a point q, find the highest level grid that contains it.
        """
        ...
    
    def GenerateParentChildInformation(self):
        """
        V.GenerateParentChildInformation()
        C++: void GenerateParentChildInformation()
        
        Generate the parent/child relationships - needed to be called
        before GetParents or GetChildren can be used!
        """
        ...
    
    def GetAMRBlockSourceIndex(self, p_int, p_int_1):
        """
        V.GetAMRBlockSourceIndex(int, int) -> int
        C++: int GetAMRBlockSourceIndex(unsigned int level,
            unsigned int id)
        
        Set/Get the source id of a block. The source id is produced by an
        AMR source, e.g. a file reader might set this to be a file block
        id
        """
        ...
    
    def GetAMRBox(self, p_int, p_int_1):
        """
        V.GetAMRBox(int, int) -> vtkAMRBox
        C++: const vtkAMRBox &GetAMRBox(unsigned int level,
            unsigned int id)
        
        Set/Get the AMRBox for a given block
        """
        ...
    
    def GetAMRInfo(self):
        """
        V.GetAMRInfo() -> vtkAMRInformation
        C++: vtkAMRInformation *GetAMRInfo() override;
        
        Get/Set the internal representation of amr meta meta data
        """
        ...
    
    def GetBounds(self, p_int, p_int_1, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBounds(int, int, [float, float, float, float, float, float])
        C++: void GetBounds(unsigned int level, unsigned int id,
            double bb[6])
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double b[6])
        
        Returns the bounding information of a data set.
        """
        ...
    
    def GetChildren(self, p_int, p_int_1, p_int_2):
        """
        V.GetChildren(int, int, int) -> (int, ...)
        C++: unsigned int *GetChildren(unsigned int level,
            unsigned int index, unsigned int &numChildren)
        
        Return a pointer to Children of a block.  The first entry is the
        number of children the block has followed by its children ids in
        level+1. If none exits it returns nullptr.
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkOverlappingAMR
        C++: static vtkOverlappingAMR *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkOverlappingAMR
        C++: static vtkOverlappingAMR *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return class name of data type (see vtkType.h for definitions).
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
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, ...)
        C++: double *GetOrigin()
        V.GetOrigin(int, int, [float, float, float])
        C++: void GetOrigin(unsigned int level, unsigned int id,
            double origin[3])
        
        Get/Set the global origin of the amr data set
        """
        ...
    
    def GetParents(self, p_int, p_int_1, p_int_2):
        """
        V.GetParents(int, int, int) -> (int, ...)
        C++: unsigned int *GetParents(unsigned int level,
            unsigned int index, unsigned int &numParents)
        
        Return a pointer to Parents of a block.  The first entry is the
        number of parents the block has followed by its parent ids in
        level-1. If none exits it returns nullptr.
        """
        ...
    
    def GetRefinementRatio(self, p_int):
        """
        V.GetRefinementRatio(int) -> int
        C++: int GetRefinementRatio(unsigned int level)
        V.GetRefinementRatio(vtkCompositeDataIterator) -> int
        C++: int GetRefinementRatio(vtkCompositeDataIterator *iter)
        
        Returns the refinement of a given level.
        """
        ...
    
    def GetSpacing(self, p_int, p_float=..., p_float=..., p_float=...):
        """
        V.GetSpacing(int, [float, float, float])
        C++: void GetSpacing(unsigned int level, double spacing[3])
        
        Get/Set the grid spacing at a given level
        """
        ...
    
    def HasChildrenInformation(self):
        """
        V.HasChildrenInformation() -> bool
        C++: bool HasChildrenInformation()
        
        Return whether parent child information has been generated
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
        V.NewInstance() -> vtkOverlappingAMR
        C++: vtkOverlappingAMR *NewInstance()
        """
        ...
    
    def NewIterator(self):
        """
        V.NewIterator() -> vtkCompositeDataIterator
        C++: vtkCompositeDataIterator *NewIterator() override;
        
        Return a new iterator (the iterator has to be deleted by the
        user).
        """
        ...
    
    def NUMBER_OF_BLANKED_POINTS(self):
        """
        V.NUMBER_OF_BLANKED_POINTS() -> vtkInformationIdTypeKey
        C++: static vtkInformationIdTypeKey *NUMBER_OF_BLANKED_POINTS()
        """
        ...
    
    def PrintParentChildInfo(self, p_int, p_int_1):
        """
        V.PrintParentChildInfo(int, int)
        C++: void PrintParentChildInfo(unsigned int level,
            unsigned int index)
        
        Prints the parents and children of a requested block (Debug
        Routine)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOverlappingAMR
        C++: static vtkOverlappingAMR *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAMRBlockSourceIndex(self, p_int, p_int_1, p_int_2):
        """
        V.SetAMRBlockSourceIndex(int, int, int)
        C++: void SetAMRBlockSourceIndex(unsigned int level,
            unsigned int id, int sourceId)
        
        Set/Get the source id of a block. The source id is produced by an
        AMR source, e.g. a file reader might set this to be a file block
        id
        """
        ...
    
    def SetAMRBox(self, p_int, p_int_1, vtkAMRBox):
        """
        V.SetAMRBox(int, int, vtkAMRBox)
        C++: void SetAMRBox(unsigned int level, unsigned int id,
            const vtkAMRBox &box)
        
        Set/Get the AMRBox for a given block
        """
        ...
    
    def SetAMRInfo(self, vtkAMRInformation):
        """
        V.SetAMRInfo(vtkAMRInformation)
        C++: void SetAMRInfo(vtkAMRInformation *info) override;
        
        Get/Set the meta AMR meta data
        """
        ...
    
    def SetOrigin(self, ):
        """
        V.SetOrigin((float, float, float))
        C++: void SetOrigin(const double origin[3])
        
        Get/Set the global origin of the amr data set
        """
        ...
    
    def SetRefinementRatio(self, p_int, p_int_1):
        """
        V.SetRefinementRatio(int, int)
        C++: void SetRefinementRatio(unsigned int level, int refRatio)
        
        Sets the refinement of a given level. The spacing at level
        level+1 is defined as spacing(level+1) =
        spacing(level)/refRatio(level). Note that currently, this is not
        enforced by this class however some algorithms might not function
        properly if the spacing in the blocks (vtkUniformGrid) does not
        match the one described by the refinement ratio.
        """
        ...
    
    def SetSpacing(self, p_int, ):
        """
        V.SetSpacing(int, (float, float, float))
        C++: void SetSpacing(unsigned int level, const double spacing[3])
        
        Get/Set the grid spacing at a given level
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

