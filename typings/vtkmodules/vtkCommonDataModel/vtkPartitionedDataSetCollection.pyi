"""
This type stub file was generated by pyright.
"""

from .vtkDataObjectTree import vtkDataObjectTree

class vtkPartitionedDataSetCollection(vtkDataObjectTree):
    """
    vtkPartitionedDataSetCollection - Composite dataset that groups
    datasets as a collection.
    
    Superclass: vtkDataObjectTree
    
    vtkPartitionedDataSetCollection is a vtkCompositeDataSet that stores
    a collection of vtkPartitionedDataSets. These items can represent
    different concepts depending on the context. For example, they can
    represent region of different materials in a simulation or parts in
    an assembly. It is not requires that items have anything in common.
    For example, they can have completely different point or cell arrays.
    """
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkPartitionedDataSetCollection
        C++: static vtkPartitionedDataSetCollection *GetData(
            vtkInformation *info)
        V.GetData(vtkInformationVector, int)
            -> vtkPartitionedDataSetCollection
        C++: static vtkPartitionedDataSetCollection *GetData(
            vtkInformationVector *v, int i=0)
        
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
    
    def GetMetaData(self, p_int):
        """
        V.GetMetaData(int) -> vtkInformation
        C++: vtkInformation *GetMetaData(unsigned int idx)
        V.GetMetaData(vtkCompositeDataIterator) -> vtkInformation
        C++: vtkInformation *GetMetaData(vtkCompositeDataIterator *iter)
            override;
        
        Returns the meta-data for the block. If none is already present,
        a new vtkInformation object will be allocated. Use HasMetaData to
        avoid allocating vtkInformation objects.
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
    
    def GetNumberOfPartitionedDataSets(self):
        """
        V.GetNumberOfPartitionedDataSets() -> int
        C++: unsigned int GetNumberOfPartitionedDataSets()
        
        Returns the number of blocks.
        """
        ...
    
    def GetPartitionedDataSet(self, p_int):
        """
        V.GetPartitionedDataSet(int) -> vtkPartitionedDataSet
        C++: vtkPartitionedDataSet *GetPartitionedDataSet(
            unsigned int idx)
        
        Returns the block at the given index. It is recommended that one
        uses the iterators to iterate over composite datasets rather than
        using this API.
        """
        ...
    
    def HasMetaData(self, p_int):
        """
        V.HasMetaData(int) -> int
        C++: int HasMetaData(unsigned int idx)
        V.HasMetaData(vtkCompositeDataIterator) -> int
        C++: int HasMetaData(vtkCompositeDataIterator *iter) override;
        
        Returns true if meta-data is available for a given block.
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
        V.NewInstance() -> vtkPartitionedDataSetCollection
        C++: vtkPartitionedDataSetCollection *NewInstance()
        """
        ...
    
    def RemovePartitionedDataSet(self, p_int):
        """
        V.RemovePartitionedDataSet(int)
        C++: void RemovePartitionedDataSet(unsigned int idx)
        
        Remove the given block from the dataset.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPartitionedDataSetCollection
        C++: static vtkPartitionedDataSetCollection *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfPartitionedDataSets(self, p_int):
        """
        V.SetNumberOfPartitionedDataSets(int)
        C++: void SetNumberOfPartitionedDataSets(unsigned int numDataSets)
        
        Set the number of blocks. This will cause allocation if the new
        number of blocks is greater than the current size. All new blocks
        are initialized to null.
        """
        ...
    
    def SetPartitionedDataSet(self, p_int, vtkPartitionedDataSet):
        """
        V.SetPartitionedDataSet(int, vtkPartitionedDataSet)
        C++: void SetPartitionedDataSet(unsigned int idx,
            vtkPartitionedDataSet *dataset)
        
        Sets the data object as the given block. The total number of
        blocks will be resized to fit the requested block no.
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


