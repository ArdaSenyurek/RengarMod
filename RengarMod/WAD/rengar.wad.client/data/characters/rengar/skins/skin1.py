#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Rengar/Rengar.bin"
    "DATA/Characters/Rengar/Animations/Skin0.bin"
    "DATA/Rengar_Skins_Skin1_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Rengar_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin1" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "HunterRengar"
        metaDataTags: string = "gender:male,race:vastaya,faction:ixtal,skinline:headhunter,appearance:feline"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Rengar/Skins/Skin01/RengarLoadScreen_1.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Rengar"
                "RengarSkin01"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Rengar_Skin01_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Skin01/Rengar_Skin01_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Skin01/Rengar_Skin01_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_RengarSkin01_RengarE_hit"
                        "Play_sfx_RengarSkin01_RengarE_missilelaunch"
                        "Play_sfx_RengarSkin01_RengarEEmpmis_OnHit"
                        "Play_sfx_RengarSkin01_RengarEEmpmis_OnMissileLaunch"
                        "Play_sfx_RengarSkin01_RengarPEmp_buffactivate"
                        "Play_sfx_RengarSkin01_RengarR_buffactivateheartbeat"
                        "Play_sfx_RengarSkin01_RengarR_buffactivateheartbeat_stop"
                        "Play_sfx_RengarSkin01_RengarR_OnBuffActivate"
                        "Play_sfx_RengarSkin01_RengarR_OnBuffDeactivate"
                        "Play_sfx_RengarSkin01_RengarR_OnCast"
                        "Play_sfx_RengarSkin01_RengarRSecondaryTarget_end"
                        "Play_sfx_RengarSkin01_RengarRSecondaryTarget_start"
                        "Play_sfx_RengarSkin01_RengarRstealth_end"
                        "Play_sfx_RengarSkin01_RengarRstealth_start"
                        "Stop_sfx_RengarSkin01_RengarR_buffactivateheartbeat"
                        "Stop_sfx_RengarSkin01_RengarR_OnBuffActivate"
                        "Stop_sfx_RengarSkin01_RengarR_OnBuffDeactivate"
                    }
                }
                BankUnit {
                    name: string = "Rengar_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Base/Rengar_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Base/Rengar_Base_SFX_events.bnk"
                    }
                }
                BankUnit {
                    name: string = "Rengar_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Rengar_Attack2DGeneral"
                        "Play_vo_Rengar_Death3D"
                        "Play_vo_Rengar_FirstEncounter3DKhazix"
                        "Play_vo_Rengar_Joke3DGeneral"
                        "Play_vo_Rengar_Laugh3DGeneral"
                        "Play_vo_Rengar_Move2DStandard"
                        "Play_vo_Rengar_RengarBasicAttack2_cast3D"
                        "Play_vo_Rengar_RengarBasicAttack3_cast3D"
                        "Play_vo_Rengar_RengarBasicAttack_cast3D"
                        "Play_vo_Rengar_RengarCritAttack_cast3D"
                        "Play_vo_Rengar_RengarE_cast3D"
                        "Play_vo_Rengar_RengarEEmp_cast3D"
                        "Play_vo_Rengar_RengarQ_cast3D"
                        "Play_vo_Rengar_RengarQEmp_cast3D"
                        "Play_vo_Rengar_RengarR_cast3D"
                        "Play_vo_Rengar_RengarW_cast3D"
                        "Play_vo_Rengar_RengarWEmp_cast3D"
                        "Play_vo_Rengar_Spell3DPStackFive"
                        "Play_vo_Rengar_Spell3DPStackFour"
                        "Play_vo_Rengar_Spell3DPStackOne"
                        "Play_vo_Rengar_Spell3DPStackThree"
                        "Play_vo_Rengar_Spell3DPStackTwo"
                        "Play_vo_Rengar_Taunt3DGeneral"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Rengar/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Rengar/Skins/Skin01/Rengar_hunter.skl"
            simpleSkin: string = "ASSETS/Characters/Rengar/Skins/Skin01/Rengar_hunter.skn"
            texture: string = "ASSETS/Characters/Rengar/Skins/Skin01/Rengar_hunter_TX_CM.tex"
            skinScale: f32 = 0.9
            selfIllumination: f32 = 0.7
            overrideBoundingBox: option[vec3] = {
                { 180, 250, 180 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            rigPoseModifierData: list[pointer] = {
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = "tail1"
                    mEndingJointName: hash = "Tail5"
                    mDefaultMaskName: hash = 0xef7cfc3b
                    mVelMultiplier: f32 = 1
                }
            }
        }
        armorMaterial: string = "Flesh"
        mContextualActionData: link = "Characters/Rengar/CAC/Rengar_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Rengar/HUD/Rengar_Circle_0.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Rengar/HUD/Rengar_Square_0.tex"
        }
        iconAvatar: string = "ASSETS/Characters/Rengar/HUD/Rengar_Circle_1.tex"
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
            attachToBone: string = "Buffbone_Glb_Ground_Loc"
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = "Emblems/29"
            }
        }
        mResourceResolver: link = "Characters/Rengar/Skins/Skin1/Resources"
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    mScriptName: string = "RengarPassiveBuff"
                }
                ForceRenderVfx: bool = true
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        effectKey: hash = "CameraTint"
                        ShowToOwnerOnly: bool = false
                        AttachToCamera: bool = true
                    }
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = AllTrueMaterialDriver {
                    mDrivers: list[pointer] = {
                        HasBuffDynamicMaterialBoolDriver {
                            mScriptName: string = "RengarQ"
                        }
                        NotMaterialDriver {
                            mDriver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "attack4"
                                }
                            }
                        }
                    
                    }
                }                     
               
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        BoneName: string = "weapon"
                        effectKey: hash = "Q_Trail"
                        ShowToOwnerOnly: bool = false
                    }
                }
            }
            
        }
    }
    "Characters/Rengar/Skins/Skin1/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Rengar_BA1_Cas" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_BA1_Cas"
            "Rengar_BA2_Cas" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_BA2_Cas"
            "Rengar_BA3_Cas" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_BA3_Cas"
            "Rengar_BA_tar_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_01"
            "Rengar_BA_tar_crit_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_crit_01"
            "Rengar_C_Cas" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_C_Cas"
            "Rengar_E_Max_Mis" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_E_Max_Mis"
            "Rengar_E_Max_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_E_Max_Tar"
            "Rengar_E_Mis" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_E_Mis"
            "Rengar_E_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_E_Tar"
            "Rengar_P_Buf_Dash_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Dash_01"
            "Rengar_P_Buf_Enhanced_Ring" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_P_Buf_Enhanced_Ring"
            "Rengar_P_Leap_Grass" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_P_Leap_Grass"
            "Rengar_P_Leap_tar_crit_sound" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_tar_crit_sound"
            "Rengar_P_Leap_tar_sound" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_tar_sound"
            "Rengar_P_Leap_tar_sound" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Tar_MyWay"
            "Rengar_Q_AS_Buf" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_AS_Buf"
            "Rengar_Q_Buf_Blade" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Buf_Blade"
            "Rengar_Q_Buf_Blade_Max" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Buf_Blade_Max"
            "Rengar_Q_Buf_Claw" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Buf_Claw"
            "Rengar_Q_Buf_Claw_Max" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Buf_Claw_Max"
            "Rengar_Q_Cas" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Cas"
            "Rengar_Q_Max_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Max_Tar"
            "Rengar_Q_Strike" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Strike"
            "Rengar_Q_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Tar"
            "Rengar_R_Armor_shred_tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Armor_shred_tar"
            "Rengar_R_Buf" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_R_Buf"
            "Rengar_R_Primary_Target" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_R_Primary_Target"
            "Rengar_R_Primary_Target_Enhanced" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_R_Primary_Target_Enhanced"
            "Rengar_R_Secondary_Target" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_R_Secondary_Target"
            "Rengar_R_Secondary_Target_Sound_Off" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_Off"
            "Rengar_R_Secondary_Target_Sound_On" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_On"
            "Rengar_W_Emp_Buf2" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_SKin01_W_Emp_Buf2"
            "Rengar_W_Heal" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Heal"
            "Rengar_W_Max_Buf" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Max_Buf"
            "Rengar_W_Max_Roar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Max_Roar"
            "Rengar_W_Max_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Max_Tar"
            "Rengar_W_Roar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Roar"
            "Rengar_W_Tar" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_W_Tar"
            "rengar_emote_dance_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_dance_sound"
            "rengar_emote_death_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_death_sound"
            "rengar_emote_joke_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_joke_sound"
            "rengar_emote_laugh_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_laugh_sound"
            "rengar_emote_taunt_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_taunt_sound"
            "Rengar_LeapSound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_LeapSound"
            "Rengar_VO_Seen_BV2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_VO_Seen"
            "Rengar_P_Buf_Max" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_P_Buf_Max"
            0xcdc6293f = 0xa60f0d10
            "Rengar_Q_Cas_Max_MyWay" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Skin01_Q_Cas_Max_MyWay"
            "Rengar_RLeap_Override" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_Base_R_LeapMatOverride"
            "CameraTint" = "Characters/Rengar/Skins/Skin1/Particles/Rengar_CameraTint"
            
            "Q_Trail" = "Characters/Rengar/Skins/Skin1/Particles/Q_Trail"
        }
    }
}
