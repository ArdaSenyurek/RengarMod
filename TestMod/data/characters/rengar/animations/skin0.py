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
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Channel_WNDPUP.anm"
                }
            }
            "Crit" = AtomicClipData {
                mTrackDataName: hash = "AA"
                mEventDataMap: map[hash,pointer] = {
                    "Crit" = ParticleEventData {
                        mName: hash = "Crit"
                        mStartFrame: f32 = 3
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
            "Run" = AtomicClipData {
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
            "Run2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = HasBuffDynamicMaterialBoolDriver {
                            mScriptName: string = "RengarPassiveBuff"
                        }
                }
                mChangeAnimationMidPlay: bool = true
                DontStompTransitionClip: bool = true
                mTrueConditionClipName: hash = "Run2_Core"
                mFalseConditionClipName: hash = "Run1_Fast"
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
            "Spell2_xd" = ConditionBoolClipData {
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
            "Spell2" =  AtomicClipData {
                mTrackDataName: hash = "Spell2"
                mMaskDataName: hash = "UpperBody"
                mTickDuration: f32 = 0.0333333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell2.anm"
                }
                # mEventDataMap: map[hash,pointer] = {
                    # 0x26a07077 = ConformToPathEventData {
                        # mMaskDataName: hash = 0x26a07077
                        # mBlendInTime: f32 = 0.1
                        # mBlendOutTime: f32 = 0.2
                    # }
                # }
            }
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "AA"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell3.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_death.anm"
                }
            }
            "Spell4_Loop" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Spell4_Winddown" = AtomicClipData {
                mTrackDataName: hash = "Default"
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
                mTrackDataName: hash = "AA"
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
                mTrackDataName: hash = "AA_below"
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
                mTrackDataName: hash = "Default"
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
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_recall.anm"
                }
            }
            0x6208af50 = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_recall_idle.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "AA"
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
                mTrackDataName: hash = "AA"
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
                mTrackDataName: hash = "AA"
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
            "Run1_Fast" = AtomicClipData {
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
            "Q_2" = AtomicClipData { # Doesn't work. Attack spells are really weirdly set-up.
                mTrackDataName: hash = "Default"
                mMaskDataName: hash = "UpperBody"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/rengar_2ndQ.anm"
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
                mTrackDataName: hash = "AA"
                mEventDataMap: map[hash,pointer] = {
                    "Normal" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas"
                        mStartFrame: f32 = 15
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
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
                mTrackDataName: hash = "AA"
                mEventDataMap: map[hash,pointer] = {
                    "Emp" = ParticleEventData {
                        mEffectKey: hash = "Rengar_Q_Cas_Max_MyWay"
                        mStartFrame: f32 = 15
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
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
                mTrackDataName: hash = "AA"
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
                        mEffectKey: hash = "Rengar_Q_Cas_Max"
                        mStartFrame: f32 = 15
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
            }
            "A4_Emp_jump" = AtomicClipData {
                mTrackDataName: hash = "AA"
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
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_jump.anm"
                }
            }
            #----------
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
            "Default" = TrackData {
                mPriority: u8 = 5
            }
            "Spell2" = TrackData {
                mPriority: u8 = 4
            }
            "AA" = TrackData { 
                mPriority: u8 = 2
            }
            "AA_below" = TrackData { 
                mPriority: u8 = 3
            }
            "Spell3" = TrackData { 
                mPriority: u8 = 1
            }
            "null" = TrackData { 
                mPriority: u8 = 6
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            # 18429392157443706570 = TimeBlendData {
                # mTime: f32 = 0.05
            # }
            # 18429392158272476449 = TimeBlendData {
                # mTime: f32 = 0.05
            # }
            6030852524956536522 = TransitionClipBlendData {
                mClipName: hash = "Q_2"
            }
            6030852525734973544 = TransitionClipBlendData {
                mClipName: hash = "Q_2"
            }
            2432597616235167053 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData {
                mTime: f32 = 0
            }
            5406481393446862157 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502141246797 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151960743245 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300475582756 = TimeBlendData {}
            6521702300509137994 = TimeBlendData {}
            6521702300525915613 = TimeBlendData {}
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313875975501 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776836431181 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110054976845 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            12217611127544659277 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556603804248356 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556603837803594 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556603854581213 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556605523311949 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793905162304845 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230072053069 = TimeBlendData {
                mTime: f32 = 0
            }
            13399971879891549517 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109403501965 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109883893864 = TimeBlendData {
                mTime: f32 = 0.025
            }
            1131039250531629160 = TimeBlendData {
                mTime: f32 = 0.03
            }
            11831733634412495629 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634660186216 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12217611127215729814 = TimeBlendData {
                mTime: f32 = 0
            }
            12217611127373576296 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12895556603067846346 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run_TRA"
            }
            12895556603142755776 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
            }
            12895556603753915499 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556603846283368 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
            }
            12895556604164517606 = TransitionClipBlendData {
                mClipName: hash = 0x713ed5b5
            }
            12895556604249691573 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605352228968 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12895556605538995048 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556606105937457 = TransitionClipBlendData {
                mClipName: hash = 0x713ed5b5
            }
            13039675255171725416 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13039675255205280654 = TimeBlendData {
                mTime: f32 = 0
            }
            13093444448966555752 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13093444449012630106 = TimeBlendData {
                mTime: f32 = 0
            }
            13093444449137638733 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580131806497 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005851105384 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13156647005911895230 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793904991221864 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13183793905058332340 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853229900970088 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13255853229984858183 = TimeBlendData {
                mTime: f32 = 0
            }
            13399971879720466536 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13399971879837909869 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339236423784 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13590883339398317155 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413649418344 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13697710809356035179 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13697710809406368036 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13697710809439923274 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13697710809456700893 = TimeBlendData {
                mTime: f32 = 0.1
            }
            13697710810954348648 = TimeBlendData {
                mTime: f32 = 0.03
            }
            13697710811141114728 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970914175080 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13987674971168453702 = TimeBlendData {
                mTime: f32 = 0
            }
            15677482531575707752 = TimeBlendData {
                mTime: f32 = 0.025
            }
            15677482531746790733 = TimeBlendData {
                mTime: f32 = 0
            }
            15677482532223425356 = TimeBlendData {
                mTime: f32 = 0
            }
            1588456593522644187 = TimeBlendData {
                mTime: f32 = 0
            }
            1588456596155283560 = TimeBlendData {
                mTime: f32 = 0.03
            }
            16132709916324804712 = TimeBlendData {
                mTime: f32 = 0.025
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709917078513201 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949399541864 = TimeBlendData {
                mTime: f32 = 0.025
            }
            17876238950559197340 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613627986596 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616064084072 = TimeBlendData {
                mTime: f32 = 0.025
            }
            3084207950027116234 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207952311498856 = TimeBlendData {
                mTime: f32 = 0.025
            }
            3405941502114026944 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3405941504323500136 = TimeBlendData {
                mTime: f32 = 0.025
            }
            5406481391532092974 = TimeBlendData {
                mTime: f32 = 0
            }
            5406481393275779176 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6030852527240919144 = TimeBlendData {
                mTime: f32 = 0.03
            }
            6247030501970163816 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6391149151789660264 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6427569502291185768 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503797131368 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6463208476699408488 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639312315844157 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313704892520 = TimeBlendData {
                mTime: f32 = 0.025
            }
            7064088775307603792 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776665348200 = TimeBlendData {
                mTime: f32 = 0.025
            }
            7794375147286900454 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148474611816 = TimeBlendData {
                mTime: f32 = 0.025
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            8160194548925812426 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run_TRA"
            }
            8160194549000721856 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
            }
            8160194549611881579 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8160194549662214436 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8160194549695769674 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8160194549704249448 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
            }
            8160194549712547293 = TimeBlendData {
                mTime: f32 = 0.1
            }
            8160194550022483686 = TimeBlendData {
                mTime: f32 = 0
            }
            8160194550107657653 = TimeBlendData {
                mTime: f32 = 0
            }
            8160194551210195048 = TimeBlendData {
                mTime: f32 = 0.03
            }
            8160194551963903537 = TimeBlendData {
                mTime: f32 = 0
            }
            9598973758890457192 = TimeBlendData {
                mTime: f32 = 0.03
            }
        }
    }
}
