"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkWordCloud(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkWordCloud - generate a word cloud visualization of a text document
    
    Superclass: vtkImageAlgorithm
    
    Word Clouds, AKA Tag Clouds
    (https://en.wikipedia.org/wiki/Tag_cloud), are a text visualization
    technique that displays individual words with properties that depend
    on the frequency of a word in a document. vtkWordCloud varies the
    font size based on word frequency. Word Clouds are useful for quickly
    perceiving the most prominent terms in a document. Also, Word Clouds
    can identify trends and patterns that would otherwise be unclear or
    difficult to see in a tabular format. Frequently used keywords stand
    out better in a word cloud. Common words that might be overlooked in
    tabular form are highlighted in the larger text, making them pop out
    when displayed in a word cloud.
    
    There is some controversy about the usefulness of word clouds. Their
    best use may be for presentations, see https://tinyurl.com/y59hy7oa
    
    The generation of the word cloud proceeds as follows:
    1. Read the text file
    2. Split text into words to be processed Extract words from the text
       Drop the case of each word for filtering Filter the words Replace
       words from the ReplacementPairs list Skip the word if it is in the
    stop list or contains a digit Skip single character words Raise the
       case of the first letter in each word Sort the word list by
       frequency
    3. Create a rectangular mask image or read a mask image
    4. For each word Render the word into an image Try to add the word to
    the word cloud image. For each orientation, see if the word "fits" If
    no fit, move along a path to try another location
    
    NOTE: A word fits if all of the non-zero word cloud pixels in the
    extent of the text image are background pixels.
    
    NOTE: The path is an Archimedean Spiral
    (https://en.wikipedia.org/wiki/Archimedean_spiral)
    
    * NOTE: vtkWordCloud has a built-in list of stop word. Stop words are
    * words that are filtered out before processing of the text, such as
    * the, is, at, which, and so on.
    *
    * NOTE: Color names are defined in vtkNamedColors. A visual
    * representation of color names is here: https://tinyurl.com/y3yxcxj6
    *
    * NOTE: vtkWordCloud offers Several methods to customize the
      resulting
    * visualization. The class provides defaults that provide a
      reasonable
    * result.
    *
    * BackgroundColorName - The vtkNamedColors name for the background
    * (MidNightBlue). See https://tinyurl.com/y3yxcxj6 for a visual
    * representation of the named colors.
    *
    * ColorDistribution - Distribution of random colors(.6 1.0), if
    * WordColorName is empty.
    *
    * ColorSchemeName - Name of a color scheme from vtkColorSeries to be
    * used to select colors for the words (), if WordColorName is empty.
    * See https://tinyurl.com/y3j6c27o for a visual representation of the
    * color schemes.
    *
    * DPI - Dots per inch(200) of the rendered text. DPI is used as a
    * scaling mechanism for the words. As DPI increases, the word size
    * increases. If there are too, few skipped words, increase this
      value,
    * too many, decrease it.
    *
    * FontFileName - If empty, the built-in Arial font is used(). The
    * FontFileName is the name of a file that contains a TrueType font.
    * https://www.1001freefonts.com/ is a good source for free TrueType
    * fonts.
    *
    * FontMultiplier - Font multiplier(6). The final FontSize is this
      value
    * times the word frequency.
    *
    * Gap - Space gap of words (2). The gap is the number of spaces added
    to
    * the beginning and end of each word.
    *
    * MaskColorName - Name of the color for the mask (black). This is the
    * name of the vtknamedColors that defines the foreground of the
    * mask. Usually black or white.  See https://tinyurl.com/y3yxcxj6 for
    * a visual representation of the named colors.
    *
    * MaskFileName - Mask file name(). If a mask file is specified, it
      will be
    * used as the mask. Otherwise, a black square is used as the mask.
      The
    * mask file should contain three channels of unsigned char values. If
    * the mask file is just a single unsigned char, specify turn the
      boolean
    * BWMask on.  If BWmask is on, the class will create a three channel
    * image using vtkImageAppendComponents.
    *
    * BWMask - Mask image has a single channel(false). Mask images
      typically
    * have three channels (r,g,b).
    *
    * MaxFontSize - Maximum font size(48).
    *
    * MinFontSize - Minimum font size(8).
    *
    * MinFrequency - Minimum word frequency accepted(2). Word with
    * frequencies less than this will be ignored.
    *
    * OffsetDistribution - Range of uniform random offsets(-size[0]/100.0
    * -size{1]/100.0)(-20 20). These offsets are offsets from the
      generated
    * path for word layout.
    *
    * OrientationDistribution - Ranges of random orientations(-20 20). If
    * discrete orientations are not defined, these orientations will be
    * generated.
    *
    * Orientations - Vector of discrete orientations(). If non-empty,
    * these will be used instead of the orientations distribution");
    *
    * ReplacementPairs - Replace the first word with another second word
    * ().  The each word will also added to the StopList. The second
    * argument can contain multiple words. For example you could replace
    * "bill" with "Bill Lorensen" or, "vtk" with "VTK . Remember that
    * words are always stored internally with lower case, even though the
    * first letter is capitalized in the Word Cloud.
    *
    * Sizes - Size of image(640 480).
    *
    * StopWords - User provided stop words(). Stop words are words that
    * are filtered out before processing of the text, such as the, is,
    * at, which, and so on.  vtkWordClass has built-in stop words. The
    * user-provided stop words are added to the built-in list. See
    * https://en.wikipedia.org/wiki/Stop_words for a description.  The
    * built-in stop words were derived from the english stop words at
    * https://www.ranks.nl/stopwords. Stop words for other languages are
    * also available.
    *
    * StopListFileName - the name of a file that contains stop words,
    * one word per line (). If present, the stop words in the file
    * replace the built-in stop list.
    *
    * Title - Add this word to the document's words and set a high
    * frequency, so that is will be rendered first.
    *
    * WordColorName - Name of the color for the words(). The name is
    * selected from vtkNamedColors. If the name is empty, the
    * ColorDistribution will generate random colors.  See
    * https://tinyurl.com/y3yxcxj6 for a visual representation of the
    * named colors.
    *
    * The class also provided Get methods that return vectors
    * StopWords, SkippedWords and KeptWords.
    """
    def AddOrientation(self, p_float):
        """
        V.AddOrientation(float)
        C++: void AddOrientation(double arg)
        """
        ...
    
    def AddStopWord(self, string):
        """
        V.AddStopWord(string)
        C++: void AddStopWord(std::string word)
        """
        ...
    
    def ClearStopWords(self):
        """
        V.ClearStopWords()
        C++: void ClearStopWords()
        """
        ...
    
    def GetBackgroundColorName(self):
        """
        V.GetBackgroundColorName() -> string
        C++: virtual std::string GetBackgroundColorName()
        """
        ...
    
    def GetBWMask(self):
        """
        V.GetBWMask() -> bool
        C++: virtual bool GetBWMask()
        """
        ...
    
    def GetColorSchemeName(self):
        """
        V.GetColorSchemeName() -> string
        C++: virtual std::string GetColorSchemeName()
        """
        ...
    
    def GetDPI(self):
        """
        V.GetDPI() -> int
        C++: virtual int GetDPI()
        """
        ...
    
    def GetFileName(self):
        """
        V.GetFileName() -> string
        C++: virtual std::string GetFileName()
        """
        ...
    
    def GetFontFileName(self):
        """
        V.GetFontFileName() -> string
        C++: virtual std::string GetFontFileName()
        """
        ...
    
    def GetFontMultiplier(self):
        """
        V.GetFontMultiplier() -> int
        C++: virtual int GetFontMultiplier()
        """
        ...
    
    def GetGap(self):
        """
        V.GetGap() -> int
        C++: virtual int GetGap()
        """
        ...
    
    def GetKeptWords(self):
        """
        V.GetKeptWords() -> Stvector_ISt6stringE
        C++: virtual std::vector<std::string> &GetKeptWords()
        """
        ...
    
    def GetMaskColorName(self):
        """
        V.GetMaskColorName() -> string
        C++: virtual std::string GetMaskColorName()
        """
        ...
    
    def GetMaskFileName(self):
        """
        V.GetMaskFileName() -> string
        C++: virtual std::string GetMaskFileName()
        """
        ...
    
    def GetMaxFontSize(self):
        """
        V.GetMaxFontSize() -> int
        C++: virtual int GetMaxFontSize()
        """
        ...
    
    def GetMinFontSize(self):
        """
        V.GetMinFontSize() -> int
        C++: virtual int GetMinFontSize()
        """
        ...
    
    def GetMinFrequency(self):
        """
        V.GetMinFrequency() -> int
        C++: virtual int GetMinFrequency()
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
    
    def GetOrientations(self):
        """
        V.GetOrientations() -> Stvector_IdE
        C++: virtual OrientationsContainer GetOrientations()
        """
        ...
    
    def GetSkippedWords(self):
        """
        V.GetSkippedWords() -> Stvector_ISt6stringE
        C++: virtual std::vector<std::string> &GetSkippedWords()
        """
        ...
    
    def GetStopListFileName(self):
        """
        V.GetStopListFileName() -> string
        C++: virtual std::string GetStopListFileName()
        """
        ...
    
    def GetStoppedWords(self):
        """
        V.GetStoppedWords() -> Stvector_ISt6stringE
        C++: virtual std::vector<std::string> &GetStoppedWords()
        """
        ...
    
    def GetTitle(self):
        """
        V.GetTitle() -> string
        C++: virtual std::string GetTitle()
        """
        ...
    
    def GetWordColorName(self):
        """
        V.GetWordColorName() -> string
        C++: virtual std::string GetWordColorName()
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
        V.NewInstance() -> vtkWordCloud
        C++: vtkWordCloud *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkWordCloud
        C++: static vtkWordCloud *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBackgroundColorName(self, string):
        """
        V.SetBackgroundColorName(string)
        C++: virtual void SetBackgroundColorName(std::string arg)
        """
        ...
    
    def SetBWMask(self, bool):
        """
        V.SetBWMask(bool)
        C++: virtual void SetBWMask(bool arg)
        """
        ...
    
    def SetColorSchemeName(self, string):
        """
        V.SetColorSchemeName(string)
        C++: virtual void SetColorSchemeName(std::string arg)
        """
        ...
    
    def SetDPI(self, p_int):
        """
        V.SetDPI(int)
        C++: virtual void SetDPI(int _arg)
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: virtual void SetFileName(std::string arg)
        """
        ...
    
    def SetFontFileName(self, string):
        """
        V.SetFontFileName(string)
        C++: virtual void SetFontFileName(std::string arg)
        """
        ...
    
    def SetFontMultiplier(self, p_int):
        """
        V.SetFontMultiplier(int)
        C++: virtual void SetFontMultiplier(int _arg)
        """
        ...
    
    def SetGap(self, p_int):
        """
        V.SetGap(int)
        C++: virtual void SetGap(int _arg)
        """
        ...
    
    def SetMaskColorName(self, string):
        """
        V.SetMaskColorName(string)
        C++: virtual void SetMaskColorName(std::string arg)
        """
        ...
    
    def SetMaskFileName(self, string):
        """
        V.SetMaskFileName(string)
        C++: virtual void SetMaskFileName(std::string arg)
        """
        ...
    
    def SetMaxFontSize(self, p_int):
        """
        V.SetMaxFontSize(int)
        C++: virtual void SetMaxFontSize(int _arg)
        """
        ...
    
    def SetMinFontSize(self, p_int):
        """
        V.SetMinFontSize(int)
        C++: virtual void SetMinFontSize(int _arg)
        """
        ...
    
    def SetMinFrequency(self, p_int):
        """
        V.SetMinFrequency(int)
        C++: virtual void SetMinFrequency(int _arg)
        """
        ...
    
    def SetOrientations(self, Stvector_IdE):
        """
        V.SetOrientations(Stvector_IdE)
        C++: virtual void SetOrientations(OrientationsContainer arg)
        """
        ...
    
    def SetStopListFileName(self, string):
        """
        V.SetStopListFileName(string)
        C++: virtual void SetStopListFileName(std::string arg)
        """
        ...
    
    def SetTitle(self, string):
        """
        V.SetTitle(string)
        C++: virtual void SetTitle(std::string arg)
        """
        ...
    
    def SetWordColorName(self, string):
        """
        V.SetWordColorName(string)
        C++: virtual void SetWordColorName(std::string arg)
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


