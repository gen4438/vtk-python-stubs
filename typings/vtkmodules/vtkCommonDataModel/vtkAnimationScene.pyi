"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkAnimationScene(__vtkmodules_vtkCommonCore.vtkAnimationCue):
    """
    vtkAnimationScene - the animation scene manager.
    
    Superclass: vtkAnimationCue
    
    vtkAnimationCue and vtkAnimationScene provide the framework to
    support animations in VTK. vtkAnimationCue represents an entity that
    changes/ animates with time, while vtkAnimationScene represents scene
    or setup for the animation, which consists of individual cues or
    other scenes.
    
    A scene can be played in real time mode, or as a sequence of frames
    1/frame rate apart in time.
    @sa
    vtkAnimationCue
    """
    def AddCue(self, vtkAnimationCue):
        """
        V.AddCue(vtkAnimationCue)
        C++: void AddCue(vtkAnimationCue *cue)
        
        Add/Remove an AnimationCue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        ...
    
    def GetFrameRate(self):
        """
        V.GetFrameRate() -> float
        C++: virtual double GetFrameRate()
        
        Get/Set the frame rate (in frames per second). This parameter
        affects only in the Sequence mode. The time interval indicated to
        each cue on every tick is progressed by 1/frame-rate seconds.
        """
        ...
    
    def GetLoop(self):
        """
        V.GetLoop() -> int
        C++: virtual int GetLoop()
        
        Enable/Disable animation loop.
        """
        ...
    
    def GetNumberOfCues(self):
        """
        V.GetNumberOfCues() -> int
        C++: int GetNumberOfCues()
        
        Add/Remove an AnimationCue to/from the Scene. It's an error to
        add a cue twice to the Scene.
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
    
    def GetPlayMode(self):
        """
        V.GetPlayMode() -> int
        C++: virtual int GetPlayMode()
        
        Get/Set the PlayMode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the RealTime mode, time indicates the instance
        in time.
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
    
    def IsInPlay(self):
        """
        V.IsInPlay() -> int
        C++: int IsInPlay()
        
        Returns if the animation is being played.
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
        V.NewInstance() -> vtkAnimationScene
        C++: vtkAnimationScene *NewInstance()
        """
        ...
    
    def Play(self):
        """
        V.Play()
        C++: virtual void Play()
        
        Starts playing the animation scene. Fires a
        vtkCommand::StartEvent before play beings and
        vtkCommand::EndEvent after play ends.
        """
        ...
    
    def RemoveAllCues(self):
        """
        V.RemoveAllCues()
        C++: void RemoveAllCues()
        
        Add/Remove an AnimationCue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        ...
    
    def RemoveCue(self, vtkAnimationCue):
        """
        V.RemoveCue(vtkAnimationCue)
        C++: void RemoveCue(vtkAnimationCue *cue)
        
        Add/Remove an AnimationCue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAnimationScene
        C++: static vtkAnimationScene *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAnimationTime(self, p_float):
        """
        V.SetAnimationTime(float)
        C++: void SetAnimationTime(double time)
        
        Makes the state of the scene same as the given time.
        """
        ...
    
    def SetFrameRate(self, p_float):
        """
        V.SetFrameRate(float)
        C++: virtual void SetFrameRate(double _arg)
        
        Get/Set the frame rate (in frames per second). This parameter
        affects only in the Sequence mode. The time interval indicated to
        each cue on every tick is progressed by 1/frame-rate seconds.
        """
        ...
    
    def SetLoop(self, p_int):
        """
        V.SetLoop(int)
        C++: virtual void SetLoop(int _arg)
        
        Enable/Disable animation loop.
        """
        ...
    
    def SetModeToRealTime(self):
        """
        V.SetModeToRealTime()
        C++: void SetModeToRealTime()
        
        Get/Set the PlayMode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the RealTime mode, time indicates the instance
        in time.
        """
        ...
    
    def SetModeToSequence(self):
        """
        V.SetModeToSequence()
        C++: void SetModeToSequence()
        
        Get/Set the PlayMode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the RealTime mode, time indicates the instance
        in time.
        """
        ...
    
    def SetPlayMode(self, p_int):
        """
        V.SetPlayMode(int)
        C++: virtual void SetPlayMode(int _arg)
        
        Get/Set the PlayMode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the RealTime mode, time indicates the instance
        in time.
        """
        ...
    
    def SetTimeMode(self, p_int):
        """
        V.SetTimeMode(int)
        C++: void SetTimeMode(int mode) override;
        
        Overridden to allow change to Normalized mode only if none of the
        constituent cues is in Relative time mode.
        """
        ...
    
    def Stop(self):
        """
        V.Stop()
        C++: void Stop()
        
        Stops the animation scene that is running.
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
    PlayModes = ...
    PLAYMODE_REALTIME = ...
    PLAYMODE_SEQUENCE = ...
    __dict__ = ...
    __vtkname__ = ...

