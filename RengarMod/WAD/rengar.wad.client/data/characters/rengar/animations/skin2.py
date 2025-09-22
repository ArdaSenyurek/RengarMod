#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Animations/Skin2" = animationGraphData {
        mCascadeBlendValue: f32 = 0
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
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Crit" = ParticleEventData {
                        mName: hash = "Crit"
                        mStartFrame: f32 = 1
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
            "Dance_Base" = AtomicClipData {
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
            "Idle1_Base" = AtomicClipData {
                mFlags: u32 = 3
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2_Base" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            0x9e55a33e = AtomicClipData {
                mFlags: u32 = 1
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
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_run1.anm"
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
            "Spell2" =  AtomicClipData {
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
            "Spell5" = ConditionBoolClipData {
                #mTrackDataName: hash = "actions"
                Updater: pointer = LogicDriverBoolParametricUpdater {                     
                    driver: pointer =  FixedDurationTriggeredBoolDriver {
                            mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarR"
                            }
                            mCustomDuration: f32 = 0.5
                        }
                }
                mChangeAnimationMidPlay: bool = false
                mFalseConditionClipName: hash = "spell5_NH"
                mTrueConditionClipName: hash = "spell5_Ult"
            }
            
            "spell5_NH" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell5_parametric_NH"
                    "Spell5_logic_NH"
                    "Spell5_legs_NH"
                    "A4_Run_Jump_NH"
                    "spell5_logic_AbsoluteNull_NH"
                }
            }  
            "spell5_Ult" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell5_parametric"
                    "spell5_logic"
                    "Spell5_legs"
                    "A4_Run_Jump"
                    "spell5_logic_AbsoluteNull"
                }
            }
            
            "Spell5_parametric_NH" = ConditionBoolClipData {
                mTrackDataName: hash = "actions"
                Updater: pointer = LogicDriverBoolParametricUpdater {                     
                    driver: pointer =  AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell2"
                                }
                            }
                            FloatComparisonMaterialDriver {
                                mOperator: u32 = 2
                                mValueB: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 0.285
                                }
                                mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                    mAnimationName: hash = "spell5_logic"
                                }
                            }
                        }                 
                    }
                }
                mPlayAnimChangeFromBeginning: bool = true
                mChangeAnimationMidPlay: bool = true
                mFalseConditionClipName: hash = "Spell5_coreUB_NH"
                mTrueConditionClipName: hash = "Spell2"
            }
            "Spell5_parametric" = ConditionBoolClipData {
                mTrackDataName: hash = "actions"
                Updater: pointer = LogicDriverBoolParametricUpdater {                     
                    driver: pointer =  AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell2"
                                }
                            }
                            FloatComparisonMaterialDriver {
                                mOperator: u32 = 2
                                mValueB: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 0.285
                                }
                                mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                    mAnimationName: hash = "spell5_logic"
                                }
                            }
                        }                 
                    }
                }
                mPlayAnimChangeFromBeginning: bool = true
                mChangeAnimationMidPlay: bool = true
                mFalseConditionClipName: hash = "Spell5_coreUB"
                mTrueConditionClipName: hash = "Spell2"
            }
            
            
            "Spell5_legs_NH" = AtomicClipData {
                mTrackDataName: hash = "Actions_below"
                mMaskDataName: hash = "Legs"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/animations/Rengar_dash_S4.anm"
                }
            }
            "Spell5_coreUB_NH" = AtomicClipData {
                mTrackDataName: hash = "actions"
                mMaskDataName: hash = "UpperBody_ForDash"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/animations/Rengar_dash_S4.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "spell3"
                    }
                    "StopLegs" = StopAnimationEventData {
                        mStartFrame: f32 = 27.5
                        mStopAnimationName: hash = "Spell5_legs_NH"
                    }
                    "LockSpell3" = LockRootOrientationEventData {
                        JointName: hash = "root"
                        mEndFrame: f32 = 20.5
                    }
                }
            }
            "Spell5_logic_NH" = AtomicClipData {
                mTrackDataName: hash = "nulll"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/animations/Rengar_dash_S4.anm"
                }
                EndFrame: f32 = 100
            }
            "spell5_logic_AbsoluteNull_NH" = AtomicClipData {
                mTrackDataName: hash = "AbsNull"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/animations/Rengar_dash_S4.anm"
                }
                EndFrame: f32 = 100
            }
            
            "Spell5_legs" = AtomicClipData {
                mTrackDataName: hash = "Actions_below"
                mMaskDataName: hash = "Legs"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash3.anm"
                }
            }
            "Spell5_coreUB" = AtomicClipData {
                mTrackDataName: hash = "actions"
                mMaskDataName: hash = "UpperBody_ForDash"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash3.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "spell3"
                    }
                    "StopLegs" = StopAnimationEventData {
                        mStartFrame: f32 = 27.5
                        mStopAnimationName: hash = "spell5_legs"
                    }
                    "LockSpell3" = LockRootOrientationEventData {
                        JointName: hash = "root"
                        mEndFrame: f32 = 20.5
                    }
                }
            }
            "Spell5_logic" = AtomicClipData {
                mTrackDataName: hash = "nulll"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash3.anm"
                }
                EndFrame: f32 = 100
            }
            "spell5_logic_AbsoluteNull" = AtomicClipData {
                mTrackDataName: hash = "AbsNull"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/dash3.anm"
                }
                EndFrame: f32 = 100
            }
            
            "Attack4" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAttackingBoolDriver {}
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = false
                mTrueConditionClipName: hash = "Attack4_land"
                mFalseConditionClipName: hash = "A4_Tiamat_Condition_Core"
            } 
            
            "A4_Tiamat_Condition_Core" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell5_logic_NH"
                                }
                            }
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell5_logic"
                                }
                            }
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = false
                mTrueConditionClipName: hash = "Attack4_DuringJump"
                mFalseConditionClipName: hash = "A4_Emp"
            }
            "Attack4_DuringJump" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell5_logic"
                                }
                            }
                            
                            FloatComparisonMaterialDriver {
                                mOperator: u32 = 2
                                mValueA: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 0.17
                                }
                                mValueB: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                    mAnimationName: hash = "spell5_logic"
                                }
                            }
                            
                        }
                    }
                }
                mChangeAnimationMidPlay: bool = false
                mFalseConditionClipName: hash = "A4_Emp"
                mTrueConditionClipName: hash = "A4_Jump_Core"
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
                mChangeAnimationMidPlay: bool = false
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
                    "NQ_SFX" = SoundEventData {
                        mSoundName: string = "Play_sfx_Leap_RengarQ_Stab"
                        mIsLoop: bool = false
                        mStartFrame: f32 = 4
                        mFireIfAnimationEndsEarly: bool = true
                        mIsKillEvent:bool = false
                        mSkipIfPastEndFrame: bool = false
                    }
                    "StopLeapLogic" = StopAnimationEventData {
                        mStopAnimationName: hash = "spell5_logic_AbsoluteNull"
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
                                    mMultiplier: f32 = 1
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
                    "NQ_SFX" = SoundEventData {
                        mSoundName: string = "Play_sfx_Leap_RengarQ_Stab"
                        mIsLoop: bool = false
                        mStartFrame: f32 = 4
                        mFireIfAnimationEndsEarly: bool = true
                        mIsKillEvent:bool = false
                        mSkipIfPastEndFrame: bool = false
                    }
                    "StopLeapLogic" = StopAnimationEventData {
                        mStopAnimationName: hash = "spell5_logic_AbsoluteNull"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_attack4_long.anm"
                }
            }
            "A4_Jump_Core" = AtomicClipData {
                mTrackDataName: hash = "channel"
                mMaskDataName: hash = "GroundExcluded"
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
                    "NQ_SFX" = SoundEventData {
                        mSoundName: string = "Play_sfx_Leap_RengarQ_Stab"
                        mIsLoop: bool = false
                        mStartFrame: f32 = 4
                        mFireIfAnimationEndsEarly: bool = true
                        mIsKillEvent:bool = false
                        mSkipIfPastEndFrame: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_Jump3.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = AttackSpeedParametricUpdater { }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mMultiplier: f32 = 0
                                    mIncrement: f32 = 1.2
                                }
                            }
                        }
                    }
                }
            }
            "A4_Run_Jump_NH" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer =  FixedDurationTriggeredBoolDriver {
                        mCustomDuration: f32 = 0.5
                        mBoolDriver: pointer = IsCastingBoolDriver {
                            SpellSlot: u32 = 7
                       }
                    }
                }
                mChangeAnimationMidPlay: bool = true
                mPlayAnimChangeFromBeginning: bool = true
                DontStompTransitionClip: bool = true
                mTrueConditionClipName: hash = "ChannelBelow_Level_A4_NH_ForTiamat"
                mFalseConditionClipName: hash = "spell5_logic_AbsoluteNull"
            }
            
            
            "A4_Run_Jump" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer =  FixedDurationTriggeredBoolDriver {
                        mCustomDuration: f32 = 0.5
                        mBoolDriver: pointer = IsCastingBoolDriver {
                            SpellSlot: u32 = 7
                       }
                    }
                }
                mChangeAnimationMidPlay: bool = true
                mPlayAnimChangeFromBeginning: bool = true
                DontStompTransitionClip: bool = true
                mTrueConditionClipName: hash = "ChannelBelow_Level_A4_Jump_ForTiamat"
                mFalseConditionClipName: hash = "spell5_logic_AbsoluteNull"
            }
            "ChannelBelow_Level_A4_Jump_ForTiamat" = AtomicClipData {
                mTrackDataName: hash = "channel_below"
                mMaskDataName: hash = "UpperBody"


                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_Jump3.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = AttackSpeedParametricUpdater { }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mMultiplier: f32 = 0
                                    mIncrement: f32 = 1.2
                                }
                            }
                        }
                    }
                }
            }
            "ChannelBelow_Level_A4_NH_ForTiamat" = AtomicClipData {
                mTrackDataName: hash = "channel_below"
                mMaskDataName: hash = "UpperBody"


                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/rengar_attack4_Jump3.anm"
                }
                mUpdaterResourceData: pointer = UpdaterResourceData {
                    mUpdaterDataList: list[embed] = {
                        UpdaterData {
                            Input: pointer = AttackSpeedParametricUpdater { }
                            mOutputType: u32 = 1
                            mValueProcessorDataList: list[pointer] = {
                                LinearTransformProcessorData {
                                    mMultiplier: f32 = 0
                                    mIncrement: f32 = 1.2
                                }
                            }
                        }
                    }
                }
            }
            "Default_Level_A4_ForTiamat" = AtomicClipData {
                mTrackDataName: hash = "Default"
                
                mTickDuration: f32 = 0.034

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
                                    mMultiplier: f32 = 1
                                }
                            }
                        }
                    }
                }
            }
            
            "Taunt_Base" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
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
            "Joke" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Joke3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Joke.anm"
                }
            }
            0x76bbc6a0 = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
                }
            }
            0x7cb9d840 = AtomicClipData {
                mFlags: u32 = 3
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
            "Recall" = AtomicClipData {
                mTrackDataName: hash = "channel"
                mEventDataMap: map[hash,pointer] = {
                    "Hood" = SubmeshVisibilityEventData {
                        mName: hash = "Hood"
                        mStartFrame: f32 = 67
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                    "Audio_Recall" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Recall3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_recall.anm"
                }
            }
            "Run1_Fast" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0xf4784b95
                    0x7cb9d840
                }
            }
            0xf4784b95 = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_run1_Fast.anm"
                }
            }
            0x8932308b = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Idle1.anm"
                }
            }
            "Idle1" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x1b254ae6
                        mProbability: f32 = 75
                    }
                    SelectorPairData {
                        mClipName: hash = 0x2c00f6af
                        mProbability: f32 = 25
                    }
                }
            }
            0xc5288be8 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Idle2.anm"
                }
            }
            0x747ae0f5 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Idle3.anm"
                }
            }
            0x299519f8 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Taunt.anm"
                }
            }
            "taunt" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Taunt_Base"
                    0x299519f8
                }
            }
            0xfebfc6d3 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Laugh.anm"
                }
            }
            "Laugh" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x9e55a33e
                    0xfebfc6d3
                }
            }
            "Dance" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Dance_Base"
                    0xd4939539
                }
            }
            0xd4939539 = AtomicClipData {
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_Dance.anm"
                }
            }
            "Recall_Winddown" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Winddown" = SubmeshVisibilityEventData {
                        mName: hash = "Winddown"
                        mEndFrame: f32 = 2
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Hood_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = "Hood"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    0xe6fda1e1 = SubmeshVisibilityEventData {
                        mName: hash = 0xe6fda1e1
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_hood_loop.anm"
                }
            }
            "Hood_Off" = AtomicClipData {
                mMaskDataName: hash = "Arm"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    "hoodoff" = SubmeshVisibilityEventData {
                        mName: hash = "hoodoff"
                        mEndFrame: f32 = 17
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_hood_off.anm"
                }
            }
            0xd884c53b = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = "Arm"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    "hoodon" = SubmeshVisibilityEventData {
                        mName: hash = "hoodon"
                        mStartFrame: f32 = 14
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Skin02/Rengar_skin02_hood_on.anm"
                }
            }
            0x1d902a0d = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xd884c53b
                    "Hood_Loop"
                }
            }
            0x713ed5b5 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x9c4b7e97 = ParticleEventData {
                        mName: hash = 0x9c4b7e97
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
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_TRA.anm"
                }
            }
            0x1b254ae6 = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle1_Base"
                    0x8932308b
                }
            }
            0x2c00f6af = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle2_Base"
                    0xc5288be8
                }
            }
            "Spell4_Idle" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x747ae0f5
                    0x76bbc6a0
                }
            }
            "Spell1_Run_TRA" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_run_TRA.anm"
                }
            }
            "Spell1_Run2_TRA" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Rengar/Skins/Base/Animations/Rengar_spell1_run2_TRA.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "Hood" = MaskData {
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
                    1
                    1
                }
            }
            "Tassel" = MaskData {
                mId: u32 = 1
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
                    1
                    0
                    0
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
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
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
            "Arm" = MaskData {
                mId: u32 = 2
                mWeightList: list[f32] = {
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
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
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
                    0
                    0
                    0
                    0
                    0
                    0
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
                    0
                    0
                    1
                    1
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
                    0
                    0
                }
            }
            "GroundExcluded" = MaskData {
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
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
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
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
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
                    1
                    1 # Ground
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
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
            "Hood" = TrackData {
                mPriority: u8 = 0
            }
            "Tassel" = TrackData {
                mPriority: u8 = 5
            }
            "Channel" = TrackData {
                mPriority: u8 = 0
            }
            "Channel_below" = TrackData {
                mPriority: u8 = 1
            }
            "Default" = TrackData {
                mPriority: u8 = 5
            }
            "Actions" = TrackData { 
                mPriority: u8 = 2
            }
            "Spell" = TrackData { 
                mPriority: u8 = 4
            }
            "Actions_below" = TrackData { 
                mPriority: u8 = 3
            }
            "nulll" = TrackData { 
                mPriority: u8 = 6
            }
            "AbsNull" = TrackData { 
                mPriority: u8 = 7
            }
            
        }
        mBlendDataTable: map[u64,pointer] = {
            350652854184754509 = TimeBlendData {
                mTime: f32 = 0
            }
            897461255355809101 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616235167053 = TimeBlendData {
                mTime: f32 = 0
            }
            2996329683201080653 = TimeBlendData {
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
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300835852006 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300975292661 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301013100192 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301322850443 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301854066283 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302328851432 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302777271857 = TimeBlendData {
                mTime: f32 = 0
            }
            6664513967696166221 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313875975501 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776836431181 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            8393268201603513677 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData {
                mTime: f32 = 0
            }
            8987452303957605709 = TimeBlendData {
                mTime: f32 = 0
            }
            9886017508763811149 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110054976845 = TimeBlendData {
                mTime: f32 = 0
            }
            11409204720869883213 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168680979789 = TimeBlendData {
                mTime: f32 = 0
            }
            12217611127544659277 = TimeBlendData {
                mTime: f32 = 0
            }
            12771797303277698381 = TimeBlendData {
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
            13630352412461706982 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412601147637 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412638955168 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412948705419 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413954706408 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352414403126833 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            14206758856262466893 = TimeBlendData {
                mTime: f32 = 0
            }
            15317750832836427085 = TimeBlendData {
                mTime: f32 = 0
            }
            15601811869485546829 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            17615913048955469133 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            18356609218899393869 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109883893864 = TimeBlendData {
                mTime: f32 = 0.025
            }
            11409204720698800232 = TimeBlendData {
                mTime: f32 = 0.025
            }
            11831733634660186216 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12167572168509896808 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12217611127373576296 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12771797303106615400 = TimeBlendData {
                mTime: f32 = 0.025
            }
            12895556603067846346 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run_TRA"
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
            12895556604341765792 = TransitionClipBlendData {
                mClipName: hash = 0x713ed5b5
            }
            12895556604442302528 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
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
            13093444449137638733 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793904991221864 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13255853229900970088 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13399971879720466536 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13630352413649418344 = TimeBlendData {
                mTime: f32 = 0.025
            }
            13987674970914175080 = TimeBlendData {
                mTime: f32 = 0.025
            }
            14206758856091383912 = TimeBlendData {
                mTime: f32 = 0.025
            }
            15317750832665344104 = TimeBlendData {
                mTime: f32 = 0.025
            }
            15601811869314463848 = TimeBlendData {
                mTime: f32 = 0.025
            }
            15677482531575707752 = TimeBlendData {
                mTime: f32 = 0.025
            }
            15677482531746790733 = TimeBlendData {
                mTime: f32 = 0
            }
            1588456596155283560 = TimeBlendData {
                mTime: f32 = 0.025
            }
            16132709916324804712 = TimeBlendData {
                mTime: f32 = 0.025
            }
            17615913048784386152 = TimeBlendData {
                mTime: f32 = 0.025
            }
            18356609218728310888 = TimeBlendData {
                mTime: f32 = 0.025
            }
            1956051968038845773 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616064084072 = TimeBlendData {
                mTime: f32 = 0.025
            }
            2996329683029997672 = TimeBlendData {
                mTime: f32 = 0.025
            }
            3084207952311498856 = TimeBlendData {
                mTime: f32 = 0.025
            }
            3170805372322102605 = TimeBlendData {
                mTime: f32 = 0
            }
            350652854013671528 = TimeBlendData {
                mTime: f32 = 0.025
            }
            5406481393275779176 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6030852527240919144 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6247030501970163816 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6391149151789660264 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6427569503797131368 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6463208476699408488 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6521702302023563368 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6664513967525083240 = TimeBlendData {
                mTime: f32 = 0.025
            }
            6929639313704892520 = TimeBlendData {
                mTime: f32 = 0.025
            }
            7064088776665348200 = TimeBlendData {
                mTime: f32 = 0.025
            }
            7794375148474611816 = TimeBlendData {
                mTime: f32 = 0.025
            }
            8160194548925812426 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run_TRA"
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
            8160194550199731872 = TimeBlendData {
                mTime: f32 = 0
            }
            8160194550300268608 = TransitionClipBlendData {
                mClipName: hash = "Spell1_Run2_TRA"
            }
            8160194551210195048 = TimeBlendData {
                mTime: f32 = 0.025
            }
            8160194551381278029 = TimeBlendData {
                mTime: f32 = 0
            }
            8160194551963903537 = TimeBlendData {
                mTime: f32 = 0
            }
            8393268201432430696 = TimeBlendData {
                mTime: f32 = 0.025
            }
            8555650310619936872 = TimeBlendData {
                mTime: f32 = 0.025
            }
            897461255184726120 = TimeBlendData {
                mTime: f32 = 0.025
            }
            8987452303786522728 = TimeBlendData {
                mTime: f32 = 0.025
            }
            9886017508592728168 = TimeBlendData {
                mTime: f32 = 0.025
            }
        }
    }
}
