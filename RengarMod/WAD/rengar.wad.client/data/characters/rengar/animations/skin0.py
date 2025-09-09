#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Animations/Skin0" = animationGraphData {
        mUseCascadeBlend: bool = false
        mClipDataMap: map[hash,pointer] = {
            "Channel" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Channel_WNDPUP.anm"
                }
            }
            "Crit" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "Crit" = ParticleEventData {
                        mName: hash = "Crit"
                        mStartFrame: f32 = 10
                        mEffectKey: hash = "Rengar_C_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_crit.anm"
                }
            }
            "Dance" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xbc45bbc5 = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Dance3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Dance.anm"
                }
            }
            "death" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Death3D_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_death.anm"
                }
            }
            "Idle1" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle1_Base"
                        mProbability: f32 = 75
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle2_Base"
                        mProbability: f32 = 25
                    }
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x0cf0606b = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Laugh3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Laugh.anm"
                }
            }
            "Run" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = IsInGrassDynamicMaterialBoolDriver {}
                }
                mChangeAnimationMidPlay: bool = true
                SyncFrameOnChangeAnim: bool = true
                mTrueConditionClipName: hash = "Run_Core"
                mFalseConditionClipName: hash = "Run_DisableInvis"
            }
            "Run_core" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                #mMaskDataName: hash = "UpperBody"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_run1.anm"
                }
            }
            "Run_DisableInvis" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                #mMaskDataName: hash = "UpperBody"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                    "R_leapOverride" = ParticleEventData {
                        mName: hash = "Rengar_RLeap_Override"
                        mStartFrame: f32 = 0
                        mEffectKey: hash = "Rengar_RLeap_Override"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = true
                        mIsKillEvent: bool = true
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_run1.anm"
                }
            }
            "Run2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = HasBuffDynamicMaterialBoolDriver {
                        mScriptName: string = "RengarPassiveBuff"
                    }
                }
                mChangeAnimationMidPlay: bool = true
                DontStompTransitionClip: bool = true
                SyncFrameOnChangeAnim: bool = true
                mTrueConditionClipName: hash = "Run2_Core"
                mFalseConditionClipName: hash = "Run1Fast_core"
            }
            "Run2_Core" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_run2.anm"
                }
            }
            "Spell1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Q" = ParticleEventData {
                        mName: hash = "Q"
                        mStartFrame: f32 = 4
                        mEffectKey: hash = "Rengar_Q_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1.anm"
                }
            }
            "Spell2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                        mAnimationNames: list[hash] = {
                            "Spell5_core"
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = true
                mDontStompTransitionClip: bool = true
                SyncFrameOnChangeAnim: bool = true
                mPlayAnimChangeFromBeginning: bool = true
                mTrueConditionClipName: hash = "Spell2_core"
                mFalseConditionClipName: hash = "Spell2_core"
            }
            "Spell2_core" =  AtomicClipData {
                mTrackDataName: hash = "Spell"
                mMaskDataName: hash = "UpperBody"
                mTickDuration: f32 = 0.0333333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell2.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
            }
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell3.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_death.anm"
                }
            }
            "Spell4_Loop" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Spell4_Winddown" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_death.anm"
                }
            }
            #----- Normal Walk Spell 5
            "spell5" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell5_core"
                    "Spell5_below"
                }
            }      
            "Spell5_core" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mMaskDataName: hash = "UpperBody_ForDash"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    # "StopIdle" = StopAnimationEventData {
                        # #mEndFrame: f32 = 20
                        # mStopAnimationName: hash = "idle1"
                    # }
                    # "StopRun2" = StopAnimationEventData {
                        # mEndFrame: f32 = 20
                        # mStopAnimationName: hash = "run1"
                    # }
                    # "StopRun" = StopAnimationEventData {
                        # mEndFrame: f32 = 20
                        # mStopAnimationName: hash = "run"
                    # }
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "spell3"
                    }
                    "StopLegs" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell5_below"
                        mStartFrame: f32 = 40
                    }
                    "R_leapOverride" = ParticleEventData {
                        mName: hash = "Rengar_RLeap_Override"
                        mStartFrame: f32 = 0
                        mEffectKey: hash = "Rengar_RLeap_Override"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = true
                        mIsKillEvent: bool = true
                    }
                    # "FadeTime" = FadeEventData {
                    # mStartFrame: f32 = 10
                    # mFireIfAnimationEndsEarly: bool = true
                    # mTimeToFade: f32 = 0.001
                    # mTargetAlpha: f32 = 1
                    # }
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = LogicDriverFloatParametricUpdater {
                                Driver: pointer = DistanceToPlayerMaterialFloatDriver {
                                    MinDistance: f32 = 0
                                    MaxDistance: f32 = 750
                                }
                            }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mIncrement: f32 = 2.4
                                }
                            }
                        }
                    }
                }
            }
            "Spell5_below" = AtomicClipData {
                mTrackDataName: hash = "Actions_below"
                mMaskDataName: hash = "Legs"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = LogicDriverFloatParametricUpdater {
                                Driver: pointer = DistanceToPlayerMaterialFloatDriver {
                                    MinDistance: f32 = 0
                                    MaxDistance: f32 = 750
                                }
                            }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mIncrement: f32 = 2.4
                                }
                            }
                        }
                    }
                }
            }
            #-----------
            "Spell6" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mTickDuration: f32 = 0.0167
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Taunt.anm"
                }
            }
            0x602b063d = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_recall.anm"
                }
            }
            0x6208af50 = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_recall_idle.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    0xb5b7e047 = ParticleEventData {
                        mName: hash = 0xb5b7e047
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA1_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack1.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                #mMaskDataName: hash = "UpperBody"
                mEventDataMap: map[hash,pointer] = {
                    0xb6b7e1da = ParticleEventData {
                        mName: hash = 0xb6b7e1da
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA2_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack2.anm"
                }
            }
            "Attack3" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    0xb7b7e36d = ParticleEventData {
                        mName: hash = 0xb7b7e36d
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA3_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack3.anm"
                }
            }
            "Recall" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    0x602b063d
                    0x6208af50
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Joke3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Joke.anm"
                }
            }
            
            "Run1_Fast" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = IsInGrassDynamicMaterialBoolDriver {}
                }
                mChangeAnimationMidPlay: bool = true
                SyncFrameOnChangeAnim: bool = true
                mTrueConditionClipName: hash = "Run1Fast_core"
                mFalseConditionClipName: hash = "Run1Fast_DisableInvis"
            }
            "Run1Fast_DisableInvis" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                            mMaskDataName: hash = 0x26a07077
                            mBlendInTime: f32 = 0.1
                            mBlendOutTime: f32 = 0.2
                        }
                    "R_leapOverride" = ParticleEventData {
                        mName: hash = "Rengar_RLeap_Override"
                        mStartFrame: f32 = 0
                        mEffectKey: hash = "Rengar_RLeap_Override"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = true
                        mIsKillEvent: bool = true
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_run1_Fast.anm"
                }   
            }
            "Run1Fast_core" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                            mMaskDataName: hash = 0x26a07077
                            mBlendInTime: f32 = 0.1
                            mBlendOutTime: f32 = 0.2
                        }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_run1_Fast.anm"
                }   
            }
            
            "Attack4" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "spell5"
                                }
                            }
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = false
                mTrueConditionClipName: hash = "Attack4_jump"
                mFalseConditionClipName: hash = "Attack4_land"
            }
            
            #----- Normal Q 
            "Attack4_land" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAttackingBoolDriver {}
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
                            }
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "A4_Emp"
                mFalseConditionClipName: hash = "A4_Normal"
            }
            "A4_Normal" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mTickDuration: f32 = 0.034
                mEventDataMap: map[hash,pointer] = {
                    "Normal" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas"
                        mStartFrame: f32 = 7
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack4_long.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = AttackSpeedParametricUpdater { }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mMultiplier: f32 = 0.95
                                }
                            }
                        }
                    }
                }
            }
            "A4_Emp" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "Emp" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas_Max_MyWay"
                        mStartFrame: f32 = 7
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack4_long.anm"
                }
            }
            
            #----- Jump Q 
            "Attack4_jump" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
                            }
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = false
                mTrueConditionClipName: hash = "A4_Emp_jump"
                mFalseConditionClipName: hash = "A4_Normal_jump"
            }
            "A4_Normal_jump" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                #mMaskDataName: hash = "RootExcludedMask"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_jump.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = AttackSpeedParametricUpdater { }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mMultiplier: f32 = 0.95
                                }
                            }
                        }
                    }
                }
                mEventDataMap: map[hash,pointer] = {
                    "Norm" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas_Max_MyWay"
                        mStartFrame: f32 = 15
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "R_leapOverride" = ParticleEventData {
                        mName: hash = "Rengar_RLeap_Override"
                        mStartFrame: f32 = 0
                        mEffectKey: hash = "Rengar_RLeap_Override"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = true
                        mIsKillEvent: bool = true
                    }
                }
            }
            "A4_Emp_jump" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                #mMaskDataName: hash = "RootExcludedMask"
                mEventDataMap: map[hash,pointer] = {
                    "Emp" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas_Max_MyWay"
                        mStartFrame: f32 = 1
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "R_leapOverride" = ParticleEventData {
                        mName: hash = "Rengar_RLeap_Override"
                        mStartFrame: f32 = 0
                        mEffectKey: hash = "Rengar_RLeap_Override"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = true
                        mIsKillEvent: bool = true
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_jump.anm"
                }
            }
            
            "Idle1_Base" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            0x0fb24234 = AtomicClipData {
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "HoodOnTrack"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_hood_on.anm"
                }
            }
            0x713ed5b5 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_TRA.anm"
                }
            }
            "Spell1_Run2_TRA" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_run2_TRA.anm"
                }
            }
            "Spell1_Run_TRA" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_run_TRA.anm"
                }
            }
            "Spell2_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell2.anm"
                }
            }
            "Spell4_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "empty" = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x26a07077 = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0.25
                    0.6
                    0.75
                    0.85
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0xef7cfc3b = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "UpperBody_ForDash" = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1 # Ground
                    1
                    0
                    0
                    1
                    1
                    1
                    0
                    1
                    1
                    0
                }
            }
            "UpperBody" = MaskData {
                mWeightList: list[f32] = {
                    0.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    1.000000
                    1.000000
                    1.000000
                    1.000000
                    0.000000
                    0.000000
                    0.000000
                    1.000000
                    1.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    0.000000
                    1.000000
                    1.000000
                    1.000000
                    0.000000
                    1.000000
                    1.000000
                    0.000000

                }
            }
            "Legs" = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0 # Weapon
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    0
                }
            }
            "RootExcludedMask" = MaskData {
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "W_Exp" = MaskData {
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    0
                    0
                    1
                    1
                    1
                    0
                    1
                    1
                    0
                }
            }

        }
        mTrackDataMap: map[hash,embed] = {
            "Channel" = TrackData {
                mPriority: u8 = 0
            }
            "Default" = TrackData {
                mPriority: u8 = 4
            }
            "Actions" = TrackData { 
                mPriority: u8 = 1
            }
            "Spell" = TrackData { 
                mPriority: u8 = 3
            }
            "Actions_below" = TrackData { 
                mPriority: u8 = 2
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            7794375146876298347 = TimeBlendData {
            mTime: f32 = 0
            }
            16132709914726491243 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883337026950592 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13156647003641632192 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3405941502114026944 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13039675252962252224 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13111734577872000448 = TimeBlendData {
            mTime: f32 = 0.2
            }
            8175344642410436032 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13183793902781748672 = TimeBlendData {
            mTime: f32 = 0.2
            }
            10832289107674420672 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13987674968704701888 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11230245603202323904 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6391149149580187072 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6463208474489935296 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6247030499760690624 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6030852525031445952 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6427569501587658176 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3084207950102025664 = TimeBlendData {
            mTime: f32 = 0.2
            }
            7064088774455875008 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6929639311495419328 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11302304928112072128 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11374364253021820352 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13255853227691496896 = TimeBlendData {
            mTime: f32 = 0.2
            }
            12217611125164103104 = TimeBlendData {
            mTime: f32 = 0.2
            }
            5406481391066305984 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13399971877510993344 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13630352411439945152 = TimeBlendData {
            mTime: f32 = 0.2
            }
            17876238947190068672 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11831733632450713024 = TimeBlendData {
            mTime: f32 = 0.2
            }
            2432597613854610880 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13590883339297213630 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13156647005911895230 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3405941504384289982 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13039675255232515262 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13111734580142263486 = TimeBlendData {
            mTime: f32 = 0.2
            }
            8175344644680699070 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13183793905052011710 = TimeBlendData {
            mTime: f32 = 0.2
            }
            10832289109944683710 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13987674970974964926 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11230245605472586942 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6391149151850450110 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6463208476760198334 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6247030502030953662 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6030852527301708990 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6427569503857921214 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3084207952372288702 = TimeBlendData {
            mTime: f32 = 0.2
            }
            7064088776726138046 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6929639313765682366 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11302304930382335166 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11374364255292083390 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13255853229961759934 = TimeBlendData {
            mTime: f32 = 0.2
            }
            12217611127434366142 = TimeBlendData {
            mTime: f32 = 0.2
            }
            5406481393336569022 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13399971879781256382 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13630352413710208190 = TimeBlendData {
            mTime: f32 = 0.2
            }
            17876238949460331710 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11831733634720976062 = TimeBlendData {
            mTime: f32 = 0.2
            }
            2432597616124873918 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13590883339398317155 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13156647006012998755 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3405941504485393507 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13039675255333618787 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13111734580243367011 = TimeBlendData {
            mTime: f32 = 0.2
            }
            8175344644781802595 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13183793905153115235 = TimeBlendData {
            mTime: f32 = 0.2
            }
            10832289110045787235 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13987674971076068451 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11230245605573690467 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6391149151951553635 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6463208476861301859 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6247030502132057187 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6030852527402812515 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6427569503959024739 = TimeBlendData {
            mTime: f32 = 0.2
            }
            3084207952473392227 = TimeBlendData {
            mTime: f32 = 0.2
            }
            7064088776827241571 = TimeBlendData {
            mTime: f32 = 0.2
            }
            6929639313866785891 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11302304930483438691 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11374364255393186915 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13255853230062863459 = TimeBlendData {
            mTime: f32 = 0.2
            }
            12217611127535469667 = TimeBlendData {
            mTime: f32 = 0.2
            }
            5406481393437672547 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13399971879882359907 = TimeBlendData {
            mTime: f32 = 0.2
            }
            13630352413811311715 = TimeBlendData {
            mTime: f32 = 0.2
            }
            17876238949561435235 = TimeBlendData {
            mTime: f32 = 0.2
            }
            11831733634822079587 = TimeBlendData {
            mTime: f32 = 0.2
            }
            2432597616225977443 = TimeBlendData {
            mTime: f32 = 0.2
            }
            2432597615709903878 = TimeBlendData {
            mTime: f32 = 0
            }
            2432597616147972167 = TimeBlendData {
            mTime: f32 = 0
            }
            2432597615906237590 = TimeBlendData {
            mTime: f32 = 0
            }
            2432597614320397870 = TimeBlendData {
            mTime: f32 = 0
            }
            2432597616181527405 = TimeBlendData {
            mTime: f32 = 0
            }
            11831733634306006022 = TimeBlendData {
            mTime: f32 = 0
            }
            11831733634744074311 = TimeBlendData {
            mTime: f32 = 0
            }
            11831733634502339734 = TimeBlendData {
            mTime: f32 = 0
            }
            11831733632916500014 = TimeBlendData {
            mTime: f32 = 0
            }
            11831733634777629549 = TimeBlendData {
            mTime: f32 = 0
            }
            17876238949045361670 = TimeBlendData {
            mTime: f32 = 0
            }
            17876238949483429959 = TimeBlendData {
            mTime: f32 = 0
            }
            17876238949241695382 = TimeBlendData {
            mTime: f32 = 0
            }
            17876238947655855662 = TimeBlendData {
            mTime: f32 = 0
            }
            17876238949516985197 = TimeBlendData {
            mTime: f32 = 0
            }
            13630352413295238150 = TimeBlendData {
            mTime: f32 = 0
            }
            13630352413733306439 = TimeBlendData {
            mTime: f32 = 0
            }
            13630352413491571862 = TimeBlendData {
            mTime: f32 = 0
            }
            13630352411905732142 = TimeBlendData {
            mTime: f32 = 0
            }
            13630352413766861677 = TimeBlendData {
            mTime: f32 = 0
            }
            11374364254877113350 = TimeBlendData {
            mTime: f32 = 0
            }
            11374364255315181639 = TimeBlendData {
            mTime: f32 = 0
            }
            11374364255073447062 = TimeBlendData {
            mTime: f32 = 0
            }
            11374364253487607342 = TimeBlendData {
            mTime: f32 = 0
            }
            11374364255348736877 = TimeBlendData {
            mTime: f32 = 0
            }
            11302304929967365126 = TimeBlendData {
            mTime: f32 = 0
            }
            11302304930405433415 = TimeBlendData {
            mTime: f32 = 0
            }
            11302304930163698838 = TimeBlendData {
            mTime: f32 = 0
            }
            11302304928577859118 = TimeBlendData {
            mTime: f32 = 0
            }
            11302304930438988653 = TimeBlendData {
            mTime: f32 = 0
            }
            6929639313350712326 = TimeBlendData {
            mTime: f32 = 0
            }
            6929639313788780615 = TimeBlendData {
            mTime: f32 = 0
            }
            6929639313547046038 = TimeBlendData {
            mTime: f32 = 0
            }
            6929639311961206318 = TimeBlendData {
            mTime: f32 = 0
            }
            6929639313822335853 = TimeBlendData {
            mTime: f32 = 0
            }
            7064088776311168006 = TimeBlendData {
            mTime: f32 = 0
            }
            7064088776749236295 = TimeBlendData {
            mTime: f32 = 0
            }
            7064088776507501718 = TimeBlendData {
            mTime: f32 = 0
            }
            7064088774921661998 = TimeBlendData {
            mTime: f32 = 0
            }
            7064088776782791533 = TimeBlendData {
            mTime: f32 = 0
            }
            3084207951957318662 = TimeBlendData {
            mTime: f32 = 0
            }
            3084207952395386951 = TimeBlendData {
            mTime: f32 = 0
            }
            3084207952153652374 = TimeBlendData {
            mTime: f32 = 0
            }
            3084207950567812654 = TimeBlendData {
            mTime: f32 = 0
            }
            3084207952428942189 = TimeBlendData {
            mTime: f32 = 0
            }
            6427569503442951174 = TimeBlendData {
            mTime: f32 = 0
            }
            6427569503881019463 = TimeBlendData {
            mTime: f32 = 0
            }
            6427569503639284886 = TimeBlendData {
            mTime: f32 = 0
            }
            6427569502053445166 = TimeBlendData {
            mTime: f32 = 0
            }
            6427569503914574701 = TimeBlendData {
            mTime: f32 = 0
            }
            6030852526886738950 = TimeBlendData {
            mTime: f32 = 0
            }
            6030852527324807239 = TimeBlendData {
            mTime: f32 = 0
            }
            6030852527083072662 = TimeBlendData {
            mTime: f32 = 0
            }
            6030852525497232942 = TimeBlendData {
            mTime: f32 = 0
            }
            6030852527358362477 = TimeBlendData {
            mTime: f32 = 0
            }
            6247030501615983622 = TimeBlendData {
            mTime: f32 = 0
            }
            6247030502054051911 = TimeBlendData {
            mTime: f32 = 0
            }
            6247030501812317334 = TimeBlendData {
            mTime: f32 = 0
            }
            6247030500226477614 = TimeBlendData {
            mTime: f32 = 0
            }
            6247030502087607149 = TimeBlendData {
            mTime: f32 = 0
            }
            6463208476345228294 = TimeBlendData {
            mTime: f32 = 0
            }
            6463208476783296583 = TimeBlendData {
            mTime: f32 = 0
            }
            6463208476541562006 = TimeBlendData {
            mTime: f32 = 0
            }
            6463208474955722286 = TimeBlendData {
            mTime: f32 = 0
            }
            6463208476816851821 = TimeBlendData {
            mTime: f32 = 0
            }
            6391149151435480070 = TimeBlendData {
            mTime: f32 = 0
            }
            6391149151873548359 = TimeBlendData {
            mTime: f32 = 0
            }
            6391149151631813782 = TimeBlendData {
            mTime: f32 = 0
            }
            6391149150045974062 = TimeBlendData {
            mTime: f32 = 0
            }
            6391149151907103597 = TimeBlendData {
            mTime: f32 = 0
            }
            11230245605057616902 = TimeBlendData {
            mTime: f32 = 0
            }
            11230245605495685191 = TimeBlendData {
            mTime: f32 = 0
            }
            11230245605253950614 = TimeBlendData {
            mTime: f32 = 0
            }
            11230245603668110894 = TimeBlendData {
            mTime: f32 = 0
            }
            11230245605529240429 = TimeBlendData {
            mTime: f32 = 0
            }
            13987674970559994886 = TimeBlendData {
            mTime: f32 = 0
            }
            13987674970998063175 = TimeBlendData {
            mTime: f32 = 0
            }
            13987674970756328598 = TimeBlendData {
            mTime: f32 = 0
            }
            13987674969170488878 = TimeBlendData {
            mTime: f32 = 0
            }
            13987674971031618413 = TimeBlendData {
            mTime: f32 = 0
            }
            10832289109529713670 = TimeBlendData {
            mTime: f32 = 0
            }
            10832289109967781959 = TimeBlendData {
            mTime: f32 = 0
            }
            10832289109726047382 = TimeBlendData {
            mTime: f32 = 0
            }
            10832289108140207662 = TimeBlendData {
            mTime: f32 = 0
            }
            10832289110001337197 = TimeBlendData {
            mTime: f32 = 0
            }
            13183793904637041670 = TimeBlendData {
            mTime: f32 = 0
            }
            13183793905075109959 = TimeBlendData {
            mTime: f32 = 0
            }
            13183793904833375382 = TimeBlendData {
            mTime: f32 = 0
            }
            13183793903247535662 = TimeBlendData {
            mTime: f32 = 0
            }
            13183793905108665197 = TimeBlendData {
            mTime: f32 = 0
            }
            8175344644265729030 = TimeBlendData {
            mTime: f32 = 0
            }
            8175344644703797319 = TimeBlendData {
            mTime: f32 = 0
            }
            8175344644462062742 = TimeBlendData {
            mTime: f32 = 0
            }
            8175344642876223022 = TimeBlendData {
            mTime: f32 = 0
            }
            8175344644737352557 = TimeBlendData {
            mTime: f32 = 0
            }
            13111734579727293446 = TimeBlendData {
            mTime: f32 = 0
            }
            13111734580165361735 = TimeBlendData {
            mTime: f32 = 0
            }
            13111734579923627158 = TimeBlendData {
            mTime: f32 = 0
            }
            13111734578337787438 = TimeBlendData {
            mTime: f32 = 0
            }
            13111734580198916973 = TimeBlendData {
            mTime: f32 = 0
            }
            13039675254817545222 = TimeBlendData {
            mTime: f32 = 0
            }
            13039675255255613511 = TimeBlendData {
            mTime: f32 = 0
            }
            13039675255013878934 = TimeBlendData {
            mTime: f32 = 0
            }
            13039675253428039214 = TimeBlendData {
            mTime: f32 = 0
            }
            13039675255289168749 = TimeBlendData {
            mTime: f32 = 0
            }
            3405941503969319942 = TimeBlendData {
            mTime: f32 = 0
            }
            3405941504407388231 = TimeBlendData {
            mTime: f32 = 0
            }
            3405941504165653654 = TimeBlendData {
            mTime: f32 = 0
            }
            3405941502579813934 = TimeBlendData {
            mTime: f32 = 0
            }
            3405941504440943469 = TimeBlendData {
            mTime: f32 = 0
            }
            13156647005496925190 = TimeBlendData {
            mTime: f32 = 0
            }
            13156647005934993479 = TimeBlendData {
            mTime: f32 = 0
            }
            13156647005693258902 = TimeBlendData {
            mTime: f32 = 0
            }
            13156647004107419182 = TimeBlendData {
            mTime: f32 = 0
            }
            13156647005968548717 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883338882243590 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883339320311879 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883339078577302 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883337492737582 = TimeBlendData {
            mTime: f32 = 0
            }
            13590883339353867117 = TimeBlendData {
            mTime: f32 = 0
            }
        }
    }
}
