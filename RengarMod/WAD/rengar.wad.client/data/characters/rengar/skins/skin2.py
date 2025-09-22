#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Rengar/Animations/Skin2.bin"
    "DATA/Characters/Rengar/Rengar.bin"
    "DATA/Rengar_Skins_Skin1_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Rengar_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Rengar_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin2" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "rengarSkin02"
        metaDataTags: string = "gender:male,race:vastaya,faction:ixtal,skinline:legacy,appearance:feline"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Rengar/Skins/Skin02/RengarLoadScreen_2.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Rengar"
                "RengarSkin02"
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
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Leap/Leap_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Leap/Leap_SFX_events.bnk"
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
            animationGraphData: link = "Characters/Rengar/Animations/Skin2"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Rengar/Skins/Skin02/rengar_Skin02.skl"
            simpleSkin: string = "ASSETS/Characters/Rengar/Skins/Skin02/rengar_Skin02.skn"
            texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/rengar_Skin02_TX_CM.tex"
            skinScale: f32 = 0.95
            selfIllumination: f32 = 0.7
            overrideBoundingBox: option[vec3] = {
                { 180, 250, 180 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Hood"
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
        iconAvatar: string = "ASSETS/Characters/Rengar/HUD/Rengar_Circle_2.tex"
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
            attachToBone: string = "Buffbone_Glb_Ground_Loc"
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = "Emblems/29"
            }
        }
        mResourceResolver: link = "Characters/Rengar/Skins/Skin2/Resources"
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = AllTrueMaterialDriver {
                    mDrivers: list[pointer] = {
                        IsAnimationPlayingDynamicMaterialBoolDriver {
                            mAnimationNames: list[hash] = {
                                "Spell5_logic"
                            }
                        }
                        FloatComparisonMaterialDriver {
                            mOperator: u32 = 2
                            mValueA: pointer = FloatLiteralMaterialDriver {
                                mValue: f32 = 0.285
                            }
                            mValueB: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                mAnimationName: hash = "spell5_logic"
                            }
                        }
                    }                 
                }                 
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        #BoneName: string = "weapon"
                        effectKey: hash = "Rengar_RLeap_Override"
                        ShowToOwnerOnly: bool = false
                    }
                }
            }
        }        
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA3_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashSkin02"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 120 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 0, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 120 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 0, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Rengar_Skin02_BA3_Cas"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA3_Cas"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA1_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashSkin02"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 110, 80, 50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, -120, -10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 110, 80, 50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                alphaRef: u8 = 255
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, -120, -10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Rengar_Skin02_BA1_Cas"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA1_Cas"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Secondary_Target" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.24
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "dArK_bg"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.2118, 0.1059, 0.6471, 1 }
                            { 0.2588, 0.0471, 0.3294, 0 }
                        }
                    }
                }
                pass: i16 = 70
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1.7, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_R_glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Eye_back"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.102, 0.0824, 0.3882, 1 }
                }
                pass: i16 = -5
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 120, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_mult.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.2, 0 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_tar_vision_eye_glow.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "groundshadow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.1216, 0.1412, 0.3255, 1 }
                }
                pass: i16 = -11
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 120, 10 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_alpha_circle.tex"
            }
        }
        particleName: string = "Rengar_Skin02_R_Secondary_Target"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Secondary_Target"
        flags: u16 = 197
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Rengar_Q_Buf_Blade_Child"
                        }
                    }
                }
                emitterName: string = "Blue_Flames_Parent"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -5
                                        90
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        -20
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 1, 1 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0 }
                }
                pass: i16 = -40
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Blade_Mesh_Flame_Dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Claw_Flame.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.2941, 0.2941, 0.2941, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.2941, 0.2941, 0.2941, 0 }
                            { 0.2941, 0.2941, 0.2941, 0.8 }
                            { 0.2941, 0.2941, 0.2941, 0 }
                        }
                    }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Blade_Flame_2x2.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.15, 0.25 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.15, 0.25 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "powerFlareBurst"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3137, 0.851, 1, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.3137, 0.851, 1, 0.8 }
                            { 0.3137, 0.851, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_flareblue.tex"
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_Claw"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_C_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashSkin02"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -47, 120, 150 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_C_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 190, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    -0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 190, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -47, 120, 150 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_C_WeaponTrail.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 190, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    -0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 190, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                }
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Rengar_Skin02_C_Cas"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_C_Cas"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Max" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Rengar_Q_Buf_Blade_Child"
                        }
                    }
                }
                emitterName: string = "Blue_Flames_Parent"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        60
                                        130
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 1, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                pass: i16 = 40
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "cross1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 60, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0235, 0.0431, 0.1412, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.9
                            1
                        }
                        values: list[vec4] = {
                            { 0.0235, 0.0431, 0.1412, 0 }
                            { 0.0235, 0.0431, 0.1412, 0.8 }
                            { 0.0235, 0.0431, 0.1412, 0.8 }
                            { 0.0235, 0.0431, 0.1412, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 120, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/Items/Item_HextechRevolver_Cyan_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "cross2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 60, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0235, 0.0431, 0.1412, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.9
                            1
                        }
                        values: list[vec4] = {
                            { 0.0235, 0.0431, 0.1412, 0 }
                            { 0.0235, 0.0431, 0.1412, 0.8 }
                            { 0.0235, 0.0431, 0.1412, 0.8 }
                            { 0.0235, 0.0431, 0.1412, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 120, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/Items/Item_HextechRevolver_Cyan_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Blade_Mesh_Flame"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 75, -2.5 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Blade_Flame.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4745, 0.9569, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec4] = {
                            { 0.4745, 0.9569, 1, 0 }
                            { 0.4745, 0.9569, 1, 1 }
                            { 0.4745, 0.9569, 1, 0 }
                        }
                    }
                }
                pass: i16 = 30
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.1, 1.1, 1.1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_EmBuf_Highlight.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5001
                                    0.5002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -0.5
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5001
                                    0.5002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -0.4
                                    0.4
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "powerFlareBurst"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3333, 1, 1, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.3333, 1, 1, 0.8 }
                            { 0.3333, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/FlareBlue.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "powerFlare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3333, 1, 1, 0.4941 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 0.3333, 1, 1, 0 }
                            { 0.3333, 1, 1, 0.4941 }
                            { 0.3333, 1, 1, 0.4941 }
                            { 0.3333, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/FlareBlue.tex"
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_Blade_Max"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Max"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Mis" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Net"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Max_Net.sco"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 10
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -600, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 165, 165, 165 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Net.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "trail_add"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.8
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.7 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.7 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 360 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 10 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 110, 110, 110 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola_Add.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "trail_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 360 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 10 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola_Add.tex"
            }
        }
        particleName: string = "Rengar_Skin02_E_Max_Mis"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Mis"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Buf" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            20
                            40
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.3
                }
                emitterName: string = "Stealth_Swirls"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -100 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                colorLookUpTypeY: u8 = 3
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, -90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_Cas.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.1 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            25
                            50
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.3
                }
                emitterName: string = "Stealth_Swirls_Add"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -100 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB_add.tex"
                colorLookUpTypeY: u8 = 3
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.05
                    fresnelColor: vec4 = { -1, -1, -1, -1 }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, -90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_Cas.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.1 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            # VfxEmitterDefinitionData {
                # rate: embed = ValueFloat {
                    # constantValue: f32 = 1
                # }
                # particleLifetime: embed = ValueFloat {
                    # constantValue: f32 = 0.4
                # }
                # lifetime: option[f32] = {
                    # 0.1
                # }
                # isSingleParticle: flag = true
                # emitterName: string = "base_Hunter"
                # bindWeight: embed = ValueFloat {
                    # constantValue: f32 = 1
                # }
                # primitive: pointer = VfxPrimitiveAttachedMesh {}
                # blendMode: u8 = 1
                # color: embed = ValueColor {
                    # dynamics: pointer = VfxAnimatedColorVariableData {
                        # times: list[f32] = {
                            # 0
                            # 0.1
                            # 1
                        # }
                        # values: list[vec4] = {
                            # { 1, 1, 1, 0 }
                            # { 0, 0.6157, 1, 1 }
                            # { 0, 0.78, 1, 0 }
                        # }
                    # }
                # }
                # pass: i16 = 100
                # colorLookUpTypeY: u8 = 3
                # alphaRef: u8 = 0
                # alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    # erosionMapName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_AlphaSlice.tex"
                # }
                # particleIsLocalOrientation: flag = true
                # isUniformScale: flag = true
                # birthScale0: embed = ValueVector3 {
                    # constantValue: vec3 = { 1.03, 1.03, 1.03 }
                # }
                # scale0: embed = ValueVector3 {
                    # dynamics: pointer = VfxAnimatedVector3fVariableData {
                        # times: list[f32] = {
                            # 0
                            # 1
                        # }
                        # values: list[vec3] = {
                            # { 1, 1, 1 }
                            # { 1.1, 1.1, 1.1 }
                        # }
                    # }
                # }
                # texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_cas_avatar.tex"
            # }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "base_Hunter1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_TransRamp.tex"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.05
                            0.07
                            0.4
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.6157, 1, 0.7  }
                            { 1, 1, 1, 0.7 }
                            { 0, 0.62, 1, 0.7 }
                            { 0, 0.62, 1, 0 }
                            { 0, 0.62, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                colorRenderFlags: u8 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.3
                                0.4
                                1
                            }
                            values: list[f32] = {
                                1 #1 = Full erode.
                                0.2
                                1
                                1
                            }
                        }
                    }
                    LingerErosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionSliceWidth: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Rengar/Skins/Skin02/org2.dds"
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.03, 1.03, 1.03 }
                }
                texture: string = "ASSETS/Shared/Particles/3161common_color-hold.dds"
            }
        }
        particleName: string = "Rengar_Skin02_R_Buf"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Buf"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Buf" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "base"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            -1.5
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/arrow01.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.1, 1.1, 1.1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Avatar.tex"
            }
        }
        particleName: string = "Rengar_Skin02_W_Max_Buf"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarWBuff_buffactivate"

        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Buf"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Net"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.006
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Net.sco"
                    }
                }
                blendMode: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 80, 150 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Net.tex"
            }
        }
        particleName: string = "Rengar_Skin02_E_Max_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Tar"
        overrideScaleCap: option[f32] = {
            500
        }
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Roar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    0.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Skin02"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 600, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_ShoutRing.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    10.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Skin02_Ult"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 600, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Max_ShoutRing.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.8, 0.8, 0.8, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.8, 0.8, 0.8, 0 }
                            { 0.8, 0.8, 0.8, 1 }
                            { 0.8, 0.8, 0.8, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 475, 475, 475 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Ring.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.6
                }
                particleLinger: option[f32] = {
                    10.6
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundRing"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_GroundRing_Geo.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.7, 0.7, 0.7, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.15
                            1
                        }
                        values: list[vec4] = {
                            { 0.7, 0.7, 0.7, 0 }
                            { 0.7, 0.7, 0.7, 1 }
                            { 0.7, 0.7, 0.7, 0 }
                        }
                    }
                }
                pass: i16 = 1
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.7, 0.5, 1.7 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_GroundRing_Sub.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1.75 }
                }
                texDiv: vec2 = { 0.7, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "ShellDistort"
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Rampdown_RGBA.tex"
                blendMode: u8 = 1
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.1
                    normalMapTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Distortion_NormalMap.tex"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 450, 450 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Distortion.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing_ULT"
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB_add.tex"
                pass: i16 = 50
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 650, 650, 650 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Max_Ring.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing_ULT_Add"
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Add_RGB.tex"
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 650, 650, 650 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Max_Ring.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.2
                }
                emitterName: string = "Model_Flash"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            -1.5
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/arrow01.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.1, 1.1, 1.1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.2
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.2, 1.2, 1.2 }
                            { 1.4, 1.4, 1.4 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Avatar.tex"
            }
        }
        particleName: string = "Rengar_Skin02_W_Max_Roar"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarWBuff_buffactivate"

        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Roar"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_AS_Buf" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "powerFlare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3255, 1, 1, 0.298 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 0.3255, 1, 1, 0 }
                            { 0.3255, 1, 1, 0.298 }
                            { 0.3255, 1, 1, 0.298 }
                            { 0.3255, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_flareblue.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.1
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    10.1
                }
                emitterName: string = "ASTrail"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0039, 0.451, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 0.0039, 0.451, 1, 0 }
                            { 0.0039, 0.451, 1, 1 }
                            { 0.0039, 0.2759, 0.1686, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Skin02_Q_AS_Buf"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_AS_Buf"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarQ_buffactivate"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Emp_Buf2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    100
                }
                isSingleParticle: flag = true
                emitterName: string = "Gold_Caustics"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.7
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.1137, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 121
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.03, 1.03, 1.03 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_EmBuf_Highlight.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.4, 0.6 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 0.25, 0.25 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    100
                }
                isSingleParticle: flag = true
                emitterName: string = "red_pulse1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.2118, 0, 0.3882, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.03, 1.03, 1.03 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Swirl_Mask.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.4, 0.6 }
                }
                texDiv: vec2 = { 0.25, 0.25 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_VerticalStreak_Mask.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.5, 0.1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.1
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    0.4
                }
                lifetime: option[f32] = {
                    0.4
                }
                emitterName: string = "Avatar"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, -200, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    2
                                    2
                                    -2
                                    -2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.2
                                    0.2
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
                                    -3
                                    -5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 10, -200, 10 }
                            { 20, -200, 20 }
                            { 50, -200, 50 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/arrow01.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_W_EmBuf_ColorText.tex"
                blendMode: u8 = 4
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 1
                sliceTechniqueRange: f32 = 0.15
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 90 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.85, 1.85, 1.85 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/global_ss_cleanse_alphaslice.dds"
            }
        }
        particleName: string = "Rengar_Skin02_W_Emp_Buf2"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Emp_Buf2"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "cursebandages"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.007
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.007
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Wrap.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 1, 30 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 0.5, 0.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.9
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                            { 0.4, 0.4, 0.4 }
                            { 0.5, 0, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Wrap.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Bola"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.0075
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.0075
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.7
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, -1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, -40, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.8, 0.8, 0.8 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola.tex"
            }
        }
        particleName: string = "Rengar_Skin02_E_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Tar"
        overrideScaleCap: option[f32] = {
            375
        }
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarE_hit"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Enhanced_Ring" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 66
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Ring_FX"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 750, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Heal_Spark_RGBA.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.4263, 1, 0.3804 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 20, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 10, 5, 1 }
                            { 30, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_DarkstarMode_LanternPullTetherThresh_Skin05_W_Einstein_01_mult.tex"
                    texDivMult: vec2 = { 4, 4 }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                HasVariableStartTime: flag = true
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                isSingleParticle: flag = true
                emitterName: string = "Ring_FX1"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 750, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Heal_Spark_RGBA.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.1686, 0.7668, 1, 0.4706 }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 20, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2389
                            1
                        }
                        values: list[vec3] = {
                            { 10, 5, 1 }
                            { 24.6413, 5, 1 }
                            { 30, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ring"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_Void_Ring.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.8 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5062, 0.7605, 1, 1 }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                colorRenderFlags: u8 = 1
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 750, 800, 800 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_CloudTxt06_1.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.1, 0 }
                }
                texDiv: vec2 = { 0.6, 0.3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ring1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_Void_Ring.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.21 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.142, 0.5971, 1, 1 }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                colorRenderFlags: u8 = 1
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 750, 800, 800 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_CloudTxt06_1.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "HARD_EDGE"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_NewRing.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.19, 0.6664, 1, 1 }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 11, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/3026_Items_Noise_02.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.1, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.25 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/3026_Items_Noise_02.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 5, 0.25 }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.08, 0.12 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.08, 0.12 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "HARD_EDGE1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_NewRing.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.19, 0.6184, 1, 0.3098 }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 11, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_CloudTxt06_1.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.1, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.25 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "HARD_EDGE2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_NewRing_02.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.0482, 0.1199, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.6
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.4 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 11, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2556
                            0.5667
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.462, 0.2539, 0.2539 }
                            { 0.8457, 1, 1 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/3026_Items_Noise_02.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.1, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.25 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/3026_Items_Noise_02.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 5, 0.25 }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.08, 0.12 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.08, 0.12 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Skin02_P_Buf_Enhanced_Ring"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Enhanced_Ring"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Mis" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Bola"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Mis_Bola.sco"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 10
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 800, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 130, 130 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "trail_add"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.8
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 360 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 10 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 75 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola_Add.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "trail_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 360 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 10 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 75 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_E_Bola_Add.tex"
            }
        }
        particleName: string = "Rengar_Skin02_E_Mis"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Mis"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarE_missilelaunch"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.075
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Slash"
                EmitterPosition: embed = ValueVector3 { constantValue: vec3 = { 0, 100, 150 } }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.015 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 200 }
                        }
                    }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.075
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd"
                EmitterPosition: embed = ValueVector3 { constantValue: vec3 = { 0, 100, 150 } }

                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0.2 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 200 }
                        }
                    }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash_Add.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.05
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Slash_Dark"
                EmitterPosition: embed = ValueVector3 { constantValue: vec3 = { 0, 100, 150 } }

                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.015 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 220, 220 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 220, 220, 220 }
                        }
                    }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Q_Slash_Dark.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Cas"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw_Max" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Rengar_Q_Buf_Blade_Child"
                        }
                    }
                }
                emitterName: string = "Blue_Flames_Parent"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -5
                                        90
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        -20
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 1, 1 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0 }
                }
                pass: i16 = 40
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Blade_Mesh_Flame"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Claw_Flame.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3333, 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec4] = {
                            { 0.3333, 1, 1, 0 }
                            { 0.3333, 1, 1, 1 }
                            { 0.3333, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 30
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.05, 1.05, 1.05 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_EmBuf_Highlight.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5001
                                    0.5002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -0.5
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5001
                                    0.5002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -0.4
                                    0.4
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "powerFlareBurst"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3137, 0.851, 1, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.3137, 0.851, 1, 0.8 }
                            { 0.3137, 0.851, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/FlareBlue.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "powerFlare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4, 0.7412, 1, 0.498 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 0.4, 0.7412, 1, 0 }
                            { 0.4, 0.7412, 1, 0.498 }
                            { 0.4, 0.7412, 1, 0.498 }
                            { 0.4, 0.7412, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/FlareBlue.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "cross1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 30, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0196, 0.0392, 0.1373, 0.5 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.9
                            1
                        }
                        values: list[vec4] = {
                            { 0.0196, 0.0392, 0.1373, 0 }
                            { 0.0196, 0.0392, 0.1373, 0.5 }
                            { 0.0196, 0.0392, 0.1373, 0.5 }
                            { 0.0196, 0.0392, 0.1373, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 120, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/Items/Item_HextechRevolver_Cyan_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "cross2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 30, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0196, 0.0392, 0.1373, 0.5 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.9
                            1
                        }
                        values: list[vec4] = {
                            { 0.0196, 0.0392, 0.1373, 0 }
                            { 0.0196, 0.0392, 0.1373, 0.5 }
                            { 0.0196, 0.0392, 0.1373, 0.5 }
                            { 0.0196, 0.0392, 0.1373, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 120, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/Items/Item_HextechRevolver_Cyan_Glow.tex"
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_Claw_Max"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarQ_OnCast"

        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw_Max"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas_Max_MyWay" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                isLocalOrientation: flag = true          # e-local-orient=1
                particleIsLocalOrientation: flag = false # p-local-orient=0
                isRotationEnabled: flag = true           # p-simpleorient=1
                emitterName: string = "Slash1"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 80 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_Rengar_Base_Q_Slash.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.9529, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.9529, 1, 1 }
                            { 0, 0.9529, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 200 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_Slash_New.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.8 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Particles/HA_PoroRay_Mult.dds"
                }
            }
            VfxEmitterDefinitionData {
                #timeBeforeFirstEmission: f32 = 0.135
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.2
                }
                lifetime: option[f32] = {
                    0.385
                }
                isSingleParticle: flag = true
                isLocalOrientation: flag = true          # e-local-orient=1
                particleIsLocalOrientation: flag = false # p-local-orient=0
                isRotationEnabled: flag = true           # p-simpleorient=1
                emitterName: string = "SlashBase"
                importance: u8 = 2
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 100, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin08/Particles/Rengar_Skin08_Z_WeaponTrail_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.7686, 1, 1 }
                            { 0, 0.5137, 1, 1 }
                        }
                    }
                }
                pass: i16 = 1
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 70 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin08/Particles/Rengar_Skin08_AA_Trail_00.tex"
                frameRate: f32 = 24
                numFrames: u16 = 5
                texDiv: vec2 = { 1, 5 }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Cas_Max_MyWay"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas_Max_MyWay"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    10.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Skin02"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_ShoutRing.tex"
            }
        }
        particleName: string = "Rengar_Skin02_W_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Tar"
    }
    "Characters/Rengar/Skins/Skin2/Particles/rengar_skin02_recall_start_sound" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_Black.tex"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_Black.tex"
            }
        }
        particleName: string = "rengar_skin02_recall_start_sound"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/rengar_skin02_recall_start_sound"
        flags: u16 = 164
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                particleLinger: option[f32] = {
                    10.4
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "SlashSkin2"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.2235, 0.3412, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.2235, 0.3412, 1, 1 }
                            { 0.2235, 0.3412, 1, 1 }
                            { 0.2235, 0.3412, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 90, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 180, 90, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 50, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_Slash_New.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.8 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.4 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "SlashAdd1"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.651, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.651, 1, 1 }
                            { 0, 0.651, 1, 1 }
                            { 0, 0.651, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 90, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 180, 90, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_Slash_New.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.8 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.4 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 80, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0196, 0.0392, 0.1373, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.0196, 0.0392, 0.1373, 1 }
                            { 0.0196, 0.0392, 0.1373, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 350, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/common_Kalista_Skin01_P_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.2
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "powerFlare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.4235, 0.6431, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.4235, 0.6431, 1, 1 }
                            { 0.4235, 0.6431, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_flareblue.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.3
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 2200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 2200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 10, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 10, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 100, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Max_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Max_Tar"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Leap_Grass" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.15
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Grass_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 300, 1000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.3
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 300, 1000 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 90, 40 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 90, 40 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 300, 300 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 22, 22 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 22, 22, 22 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_P_Leap_Grass.tex"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
        }
        particleName: string = "Rengar_Skin02_P_Leap_Grass"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Leap_Grass"
        SoundOnCreateDefault: string = "Play_sfx_Leap_RengarP_Leap_Grass"

    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target_Enhanced" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Smoke_heart"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.1137, 0.1137, 0.1137, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.4
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.1
                                0.4
                                1
                            }
                            values: list[f32] = {
                                0.8
                                0.4
                                1.6
                                2.8
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/common_test_texture_mult.tex"
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 0.7 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 0.7 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.05
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 1, 1, 1 }
                            { 3, 3, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_Heart.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.2, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_r_heart_mult.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "background_smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 120, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.349, 0.6863, 0.8549, 0.4667 }
                }
                pass: i16 = -11
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 200, 10 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_mult.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.1 }
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_alpha_circle.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.62, 0.91, 0.36 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.05
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.62, 0.91, 0 }
                            { 0, 0.62, 0.91, 0.36 }
                            { 0, 0.62, 0.91, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -6 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/3161color-hold.AprilFools2025.dds"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.4, 0.2 }
                }
            }
        }
        particleName: string = "Rengar_Skin02_R_Primary_Target_Enhanced"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target_Enhanced"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarR_buffactivateheartbeat"
        flags: u16 = 213
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Roar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    0.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Skin02"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 600, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_W_ShoutRing.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 2
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 475, 475, 475 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_W_Ring.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.6
                }
                particleLinger: option[f32] = {
                    10.6
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundRing"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_W_GroundRing_Geo.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.7, 0.7, 0.7, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.15
                            1
                        }
                        values: list[vec4] = {
                            { 0.7, 0.7, 0.7, 0 }
                            { 0.7, 0.7, 0.7, 1 }
                            { 0.7, 0.7, 0.7, 0 }
                        }
                    }
                }
                pass: i16 = 1
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.7, 0.5, 1.7 }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_W_GroundRing_Sub.dds"
                texDiv: vec2 = { 0.7, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1.8 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "ShellDistort"
                particleColorTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Rampdown_RGBA.dds"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                pass: i16 = 100
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.03999999910593033
                    distortionMode: u8 = 1
                    normalMapTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Distortion_NormalMap.dds"
                }
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Distortion.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 500
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.4
                                0.6
                                1
                            }
                            values: list[f32] = {
                                0
                                0.7
                                0.9
                                1
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    4.5
                }
                emitterName: string = "ArmorFX"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 2
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.043
                            0.089
                            0.172
                            0.355
                            0.592
                            0.788
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.1183 }
                            { 1, 1, 1, 0.86 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.8827 }
                            { 1, 1, 1, 0.5068 }
                            { 1, 1, 1, 0.1313 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.4929
                            0.9976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.1301, 1.1301, 1.1301 }
                            { 1.25, 1.25, 1.25 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Avatar.tex"
                particleColorTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_RGB.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    4.5
                }
                emitterName: string = "ArmorFX"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 2
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.043
                            0.089
                            0.172
                            0.355
                            0.592
                            0.788
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.1183 }
                            { 1, 1, 1, 0.86 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.8827 }
                            { 1, 1, 1, 0.5068 }
                            { 1, 1, 1, 0.1313 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.4929
                            0.9976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.1301, 1.1301, 1.1301 }
                            { 1.25, 1.25, 1.25 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_Avatar.tex"
                particleColorTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_RGB.dds"
            }
        }
        particleName: string = "Rengar_Skin02_W_Roar"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarWemp_OnCast"

        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Roar"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Blue_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -10, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.5176, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.35
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.5176, 1, 1 }
                            { 0, 0.5176, 1, 1 }
                            { 0, 0, 1, 0.2 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = -40
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                    -1.5
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 35, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 3, 1, 0 }
                            { 3.5, 3, 0 }
                            { 4, 6, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Flames_add_4x4.tex"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                emitterName: string = "Blue_Glow_Sub"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -10, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 2
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.75 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -50
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                    -1.5
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 25, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 3, 0, 0 }
                            { 4, 3, 0 }
                            { 5, 6, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Flames_sub_4x4.tex"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_Blade_Child"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Child"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Strike" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.07
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.07
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Swipe1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -50, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_mesh_swipes_02.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.5
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 2
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.3, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_swipe_tex.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -2.8, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.1 }
                }
                texDiv: vec2 = { 1, 1.5 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.17
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                particleLinger: option[f32] = {
                    10.4
                }
                lifetime: option[f32] = {
                    1.17
                }
                isSingleParticle: flag = true
                emitterName: string = "bottom_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 300 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.7255 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 260, 120, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_Q_ground_swipe.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.15
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.1
                }
                lifetime: option[f32] = {
                    1.15
                }
                isSingleParticle: flag = true
                emitterName: string = "Bright_glow"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 500 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 60, 300 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 0.6667, 1, 1, 0 }
                            { 0.1333, 0.1608, 0.6667, 0.8118 }
                            { 0.2196, 0.1294, 0.4039, 0.4745 }
                            { 0.2549, 0.149, 0.3294, 0 }
                        }
                    }
                }
                pass: i16 = 4
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 2, 0 }
                            { 2, 2, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Yorick_Base_R_Aura_self.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.07
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    0.9
                                }
                                keyValues: list[f32] = {
                                    0.1
                                    0.3
                                    0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.4
                        }
                    }
                }
                lifetime: option[f32] = {
                    1.07
                }
                isSingleParticle: flag = true
                emitterName: string = "mesh_Sparkles_right"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 3000 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 12 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 50, 20, 150 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 200 }
                }
                blendMode: u8 = 5
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.251 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.3647, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.15
                            1
                        }
                        values: list[vec3] = {
                            { 3, 3, 1 }
                            { 0.3, 2, 1 }
                            { 0.15, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Strike"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Strike"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA2_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashSkin02"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -150, 120, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 150, 185 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -150, 120, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 150, 190 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_WeaponTrail.tex"
                numFrames: u16 = 4
                startFrame: u16 = 1
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Rengar_Skin02_BA2_Cas"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA2_Cas"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Heal" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterName: string = "healspark"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 800, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1, 3 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, 25, 60 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.51
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        -0.5
                                        0.5
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.51
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        -0.5
                                        0.5
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 60, 25, 60 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Heal_Spark_RGBA.tex"
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.3
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0.1, 0.1, 0.1 }
                            { 0.3, 0.3, 0.3 }
                            { 1, 10, 1 }
                            { 0.3, 0.3, 0.3 }
                            { 0.1, 0.1, 0.1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Heal_Spark.tex"
            }
        }
        particleName: string = "Rengar_Skin02_W_Heal"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Heal"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    10.75
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "SlashSkin02"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = false
                doesCastShadow: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 90, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 180, 90, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 50, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1 }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_WeaponTrail.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 1 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    10.75
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "SlashAdd"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_WeaponTrail.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = false
                doesCastShadow: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 90, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 180, 90, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1 }
                }
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_WeaponTrail.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 1 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                }
            } 
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.15000000596046448
                }
                emitterName: string = "blood_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 1 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                particleColorTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Blood_RGBA.dds"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Blood.dds"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                birthScale: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            1
                        }
                    }
                }
                particleBind: vec2 = { 0, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 450
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.3
                }
                emitterLinger: option[f32] = {
                    -1
                }
                emitterName: string = "blood_02"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                particleColorTexture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Blood_RGBA.dds"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                texture: string = "assets/characters/rengar/skins/skin02/Rengar_Skin02_Z_Blood.dds"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                birthScale: embed = ValueVector3 {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            {10, 10, 10}
                            {10, 10, 10}
                            {10, 10, 10}
                        }
                    }
                    }
                    particleBind: vec2 = { 1, 1 }
            }
            
            
             # Darius Blood
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 600
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -3250, 0 }
                            }
                        }
                    }
                }
                emitterName: string = "blood_02"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 880, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 880, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            5
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 28, 28, 28 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 28, 28, 28 }
                            { 28, 28, 28 }
                            { 28, 28, 28 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/blurdrops.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                EmitterPosition: embed = ValueVector3 { constantValue: vec3 = { 0, 100, 0 } } # p-postoffset

                isSingleParticle: flag = true
                emitterName: string = "flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_color-hit-physical.tex"
                pass: i16 = 10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 150 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_HitEffect.tex"
            }

            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -3250, 0 }
                            }
                        }
                    }
                }
                emitterName: string = "blood"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 250, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/Darius_color-bloodfluid32.tex"
                blendMode: u8 = 3
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 20
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    20
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 4, 4, 4 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/Darius_webfluid32.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 600
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -3250, 0 }
                            }
                        }
                    }
                }
                emitterName: string = "blood_03"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 280, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 280, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            5
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 28, 28, 28 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 28, 28, 28 }
                            { 28, 28, 28 }
                            { 28, 28, 28 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/blurdrops.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    # dynamics: pointer = VfxAnimatedFloatVariableData {
                        # probabilityTables: list[pointer] = {
                            # VfxProbabilityTableData {
                                # keyTimes: list[f32] = {
                                    # 0
                                    # 1
                                # }
                                # keyValues: list[f32] = {
                                    # 0.5
                                    # 1
                                # }
                            # }
                        # }
                        # times: list[f32] = {
                            # 0
                        # }
                        # values: list[f32] = {
                            # 1
                        # }
                    # }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.15000000596046448
                }
                emitterName: string = "blood_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 600, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            25
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                particleColorTexture: string = "ASSETS/characters/rengar/skins/base/NewFXs/Rengar_Skin01_Z_Blood_RGBA.tex"
                blendMode: u8 = 1
                ParticlesShareRandomValue: bool = true
                #particleIsLocalOrientation: flag = false
                #isLocalOrientation: flag = false
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                #isDirectionOriented: flag = false
                texture: string = "ASSETS/characters/rengar/skins/base/NewFXs/Rengar_Skin01_Z_Blood.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 15
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.4
                                        1.2
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                15
                                15
                                15
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 450
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    # dynamics: pointer = VfxAnimatedFloatVariableData {
                        # probabilityTables: list[pointer] = {
                            # VfxProbabilityTableData {
                                # keyTimes: list[f32] = {
                                    # 0
                                    # 1
                                # }
                                # keyValues: list[f32] = {
                                    # 0.5
                                    # 0.7
                                # }
                            # }
                        # }
                        # times: list[f32] = {
                            # 0
                        # }
                        # values: list[f32] = {
                            # 1
                        # }
                    # }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.3
                }
                emitterLinger: option[f32] = {
                    -1
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 500, 0, 500 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 500, 0, 500 }
                        }
                    }
                }
                emitterName: string = "blood_02"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 90, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 180, 90, -90 }
                        }
                    }
                }
                
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                }
                particleColorTexture: string = "ASSETS/characters/rengar/skins/base/NewFXs/Rengar_Skin01_Z_Blood_RGBA.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                texture: string = "ASSETS/characters/rengar/skins/base/NewFXs/Rengar_Skin01_Z_Blood.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 15
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.4
                                        1.2
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                15
                                15
                                15
                            }
                        }
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
            
            
        }
        particleName: string = "Rengar_Skin02_Q_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Tar"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "eyes"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.4353 }
                        }
                    }
                }
                pass: i16 = 100
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_tar_vision_eye.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "dark_eyes_pulse"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 26, 26, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 26, 26, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 0.1686, 0.0706, 0.2392, 1 }
                            { 0.0588, 0.0588, 0.1294, 0.5059 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 90
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_tar_vision_eye_pulse.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "yellow_eye_glow_pulse"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.8824, 0.7176, 0 }
                        }
                    }
                }
                pass: i16 = 102
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 65, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.8, 1, 1 }
                            { 1.2, 1.4, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_tar_vision_eye_glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "yellow_eye_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 124, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0706, 0.102, 0.2392, 0.7137 }
                }
                pass: i16 = 90
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 100, 1 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_R_tar_vision_eye_glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                emitterName: string = "Smoke_AE"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.4
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1000, 200, 1000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1000, 200, 1000 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 2, 13 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -50
                                    50
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -50
                                    50
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 50, 1 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.1137, 0.1137, 0.1137, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.1
                                0.4
                                1
                            }
                            values: list[f32] = {
                                1
                                0.5
                                1
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionSliceWidth: f32 = 10
                    erosionMapName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/common_test_texture_mult.tex"
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -60
                                    60
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 50, 0.7 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 50, 0.7 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 4, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_R_smoke_dust.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.3
                }
                emitterName: string = "wisp"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -30, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.3333, 0.498, 0 }
                            { 0, 0.4784, 0.702, 1 }
                            { 0, 0, 0.2314, 0 }
                        }
                    }
                }
                pass: i16 = -500
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, -230, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9
                                    1
                                }
                                keyValues: list[f32] = {
                                    6
                                    10
                                    13
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, -230, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec3] = {
                            { 0.6, 2, 1 }
                            { 1, 2, 1 }
                            { 1.2, 2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_skin02_R_glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "groundshadow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -70, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0078, 0.1176, 0.2392, 0.549 }
                }
                pass: i16 = -11
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 120, 10 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_alpha_circle.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                particleLinger: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "wisp1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.3882, 1, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.6667, 0.3333, 0, 0 }
                        }
                    }
                }
                pass: i16 = 200
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 90, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec3] = {
                            { 2, 0.6, 1 }
                            { 2, 1, 1 }
                            { 2, 1.2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Talon_base_w_mis_02_spark.tex"
            }
        }
        particleName: string = "Rengar_Skin02_R_Primary_Target"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target"
        flags: u16 = 197
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    10.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Skin02"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_ShoutRing.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 32
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.2
                }
                lifetime: option[f32] = {
                    0.2
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "Zap"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 2, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        30
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 2, 0 }
                            }
                        }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveRay {}
                particleColorTexture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Z_RGB.tex"
                blendMode: u8 = 2
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 65, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 4, 3, 0 }
                            { 0, 5.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_W_Barbs.tex"
            }
        }
        particleName: string = "Rengar_Skin02_W_Max_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Tar"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Rengar_Q_Buf_Blade_Child"
                        }
                    }
                }
                emitterName: string = "Blue_Flames_Parent"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        60
                                        130
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 1, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                pass: i16 = -40
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Blade_Mesh_Flame_Dark1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 75, -5.5 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 20
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Blade_Flame.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.2941, 0.2941, 0.2941, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec4] = {
                            { 0.2941, 0.2941, 0.2941, 0 }
                            { 0.2941, 0.2941, 0.2941, 0.8 }
                            { 0.2941, 0.2941, 0.2941, 0 }
                        }
                    }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                # birthScale0: embed = ValueVector3 {
                    # constantValue: vec3 = { 1.5, 1.5, 1.5 }
                # }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_Q_Buf_Blade_Flame_2x2.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.15, 0.25 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.15, 0.25 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "powerFlareBurst"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3137, 0.851, 1, 0.8 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.3137, 0.851, 1, 0.8 }
                            { 0.3137, 0.851, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/common_flareblue.tex"
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_Blade"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Max" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "ShadowWispsVert"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.75, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -0.75, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.8
                            1
                        }
                        values: list[f32] = {
                            1
                            0.6
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 5, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 2
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -50
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 75, 75, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_shadowwisps_sub_4x4.tex"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "ShadowWispsAdd"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.75, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -0.75, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.8
                            1
                        }
                        values: list[f32] = {
                            1
                            0.6
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 5, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -30
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 75, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 75, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Skin02/Particles/Rengar_Skin02_shadowwisps_add_4x4.tex"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
        }
        particleName: string = "Rengar_Skin02_P_Buf_Max"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Max"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarPEmp_buffactivate"
    }
    "Characters/Rengar/Skins/Skin2/Particles/Rengar_Base_R_LeapMatOverride" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    1.4
                }
                isSingleParticle: flag = true
                emitterName: string = "on_cast"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                # color: embed = ValueColor {
                    # constantValue: vec4 = { 1, 1, 1, 0 }
                # }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                BlendMode: u8 = 1
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.01, 1.01, 1.01 }
                    # dynamics: pointer = VfxAnimatedVector3fVariableData {
                        # times: list[f32] = {
                            # 0
                            # 1
                        # }
                        # values: list[vec3] = {
                            # { 1, 1.03, 1.03 }
                            # { 1.1, 1.03, 1.03 }
                        # }
                    # }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/skin02/rengar_skin02_tx_cm.tex"
            }
        }
        particleName: string = "Rengar_Skin02_R_Leap"
        particlePath: string = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Base_R_LeapMatOverride"
    }
    
    "Characters/Rengar/Skins/Skin2/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Rengar_BA1_Cas" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA1_Cas"
            "Rengar_BA2_Cas" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA2_Cas"
            "Rengar_BA3_Cas" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_BA3_Cas"
            "Rengar_BA_tar_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_01"
            "Rengar_BA_tar_crit_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_crit_01"
            "Rengar_C_Cas" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_C_Cas"
            "Rengar_E_Max_Mis" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Mis"
            "Rengar_E_Max_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Max_Tar"
            "Rengar_E_Mis" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Mis"
            "Rengar_E_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_E_Tar"
            "Rengar_P_Buf_Dash_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Dash_01"
            "Rengar_P_Buf_Enhanced_Ring" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Enhanced_Ring"
            "Rengar_P_Leap_Grass" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Leap_Grass"
            "Rengar_P_Leap_tar_crit_sound" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_tar_crit_sound"
            "Rengar_P_Leap_tar_sound" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_tar_sound"
            "Rengar_Q_AS_Buf" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_AS_Buf"
            "Rengar_Q_Buf_Blade" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade"
             "Rengar_Q_Buf_Blade_Max" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Max"
            "Rengar_Q_Buf_Claw" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw"
            "Rengar_Q_Buf_Claw_Max" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Claw_Max"
            "Rengar_Q_Cas" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas"
            "Rengar_Q_Cas_Max_MyWay" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Cas_Max_MyWay"
            "Rengar_Q_Max_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Max_Tar"
            "Rengar_Q_Strike" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Strike"
            "Rengar_Q_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Tar"
            "Rengar_R_Armor_shred_tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Armor_shred_tar"
            "Rengar_R_Buf" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Buf"
            "Rengar_R_Primary_Target" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target"
            "Rengar_R_Primary_Target_Enhanced" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Primary_Target_Enhanced"
            "Rengar_R_Secondary_Target" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_R_Secondary_Target"
            "Rengar_R_Secondary_Target_Sound_Off" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_Off"
            "Rengar_R_Secondary_Target_Sound_On" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_On"
            "Rengar_W_Emp_Buf2" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Emp_Buf2"
            "Rengar_W_Heal" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Heal"
            "Rengar_W_Max_Buf" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Buf"
            "Rengar_W_Max_Roar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Roar"
            "Rengar_W_Max_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Max_Tar"
            "Rengar_W_Roar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Roar"
            "Rengar_W_Tar" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_W_Tar"
            "rengar_emote_dance_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_dance_sound"
            "rengar_emote_death_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_death_sound"
            "rengar_emote_joke_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_joke_sound"
            "rengar_emote_laugh_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_laugh_sound"
            "rengar_emote_taunt_sound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/rengar_emote_taunt_sound"
            "Rengar_LeapSound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_LeapSound"
            "Rengar_VO_Seen_BV2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_VO_Seen"
            "Rengar_P_Buf_Max" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_P_Buf_Max"
            0xcdc6293f = 0xa60f0d10
            "Rengar_Q_Buf_Blade_Child" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Skin02_Q_Buf_Blade_Child"
            0xc0b74aaf = "Characters/Rengar/Skins/Skin2/Particles/rengar_skin02_recall_start_sound"
            
            "Rengar_RLeap_Override" = "Characters/Rengar/Skins/Skin2/Particles/Rengar_Base_R_LeapMatOverride"
            
            "LPF" = "Characters/Rengar/Skins/Skin1/Particles/LPF"

        }
    }
}
