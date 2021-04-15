"""
This type stub file was generated by pyright.
"""

from .vtkDataObjectTree import vtkDataObjectTree

class vtkMultiBlockDataSet(vtkDataObjectTree):
    """
    vtkMultiBlockDataSet - Composite dataset that organizes datasets into
    blocks.
    
    Superclass: vtkDataObjectTree
    
    vtkMultiBlockDataSet is a vtkCompositeDataSet that stores a hierarchy
    of datasets. The dataset collection consists of multiple blocks. Each
    block can itself be a vtkMultiBlockDataSet, thus providing for a full
    tree structure. Sub-blocks are usually used to distribute blocks
    across processors. For example, a 1 block dataset can be distributed
    as following:
     proc 0:
     Block 0:
       * ds 0
       * (null)
    
     proc 1:
     Block 0:
       * (null)
       * ds 1
    """
    def GetBlock(self, p_int):
        """
        V.GetBlock(int) -> vtkDataObject
        C++: vtkDataObject *GetBlock(unsigned int blockno)
        
        Returns the block at the given index. It is recommended that one
        uses the iterators to iterate over composite datasets rather than
        using this API.
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkMultiBlockDataSet
        C++: static vtkMultiBlockDataSet *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkMultiBlockDataSet
        C++: static vtkMultiBlockDataSet *GetData(vtkInformationVector *v,
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
    
    def GetMetaData(self, p_int):
        """
        V.GetMetaData(int) -> vtkInformation
        C++: vtkInformation *GetMetaData(unsigned int blockno)
        V.GetMetaData(vtkCompositeDataIterator) -> vtkInformation
        C++: vtkInformation *GetMetaData(vtkCompositeDataIterator *iter)
            override;
        
        Returns the meta-data for the block. If none is already present,
        a new vtkInformation object will be allocated. Use HasMetaData to
        avoid allocating vtkInformation objects.
        """
        ...
    
    def GetNumberOfBlocks(self):
        """
        V.GetNumberOfBlocks() -> int
        C++: unsigned int GetNumberOfBlocks()
        
        Returns the number of blocks.
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
    
    def HasMetaData(self, p_int):
        """
        V.HasMetaData(int) -> int
        C++: int HasMetaData(unsigned int blockno)
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
        V.NewInstance() -> vtkMultiBlockDataSet
        C++: vtkMultiBlockDataSet *NewInstance()
        """
        ...
    
    def RemoveBlock(self, p_int):
        """
        V.RemoveBlock(int)
        C++: void RemoveBlock(unsigned int blockno)
        
        Remove the given block from the dataset.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMultiBlockDataSet
        C++: static vtkMultiBlockDataSet *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBlock(self, p_int, vtkDataObject):
        """
        V.SetBlock(int, vtkDataObject)
        C++: void SetBlock(unsigned int blockno, vtkDataObject *block)
        
        Sets the data object as the given block. The total number of
        blocks will be resized to fit the requested block no.
        """
        ...
    
    def SetNumberOfBlocks(self, p_int):
        """
        V.SetNumberOfBlocks(int)
        C++: void SetNumberOfBlocks(unsigned int numBlocks)
        
        Set the number of blocks. This will cause allocation if the new
        number of blocks is greater than the current size. All new blocks
        are initialized to null.
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


