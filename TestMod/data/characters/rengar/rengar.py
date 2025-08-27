#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Spells/RengarEEmpAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp"
            "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmpMis"
        }
        mName: string = "RengarEEmpAbility"
    }
    "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmpMis" = SpellObject {
        ObjectName: string = "RengarEEmpMis"
        mScriptName: string = "RengarEEmpMis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarE"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        50
                        100
                        150
                        200
                        250
                        300
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        20
                        20
                        20
                        20
                        20
                        20
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        55
                        60
                        65
                        70
                        75
                        80
                        85
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.7
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E_Emp.dds"
            }
            mCastTime: f32 = 0.25
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.875
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                9
                9
                9
                9
                9
                9
                9
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 70
                movementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "head"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1500
                }
                heightSolver: pointer = BlendedLinearHeightSolver {}
                verticalFacing: pointer = VerticalFacingFaceTarget {}
                behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mMissileEffectKey: hash = "Rengar_E_Max_Mis"
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
    }
    "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp" = SpellObject {
        ObjectName: string = "RengarEEmp"
        mScriptName: string = "RengarEEmp"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarE"
            mSpellTags: list[string] = {
                "Trait_ImmobilizingCCSpell"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        50
                        100
                        150
                        200
                        250
                        300
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        15
                        30
                        45
                        60
                        75
                        90
                        105
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.8
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E_Emp.dds"
            }
            mCastTime: f32 = 0.25
            cooldownTime: list[f32] = {
                0.4
                0.4
                0.4
                0.4
                0.4
                0.4
                0.4
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.875
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                10
                10
                10
                10
                10
                10
                10
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarEAbility/RengarE"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarEEmp"
        }
    }
    "Characters/Rengar/Spells/RengarRAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarRAbility/RengarR"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarRAbility/RengarR"
        }
        mLifetimeManuallyManaged: bool = true
        mName: string = "RengarRAbility"
        mType: u8 = 2
        AbilityTraits: u32 = 128
    }
    "Characters/Rengar/Spells/RengarQAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            "Characters/Rengar/Spells/RengarQAbility/RengarQAttack"
            "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
            "Characters/Rengar/Spells/RengarQAbility/RengarQEmpAttack"
            "Characters/Rengar/Spells/RengarQAbility/RengarQEmpASBuff"
        }
        mName: string = "RengarQAbility"
    }
    0x254b0092 = SpellObject {
        ObjectName: string = "RengarHatredReward"
        mScriptName: string = "RengarHatredReward"
        mSpell: pointer = SpellDataResource {
            ImgIconPath: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntVictoryR"
        }
    }
    0x2aa33976 = SpellObject {
        ObjectName: string = "RengarHatredWins"
        mScriptName: string = "RengarHatredWins"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntVictoryR"
        }
    }
    "Characters/Rengar/Spells/Rengar9StackBuff" = SpellObject {
        ObjectName: string = "Rengar9StackBuff"
        mScriptName: string = "Rengar9StackBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_Rengar9StackBuff"
        }
    }
    "Characters/Rengar/Spells/RengarRShred" = SpellObject {
        ObjectName: string = "RengarRShred"
        mScriptName: string = "RengarRShred"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarRShred"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff5" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff5"
        mScriptName: string = "RengarPassiveBonetoothBuff5"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff5"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff4" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff4"
        mScriptName: string = "RengarPassiveBonetoothBuff4"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff4"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff3" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff3"
        mScriptName: string = "RengarPassiveBonetoothBuff3"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff3"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff2" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff2"
        mScriptName: string = "RengarPassiveBonetoothBuff2"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff2"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff1" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff1"
        mScriptName: string = "RengarPassiveBonetoothBuff1"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff1"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarQSound" = SpellObject {
        ObjectName: string = "RengarQSound"
        mScriptName: string = "RengarQSound"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                ""
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = 0.1833
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                2000
                                2000
                                2000
                                2000
                                2000
                                2000
                            }
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionRange {
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1100
                                1100
                                1100
                                1100
                                1100
                                1100
                            }
                            mValueType: u32 = 1
                        }
                        textureOverrideName: string = "ASSETS/Spells/Textures/CircularRangeIndicator_Dark.dds"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
    }
    "Characters/Rengar/Spells/RengarRBuff" = SpellObject {
        ObjectName: string = "RengarRBuff"
        mScriptName: string = "RengarRBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmpASBuff"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBuff" = SpellObject {
        ObjectName: string = "RengarPassiveBuff"
        mScriptName: string = "RengarPassiveBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBuff"
        }
    }
    "Characters/Rengar/Spells/RengarWAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarWAbility/RengarW"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarWAbility/RengarW"
            "Characters/Rengar/Spells/RengarWAbility/RengarWEmp"
        }
        mName: string = "RengarWAbility"
    }
    "Characters/Rengar/Spells/RengarWAbility/RengarWEmp" = SpellObject {
        ObjectName: string = "RengarWEmp"
        mScriptName: string = "RengarWEmp"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarW"
            mSpellTags: list[string] = {
                "SpecialCase_StasisLocked"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        50
                        80
                        110
                        140
                        170
                        200
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.7
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_W_Emp.dds"
            }
            cooldownTime: list[f32] = {
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                22
                20
                18
                16
                14
                12
                12
            }
            mAmmoCountHiddenInUI: bool = true
            cannotBeSuppressed: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 7.5
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarWAbility/RengarW"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarWEmp"
        }
    }
    "Characters/Rengar/Spells/RengarWAbility/RengarW" = SpellObject {
        ObjectName: string = "RengarW"
        mScriptName: string = "RengarW"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarW"
            mSpellTags: list[string] = {
                "SpecialCase_StasisLocked"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {}
                SpellEffectAmount {
                    value: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "BaseDamage"
                    mValues: list[f32] = {
                        20
                        50
                        80
                        110
                        140
                        170
                        200
                    }
                }
                SpellDataValue {
                    mName: string = "DamagePercentageHealed"
                    mValues: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellDataValue {
                    mName: string = "APRatio"
                    mValues: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
                SpellDataValue {
                    mName: string = "EmpoweredAPRatio"
                    mValues: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "BaseDamage"
                            mValues: list[f32] = {
                                20
                                60
                                100
                                140
                                180
                                220
                                260
                            }
                        }
                        SpellDataValue {
                            mName: string = "DamagePercentageHealed"
                            mValues: list[f32] = {
                                60
                                60
                                60
                                60
                                60
                                60
                                60
                            }
                        }
                        SpellDataValue {
                            mName: string = "APRatio"
                            mValues: list[f32] = {
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                            }
                        }
                        SpellDataValue {
                            mName: string = "EmpoweredAPRatio"
                            mValues: list[f32] = {
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "BonusMonsterDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelInterpolationCalculationPart {
                            mStartValue: f32 = 65
                            mEndValue: f32 = 130
                        }
                    }
                }
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mDataValue: hash = "APRatio"
                        }
                    }
                }
                "TotalDamageEmpowered" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelFormulaCalculationPart {
                            mValues: list[f32] = {
                                0
                                50
                                60
                                70
                                80
                                90
                                100
                                110
                                120
                                130
                                140
                                150
                                160
                                170
                                180
                                190
                                200
                                210
                                220
                                230
                                240
                                250
                                260
                                270
                                280
                                290
                                300
                                310
                                320
                                330
                                340
                            }
                        }
                        StatByNamedDataValueCalculationPart {
                            mDataValue: hash = "EmpoweredAPRatio"
                        }
                    }
                }
            }
            mCoefficient: f32 = 0.8
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_W.dds"
            }
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                22
                16
                14.5
                13
                11.5
                10
                10
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 7.5
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarW"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarW_Name"
                        "keySummary" = "Spell_RengarW_Summary"
                        "keyTooltip" = "Spell_RengarW_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarW_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "BaseDamage"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "AmmoRechargeTime"
                                    nameOverride: string = "Spell_ListType_Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 1
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 8
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 2
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 2097152
                    EffectCalculation: pointer = GameCalculation {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQ" = SpellObject {
        ObjectName: string = "RengarQ"
        mScriptName: string = "RengarQ"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "Trait_AttackReset"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        30
                        30
                        60
                        90
                        120
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        105
                        110
                        115
                        120
                        120
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        40
                        40
                        40
                        40
                        40
                        40
                        40
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.1
                        0.2
                        0.3
                        0.4
                        0.5
                        0.6
                        0.7
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "BaseDamage"
                    mValues: list[f32] = {
                        0
                        30
                        60
                        90
                        120
                        150
                        180
                    }
                }
                SpellDataValue {
                    mName: string = "BaseADRatio"
                    mValues: list[f32] = {
                        -0.0375
                        0
                        0.0375
                        0.075
                        0.1125
                        0.15
                        0.1875
                    }
                }
                SpellDataValue {
                    mName: string = "CritRatio"
                    mValues: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellDataValue {
                    mName: string = "EmpoweredADRatio"
                    mValues: list[f32] = {
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                    }
                }
                SpellDataValue {
                    mName: string = "CritScalingRatio"
                    mValues: list[f32] = {
                        0.75
                        0.75
                        0.75
                        0.75
                        0.75
                        0.75
                        0.75
                    }
                }
                SpellDataValue {
                    mName: string = "TotalEmpoweredADRatio"
                    mValues: list[f32] = {
                        1.3
                        1.3
                        1.3
                        1.3
                        1.3
                        1.3
                        1.3
                    }
                }
                SpellDataValue {
                    mName: string = "TotalADRatio"
                    mValues: list[f32] = {
                        0.9625
                        1
                        1.0375
                        1.075
                        1.1125
                        1.15
                        1.1875
                    }
                }
                SpellDataValue {
                    mName: string = "TowerMod"
                    mValues: list[f32] = {
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                        0.4
                    }
                }
                SpellDataValue {
                    mName: string = "QCritDamageScalar"
                    mValues: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "BaseDamage"
                            mValues: list[f32] = {
                                0
                                40
                                80
                                120
                                160
                                200
                                240
                            }
                        }
                        SpellDataValue {
                            mName: string = "BaseADRatio"
                            mValues: list[f32] = {
                                0
                                0.05
                                0.1
                                0.15
                                0.2
                                0.25
                                0.3
                            }
                        }
                        SpellDataValue {
                            mName: string = "EmpoweredADRatio"
                            mValues: list[f32] = {
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                            }
                        }
                        SpellDataValue {
                            mName: string = "TotalADRatio"
                            mValues: list[f32] = {
                                1
                                1.05
                                1.1
                                1.15
                                1.2
                                1.25
                                1.3
                            }
                        }
                        SpellDataValue {
                            mName: string = "TotalEmpoweredADRatio"
                            mValues: list[f32] = {
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                            }
                        }
                    }
                }
                "ARAM" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "BaseADRatio"
                            mValues: list[f32] = {
                                0.0625
                                0.1
                                0.1375
                                0.175
                                0.2125
                                0.25
                                0.2875
                            }
                        }
                        SpellDataValue {
                            mName: string = "EmpoweredADRatio"
                            mValues: list[f32] = {
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                            }
                        }
                        SpellDataValue {
                            mName: string = "TotalADRatio"
                            mValues: list[f32] = {
                                1.0625
                                1.1
                                1.1375
                                1.175
                                1.2125
                                1.25
                                1.2875
                            }
                        }
                        SpellDataValue {
                            mName: string = "TotalEmpoweredADRatio"
                            mValues: list[f32] = {
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "EmpoweredQdamageTT" = GameCalculation {
                    tooltipOnly: bool = true
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 30
                            mInitialBonusPerLevel: f32 = 15
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 9
                                    mBonusPerLevelAtAndAfter: f32 = 10
                                }
                            }
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "TotalEmpoweredADRatio"
                        }
                    }
                }
                "EmpoweredQAS" = GameCalculation {
                    mMultiplier: pointer = NumberCalculationPart {
                        mNumber: f32 = 0.01
                    }
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 50
                            mInitialBonusPerLevel: f32 = 3
                        }
                    }
                    mDisplayAsPercent: bool = true
                }
                "TotalDamageTT" = GameCalculation {
                    tooltipOnly: bool = true
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "TotalADRatio"
                        }
                    }
                }
                0xc285d829 = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 30
                            mInitialBonusPerLevel: f32 = 15
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 9
                                    mBonusPerLevelAtAndAfter: f32 = 10
                                }
                            }
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "EmpoweredADRatio"
                        }
                    }
                }
                0xe29bb654 = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "BaseADRatio"
                        }
                    }
                }
                "CritDamageScalar" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 9
                            mDataValue: hash = "CritScalingRatio"
                        }
                    }
                    mDisplayAsPercent: bool = true
                }
            }
            mCoefficient: f32 = 1
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQ.dds"
            }
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                6
                6
                5.5
                5
                4.5
                4
                3.5
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarQ"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarQ_Name"
                        "keySummary" = "Spell_RengarQ_Summary"
                        "keyTooltip" = "Spell_RengarQ_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtended" = "Spell_RengarQ_TooltipExtended"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "Effect%dAmount"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "Effect%dAmount"
                                    typeIndex: i32 = 2
                                    nameOverride: string = "Spell_ListType_TotalADRatio"
                                    Style: u32 = 1
                                }
                                TooltipInstanceListElement {
                                    type: string = "AmmoRechargeTime"
                                    nameOverride: string = "Spell_ListType_Cooldown"
                                }
                            }
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamageTT"
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmpASBuff" = SpellObject {
        ObjectName: string = "RengarQEmpASBuff"
        mScriptName: string = "RengarQEmpASBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmpASBuff"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmpAttack" = SpellObject {
        ObjectName: string = "RengarQEmpAttack"
        mScriptName: string = "RengarQEmpAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        10
                        30
                        50
                        70
                        90
                        110
                        130
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        350
                        350
                        350
                        350
                        350
                        350
                        350
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        90
                        90
                        90
                        90
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.1
                        0.2
                        0.3
                        0.4
                        0.5
                        0.6
                        0.7
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.5
            mCoefficient2: f32 = 0.9
            mAnimationName: string = "Attack4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQEmp.dds"
            }
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mApplyAttackDamage: bool = true
            mApplyAttackEffect: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {
            }
            mConsideredAsAutoAttack: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8.5
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            mHitEffectName: string = "GlobalHit_Yellow_tar.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.dds"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                625
                                625
                                625
                                625
                                625
                                625
                            }
                            mValueType: u32 = 2
                        }
                        textureBaseOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileBase_Dark.dds"
                        textureTargetOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileTarget_Dark.dds"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQAttack" = SpellObject {
        ObjectName: string = "RengarQAttack"
        mScriptName: string = "RengarQAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        10
                        30
                        50
                        70
                        90
                        110
                        130
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        350
                        350
                        350
                        350
                        350
                        350
                        350
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        90
                        90
                        90
                        90
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.1
                        0.2
                        0.3
                        0.4
                        0.5
                        0.6
                        0.7
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.5
            mCoefficient2: f32 = 0.9
            mAnimationName: string = "Attack4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQ.dds"
            }
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mApplyAttackDamage: bool = true
            mApplyAttackEffect: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {
            }
            mConsideredAsAutoAttack: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8.5
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            mHitEffectName: string = "GlobalHit_Yellow_tar.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.dds"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                625
                                625
                                625
                                625
                                625
                                625
                            }
                            mValueType: u32 = 2
                        }
                        textureBaseOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileBase_Dark.dds"
                        textureTargetOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileTarget_Dark.dds"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmp" = SpellObject {
        ObjectName: string = "RengarQEmp"
        mScriptName: string = "RengarQEmp"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
                "Trait_AttackReset"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        30
                        30
                        60
                        90
                        120
                        150
                        180
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        105
                        110
                        115
                        120
                        125
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        90
                        90
                        90
                        90
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        40
                        40
                        40
                        40
                        40
                        40
                        40
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.2
                        0.3
                        0.4
                        0.5
                        0.6
                        0.7
                        0.8
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1
            mCoefficient2: f32 = 1.4
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQEmp.dds"
            }
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -1
            delayTotalTimePercent: f32 = -1
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                6
                6
                5.5
                4
                4.5
                4
                3.5
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmp"
        }
    }
    0x62b7fb36 = SpellObject {
        ObjectName: string = "RengarHatredDefeat"
        mScriptName: string = "RengarHatredDefeat"
        mSpell: pointer = SpellDataResource {
            ImgIconPath: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntDefeatK"
        }
    }
    "Characters/Rengar/Spells/RengarOutOfCombat" = SpellObject {
        ObjectName: string = "RengarOutOfCombat"
        mScriptName: string = "RengarOutOfCombat"
    }
    0x77cee58a = SpellObject {
        ObjectName: string = "RengarHatredGoTime"
        mScriptName: string = "RengarHatredGoTime"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_VolibearHatredZilean"
        }
    }
    "Characters/Rengar/Spells/RengarEAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarEAbility/RengarE"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarEAbility/RengarE"
            "Characters/Rengar/Spells/RengarEAbility/RengarEMis"
        }
        mName: string = "RengarEAbility"
    }
    "Characters/Rengar/Spells/RengarEAbility/RengarE" = SpellObject {
        ObjectName: string = "RengarE"
        mScriptName: string = "RengarE"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarE"
            mSpellTags: list[string] = {
                "Trait_SwapsIntoImmobilizingCCSpell"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        10
                        55
                        100
                        145
                        190
                        235
                        280
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        15
                        30
                        45
                        60
                        75
                        90
                        105
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "RevealDuration"
                    mValues: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellDataValue {
                    mName: string = "BaseDamage"
                    mValues: list[f32] = {
                        10
                        55
                        100
                        145
                        190
                        235
                        280
                    }
                }
                SpellDataValue {
                    mName: string = "SlowAmount"
                    mValues: list[f32] = {
                        15
                        30
                        45
                        60
                        75
                        90
                        105
                    }
                }
                SpellDataValue {
                    mName: string = "BonusADRatio"
                    mValues: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "ARAM" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "BonusADRatio"
                            mValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mDataValue: hash = "BonusADRatio"
                        }
                    }
                }
                "TotalEmpoweredDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 50
                            mInitialBonusPerLevel: f32 = 15
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mDataValue: hash = "BonusADRatio"
                        }
                    }
                }
            }
            mCoefficient: f32 = 0.8
            mCoefficient2: f32 = 0.6
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E.dds"
            }
            mCastTime: f32 = 0.25
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.875
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                10
                10
                10
                10
                10
                10
                10
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarE"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarE_Name"
                        "keySummary" = "Spell_RengarE_Summary"
                        "keyTooltip" = "Spell_RengarE_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarE_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "BaseDamage"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "SlowAmount"
                                    typeIndex: i32 = 2
                                    nameOverride: string = "Spell_ListType_Slow"
                                    Style: u32 = 1
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 1
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 3
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 4096
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 3
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 32768
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NumberCalculationPart {
                                mNumber: f32 = 70
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2048
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8192
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarEAbility/RengarEMis" = SpellObject {
        ObjectName: string = "RengarEMis"
        mScriptName: string = "RengarEMis"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarE"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        50
                        100
                        150
                        200
                        250
                        300
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        5
                        10
                        15
                        20
                        25
                        30
                        35
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        15
                        30
                        45
                        60
                        75
                        90
                        105
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.7
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E.dds"
            }
            mCastTime: f32 = 0.25
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.875
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                9
                9
                9
                9
                9
                9
                9
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 70
                movementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "head"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1500
                }
                heightSolver: pointer = BlendedLinearHeightSolver {}
                verticalFacing: pointer = VerticalFacingFaceTarget {}
                behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mMissileEffectKey: hash = "Rengar_E_Mis"
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack" = SpellObject {
        ObjectName: string = "RengarBasicAttack"
        mScriptName: string = "RengarBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.1739
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothManager" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothManager"
        mScriptName: string = "RengarPassiveBonetoothManager"
    }
    "Characters/Rengar/Spells/RengarQ2" = SpellObject {
        ObjectName: string = "RengarQ2"
        mScriptName: string = "RengarQ2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        15
                        30
                        45
                        60
                        75
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        20
                        20
                        20
                        20
                        20
                        20
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        25
                        30
                        35
                        40
                        45
                        50
                        55
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        200
                        200
                        200
                        200
                        200
                        200
                        200
                    }
                }
            }
            mCoefficient: f32 = 0.6
            mCoefficient2: f32 = 0.4
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.7
            delayTotalTimePercent: f32 = -0.925
            mMaxAmmo: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mAmmoUsed: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.dds"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBuffDash" = SpellObject {
        ObjectName: string = "RengarPassiveBuffDash"
        mScriptName: string = "RengarPassiveBuffDash"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6831
            mAlternateName: string = "RengarPassiveBuffDash"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {
                    value: list[f32] = {
                        800
                        800
                        800
                        800
                        800
                        800
                        800
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Passive.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castConeDistance: f32 = 100
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBuffDashAADummy" = SpellObject {
        ObjectName: string = "RengarPassiveBuffDashAADummy"
        mScriptName: string = "RengarPassiveBuffDashAADummy"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 8191
            mAlternateName: string = "RengarPassiveBuffDash"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Passive.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff"
        mScriptName: string = "RengarPassiveBonetoothBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveEmpowered" = SpellObject {
        ObjectName: string = "RengarPassiveEmpowered"
        mScriptName: string = "RengarPassiveEmpowered"
    }
    0xa05f165c = SpellObject {
        ObjectName: string = "RengarRPassive"
        mScriptName: string = "RengarRPassive"
    }
    "Characters/Rengar/Spells/RengarRAbility/RengarR" = SpellObject {
        ObjectName: string = "RengarR"
        mScriptName: string = "RengarR"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                "Trait_Ultimate"
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "StealthDuration"
                    mValues: list[f32] = {
                        8
                        12
                        16
                        20
                        24
                        28
                        32
                    }
                }
                SpellDataValue {
                    mName: string = "EnemyDetectionRange"
                    mValues: list[f32] = {
                        1600
                        1600
                        1600
                        1600
                        1600
                        1600
                        1600
                    }
                }
                SpellDataValue {
                    mName: string = "SelfVisionRange"
                    mValues: list[f32] = {
                        2000
                        2500
                        3000
                        3500
                        4000
                        4500
                        5000
                    }
                }
                SpellDataValue {
                    mName: string = "SelfRevealRange"
                    mValues: list[f32] = {
                        750
                        750
                        750
                        750
                        750
                        750
                        750
                    }
                }
                SpellDataValue {
                    mName: string = "StealthMS"
                    mValues: list[f32] = {
                        30
                        40
                        50
                        60
                        70
                        80
                        90
                    }
                }
                SpellDataValue {
                    mName: string = "FadeTime"
                    mValues: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellDataValue {
                    mName: string = "ArmorShred"
                    mValues: list[f32] = {
                        10
                        15
                        20
                        25
                        30
                        35
                        40
                    }
                }
                SpellDataValue {
                    mName: string = "ArmorShredDuration"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    mName: string = "LeapRange"
                    mValues: list[f32] = {
                        725
                        725
                        725
                        725
                        725
                        725
                        725
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "StealthMS"
                            mValues: list[f32] = {
                                30
                                50
                                70
                                90
                                110
                                130
                                150
                            }
                        }
                    }
                }
            }
            0xf9c2333e: map[hash,embed] = {
                "cherry" = SpellEffectAmount {
                    value: list[f32] = {
                        80
                        80
                        70
                        60
                        50
                        40
                        30
                    }
                }
                "ARAM" = SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        80
                        70
                        70
                        70
                        70
                    }
                }
                0xa110bc47 = SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        75
                        60
                        60
                        60
                        60
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "BonusDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mCoefficient: f32 = 1
                        }
                    }
                }
            }
            mCoefficient: f32 = 0.5
            mCoefficient2: f32 = 0.6
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
            }
            cooldownTime: list[f32] = {
                100
                100
                90
                80
                80
                80
                80
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = 0.1833
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                2500
                2500
                3000
                3500
                2500
                2500
                2500
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarR"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarR_Name"
                        "keySummary" = "Spell_RengarR_Summary"
                        "keyTooltip" = "Spell_RengarR_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarR_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 3
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "ArmorShred"
                                    typeIndex: i32 = 8
                                    nameOverride: string = "Spell_ListType_ArmorReduction"
                                }
                                TooltipInstanceListElement {
                                    type: string = "StealthDuration"
                                    typeIndex: i32 = 2
                                    nameOverride: string = "Spell_ListType_Duration"
                                }
                                TooltipInstanceListElement {
                                    type: string = "StealthMS"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_MovementSpeed"
                                    Style: u32 = 1
                                }
                                TooltipInstanceListElement {
                                    type: string = "SelfVisionRange"
                                    typeIndex: i32 = 9
                                    nameOverride: string = "Spell_ListType_RengarTrackingRange"
                                }
                                TooltipInstanceListElement {
                                    type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "BonusDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 2
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "StealthMS"
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 1024
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "StealthDuration"
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarNewPassiveBuffDash" = SpellObject {
        ObjectName: string = "RengarNewPassiveBuffDash"
        mScriptName: string = "RengarNewPassiveBuffDash"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 8191
            mAlternateName: string = "RengarNewPassiveBuffDash"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Passive.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarInCombat" = SpellObject {
        ObjectName: string = "RengarInCombat"
        mScriptName: string = "RengarInCombat"
    }
    "Characters/Rengar/Spells/RengarPassiveEmpoweredMS" = SpellObject {
        ObjectName: string = "RengarPassiveEmpoweredMS"
        mScriptName: string = "RengarPassiveEmpoweredMS"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveEmpoweredMS"
        }
    }
    "Characters/Rengar/Spells/RengarQEmpowered" = SpellObject {
        ObjectName: string = "RengarQEmpowered"
        mScriptName: string = "RengarQEmpowered"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        20
                        40
                        60
                        80
                        100
                        120
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        20
                        20
                        20
                        20
                        20
                        20
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        25
                        30
                        35
                        40
                        45
                        50
                        55
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        200
                        200
                        200
                        200
                        200
                        200
                        200
                    }
                }
            }
            mCoefficient: f32 = 0.6
            mCoefficient2: f32 = 0.4
            mAnimationName: string = "Spell1a"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            mCastTime: f32 = 0.2
            cooldownTime: list[f32] = {
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.875
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            alwaysSnapFacing: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.dds"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarRSpeed" = SpellObject {
        ObjectName: string = "RengarRSpeed"
        mScriptName: string = "RengarRSpeed"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        15
                        20
                        25
                        30
                        0
                        0
                        5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        5
                        5
                        5
                        5
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        1000
                        2000
                        3000
                        4000
                        0
                        0
                        1000
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        25
                        30
                        35
                        0
                        0
                        5
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        15
                        15
                        15
                        15
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1"
            cooldownTime: list[f32] = {
                175
                140
                105
                70
                11
                11
                11
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = 0.1833
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                1000
                2000
                3000
                4000
                2000
                2000
                3000
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarRSpeed"
        }
    }
    "Characters/Rengar/Spells/RengarNewPassive" = SpellObject {
        ObjectName: string = "RengarNewPassive"
        mScriptName: string = "RengarNewPassive"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarNewPassive"
        }
    }
    "Characters/Rengar/Spells/RengarBushSpeedBonus" = SpellObject {
        ObjectName: string = "RengarBushSpeedBonus"
        mScriptName: string = "RengarBushSpeedBonus"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarBushSpeedBonus"
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack3" = SpellObject {
        ObjectName: string = "RengarBasicAttack3"
        mScriptName: string = "RengarBasicAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Attack3"
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.1739
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack2" = SpellObject {
        ObjectName: string = "RengarBasicAttack2"
        mScriptName: string = "RengarBasicAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Attack2"
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.1739
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.4
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarQ2Emp" = SpellObject {
        ObjectName: string = "RengarQ2Emp"
        mScriptName: string = "RengarQ2Emp"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        0
                        15
                        30
                        45
                        60
                        75
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        20
                        20
                        20
                        20
                        20
                        20
                        20
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        25
                        30
                        35
                        40
                        45
                        50
                        55
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        200
                        200
                        200
                        200
                        200
                        200
                        200
                    }
                }
            }
            mCoefficient: f32 = 0.6
            mCoefficient2: f32 = 0.4
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q_Emp.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.7
            delayTotalTimePercent: f32 = -0.925
            mMaxAmmo: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mAmmoUsed: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.dds"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarFerocityManagerInCombat" = SpellObject {
        ObjectName: string = "RengarFerocityManagerInCombat"
        mScriptName: string = "RengarFerocityManagerInCombat"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarFerocityManagerInCombat"
        }
    }
    "Characters/Rengar/Spells/RengarRLeap" = SpellObject {
        ObjectName: string = "RengarRLeap"
        mScriptName: string = "RengarRLeap"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                "Trait_Ultimate"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        40
                        40
                        40
                        40
                        40
                        40
                        40
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        14
                        14
                        22
                        30
                        30
                        30
                        30
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        2000
                        2000
                        3000
                        4000
                        4000
                        4000
                        4000
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        750
                        750
                        750
                        750
                        750
                        750
                        750
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        725
                        725
                        725
                        725
                        725
                        725
                        725
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.1
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
            }
            cooldownTime: list[f32] = {
                130
                130
                100
                70
                70
                70
                70
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = 0.1833
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                2000
                2000
                3000
                4000
                4000
                4000
                4000
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Self {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuffKhazix" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuffKhazix"
        mScriptName: string = "RengarPassiveBonetoothBuffKhazix"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuffKhazix"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        }
        mName: string = "RengarPassiveAbility"
        mType: u8 = 3
    }
    "Characters/Rengar/Spells/RengarEFinalMAX" = SpellObject {
        ObjectName: string = "RengarEFinalMAX"
        mScriptName: string = "RengarEFinalMAX"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarE"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        25
                        70
                        115
                        160
                        205
                        250
                        295
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        13
                        12
                        11
                        10
                        9
                        8
                        7
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        55
                        60
                        65
                        70
                        75
                        80
                        85
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell3"
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 70
                movementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 20
                    mStartBoneName: string = "LHand"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1500
                }
                heightSolver: pointer = BlendedLinearHeightSolver {}
                verticalFacing: pointer = VerticalFacingFaceTarget {}
                behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            castFrame: f32 = 8.52
            missileSpeed: f32 = 1500
            mMissileEffectKey: hash = "Rengar_E_Max_Mis"
            mLineWidth: f32 = 70
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarCritAttack" = SpellObject {
        ObjectName: string = "RengarCritAttack"
        mScriptName: string = "RengarCritAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Crit"
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.1739
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.4
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_crit_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarQ2Sound" = SpellObject {
        ObjectName: string = "RengarQ2Sound"
        mScriptName: string = "RengarQ2Sound"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                ""
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            delayCastOffsetPercent: f32 = -0.5
            delayTotalTimePercent: f32 = 0.1833
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                2000
                                2000
                                2000
                                2000
                                2000
                                2000
                            }
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionRange {
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1100
                                1100
                                1100
                                1100
                                1100
                                1100
                            }
                            mValueType: u32 = 1
                        }
                        textureOverrideName: string = "ASSETS/Spells/Textures/CircularRangeIndicator_Dark.dds"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive" = SpellObject {
        ObjectName: string = "RengarPassive"
        mScriptName: string = "RengarPassive"
        mSpell: pointer = SpellDataResource {
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "MaxFerocity"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    mName: string = "InCombatTimer"
                    mValues: list[f32] = {
                        10
                        10
                        10
                        10
                        10
                        10
                        10
                    }
                }
                SpellDataValue {
                    mName: string = "InCombatTimerVisual"
                    mValues: list[f32] = {
                        10
                        10
                        10
                        10
                        10
                        10
                        10
                    }
                }
                SpellDataValue {
                    mName: string = "EmpoweredMSDuration"
                    mValues: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellDataValue {
                    mName: string = "RengarPassiveRangeIncrease"
                    mValues: list[f32] = {
                        620
                        620
                        620
                        620
                        620
                        620
                        620
                    }
                }
                SpellDataValue {
                    mName: string = "LeapFerocityGeneration"
                    mValues: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "EmpoweredMS" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 0.3
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 7
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 13
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 19
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 25
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                            }
                        }
                    }
                    mDisplayAsPercent: bool = true
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_P.dds"
            }
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
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
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarPassive"
                    mFormat: link = 0x476ec0b8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarPassive_Name"
                        "keyTooltip" = "Spell_RengarPassive_Tooltip"
                        "keyTooltipExtended" = "Spell_RengarPassive_TooltipExtended"
                        "keySummary" = "Spell_RengarPassive_Summary"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassive"
        }
    }
    0x4f9cd28b = StatStoneSet {
        name: string = "stat_stone_set_name_1"
        catalogEntry: embed = catalogEntry {
            contentId: string = "5e16e630-e328-480e-857a-f4625eec5add"
            itemID: u32 = 66600094
        }
        statStones: list[link] = {
            0x176cfeb2
            0xf7ea7750
            0xd859dffb
        }
    }
    0x176cfeb2 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarRKills"
        catalogEntry: embed = catalogEntry {
            contentId: string = "ce658030-b956-47fd-b78b-c21a39ccb397"
            itemID: u32 = 3166
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarRKills"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x024e22b2
        Milestones: list[u64] = {
            6
            15
            30
            35
            45
            20
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarRKills"
    }
    0xd859dffb = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarCCWCancels"
        catalogEntry: embed = catalogEntry {
            contentId: string = "add97e64-dd42-4a99-b118-24befd1b17d5"
            itemID: u32 = 196
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarCCWCancels"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            7
            20
            35
            45
            55
            20
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarCCWCancels"
    }
    0xf7ea7750 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarQuickP"
        catalogEntry: embed = catalogEntry {
            contentId: string = "1c5890f6-8d0e-4f7b-839e-23fd9ac64267"
            itemID: u32 = 194
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarQuickP"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            1
            3
            6
            8
            9
            4
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarQuickP"
    }
    0x509cd41e = StatStoneSet {
        name: string = "stat_stone_set_name_2"
        catalogEntry: embed = catalogEntry {
            contentId: string = "6211bd8a-b2f1-4ff8-92de-980869235029"
            itemID: u32 = 66600467
        }
        statStones: list[link] = {
            0x756274ee
            0xc1e0cd13
            0xdb172aa8
        }
    }
    0xdcc9c9f3 = StatStoneSet {
        name: string = "stat_stone_set_name_starter"
        catalogEntry: embed = catalogEntry {
            contentId: string = "18696f82-140d-44aa-a421-da317e5464ae"
            itemID: u32 = 66600261
        }
        statStones: list[link] = {
            0xb164e242
            0x6b2e866b
            0x6f223a0a
        }
    }
    0x6b2e866b = StatStoneData {
        mNameTraKey: string = "stat_stone_name_takedowns"
        catalogEntry: embed = catalogEntry {
            contentId: string = "165b4624-1bc7-4798-98c5-0b529872157e"
            itemID: u32 = 125721
        }
        mDescriptionTraKey: string = "stat_stone_description_Takedowns"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 7
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 81
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        MinionsAreValid: bool = false
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 220
            }
        }
        category: link = 0x5c6e96a2
        Milestones: list[u64] = {
            25
            65
            125
            150
            185
            75
        }
        stoneName: string = "RengarTakedowns"
    }
    0x6f223a0a = StatStoneData {
        mNameTraKey: string = "stat_stone_name_structures_destroyed"
        catalogEntry: embed = catalogEntry {
            contentId: string = "6fffce2d-09d2-4204-9352-aa445a35d376"
            itemID: u32 = 125722
        }
        mDescriptionTraKey: string = "stat_stone_description_StructuresDestroyed"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 58
            }
        }
        category: link = 0x6ce57a50
        Milestones: list[u64] = {
            5
            15
            25
            30
            40
            15
        }
        stoneName: string = "RengarStructuresDestroyed"
    }
    0xb164e242 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_EpicMonstersKilled"
        catalogEntry: embed = catalogEntry {
            contentId: string = "d1495dcd-b159-4c01-bc2e-c9a2a3742278"
            itemID: u32 = 125720
        }
        mDescriptionTraKey: string = "stat_stone_description_EpicMonstersKilled"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 61
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 81
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        ChampionsAreValid: bool = false
                    }
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 60
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
        }
        category: link = 0x6ce57a50
        Milestones: list[u64] = {
            3
            10
            20
            22
            25
            10
        }
        stoneName: string = "RengarEpicMonstersKilled"
    }
    0x756274ee = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarERoots"
        catalogEntry: embed = catalogEntry {
            contentId: string = "4e93d1bb-a5b7-492e-bb27-c2bc5efc5e0c"
            itemID: u32 = 126186
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarERoots"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x2eeaa87d
        Milestones: list[u64] = {
            8
            20
            40
            50
            60
            25
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarERoots"
    }
    0xc1e0cd13 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarPSubsequent"
        catalogEntry: embed = catalogEntry {
            contentId: string = "7c269156-4371-46f3-b6f3-41beaac0ac2f"
            itemID: u32 = 126185
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarPSubsequent"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            10
            25
            50
            60
            75
            30
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarPSubsequent"
    }
    0xdb172aa8 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarQKills"
        catalogEntry: embed = catalogEntry {
            contentId: string = "fa74b68c-5386-458d-ac68-878596cc6b6a"
            itemID: u32 = 126187
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarQKills"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 239
            }
        }
        category: link = 0x06fc9407
        Milestones: list[u64] = {
            10000
            26000
            51000
            62000
            77000
            31000
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarQDamage"
    }
    "Characters/Rengar/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Rengar"
        baseHP: f32 = 590
        hpPerLevel: f32 = 104
        baseStaticHPRegen: f32 = 1.2
        hpRegenPerLevel: f32 = 0.1
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 9
            arBase: f32 = 4
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 4
            arHasRegenText: bool = false
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 14
            arBase: f32 = 4
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 4
            arMaxSegments: i32 = 4
            arDisplayAsPips: bool = true
            arOverrideSmallPipName: string = "GenericLargeUncolored"
            arOverrideMediumPipName: string = "GenericLargeUncolored"
            arOverrideLargePipName: string = "GenericLarge"
            arOverrideSpacerName: string = "PipSpacer1"
        }
        baseDamage: f32 = 68
        damagePerLevel: f32 = 3
        baseArmor: f32 = 34
        armorPerLevel: f32 = 4.2
        baseSpellBlock: f32 = 32
        spellBlockPerLevel: f32 = 2.05
        baseMoveSpeed: f32 = 345
        attackRange: f32 = 125
        attackSpeed: f32 = 0.667
        attackSpeedRatio: f32 = 0.667
        attackSpeedPerLevel: f32 = 3
        acquisitionRange: f32 = 600
        basicAttack: embed = AttackSlotData {
            mAttackTotalTime: option[f32] = {
                1.5
            }
            mAttackCastTime: option[f32] = {
                0.3
            }
            mAttackProbability: option[f32] = {
                0.45
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0.45
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0.1
                }
            }
        }
        critAttacks: list[embed] = {
            AttackSlotData {
                mAttackName: option[string] = {
                    "RengarCritAttack"
                }
            }
        }
        spellNames: list[string] = {
            "RengarQAbility/RengarQ"
            "RengarWAbility/RengarW"
            "RengarEAbility/RengarE"
            "RengarRAbility/RengarR"
        }
        spells: list[link] = {
            "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            "Characters/Rengar/Spells/RengarWAbility/RengarW"
            "Characters/Rengar/Spells/RengarEAbility/RengarE"
            "Characters/Rengar/Spells/RengarRAbility/RengarR"
        }
        extraSpells: list[string] = {
            "RengarPassiveBuffDash"
            "RengarQSound"
            "RengarQ2Sound"
            "RengarQ2"
            "RengarEMis"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
        }
        mAbilities: list[link] = {
            "Characters/Rengar/Spells/RengarRAbility"
            "Characters/Rengar/Spells/RengarQAbility"
            "Characters/Rengar/Spells/RengarWAbility"
            "Characters/Rengar/Spells/RengarEAbility"
            "Characters/Rengar/Spells/RengarPassiveAbility"
            "Characters/Rengar/Spells/RengarEEmpAbility"
        }
        passiveName: string = "game_character_passiveName_Rengar"
        passiveLuaName: string = ""
        passiveToolTip: string = "game_character_passiveDescription_Rengar"
        passiveSpell: string = "RengarPassive"
        passive1IconName: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_P.dds"
        name: string = "game_character_displayname_Rengar"
        weaponMaterials: list[string] = {
            "RengarBasicAttack"
            "None"
            "RengarBasicAttack2"
            "RengarBasicAttack3"
        }
        selectionHeight: f32 = 225
        selectionRadius: f32 = 120
        pathfindingCollisionRadius: f32 = 35
        unitTagsString: string = "Champion"
        mEducationToolData: embed = ToolEducationData {
            firstItem: i32 = 1055
        }
        characterToolData: embed = characterToolData {
            spellData: list[embed] = {
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
            }
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                3 = ToolAiPresence {}
                4 = ToolAiPresence {}
            }
            passiveData: list[embed] = {
                ToolPassiveData {
                    name: string = "game_character_passiveName_Rengar"
                    level: list[i32] = {
                        1
                        6
                        11
                        16
                    }
                }
            }
            searchTags: string = "assassin"
            searchTagsSecondary: string = "fighter"
            championId: i32 = 107
            roles: string = "BRAWLER,TANK,ASSASSIN"
            PARFadeColor: string = "55 55 55"
            magicRank: i32 = 2
            LevelSpellEffectiveness: f32 = 2
            difficultyRank: i32 = 8
            description: string = "game_character_description_Rengar"
            defenseRank: i32 = 4
            classification: string = "Deadly"
            0xaa75da9d: bool = false
            attackRank: i32 = 7
        }
        platformEnabled: bool = true
        flags: u32 = 8398088
        purchaseIdentities: list[hash] = {
            "Melee"
        }
        mPreferredPerkStyle: link = "Perks/Styles/Domination"
        mPerkReplacements: embed = PerkReplacementList {
            mReplacements: list[pointer] = {
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Sorcery/ManaflowBand"
                    mReplaceWith: hash = "Perks/Styles/Sorcery/NullifyingOrb"
                }
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Precision/PresenceOfMind"
                    mReplaceWith: hash = "Perks/Styles/Precision/Triumph"
                }
            }
        }
        mCharacterPassiveSpell: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        mCharacterPassiveBuffs: list[embed] = {
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
                mComponentBuffs: list[link] = {
                    "Characters/Rengar/Spells/RengarPassiveEmpowered"
                    "Characters/Rengar/Spells/RengarOutOfCombat"
                    "Characters/Rengar/Spells/RengarInCombat"
                }
            }
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Rengar/Spells/RengarPassiveBonetoothManager"
                mAllowOnClones: bool = false
            }
        }
        0x6854087e: list2[embed] = {
            0x47f13ab0 {
                0xe4f7105d: link = "Maps/Shipping/Map11/Modes/SWIFTPLAY"
                0xcf19cb5d: embed = 0x770f7888 {
                    damagePerLevel: f32 = 0.5
                    baseHP: f32 = 30
                    hpPerLevel: f32 = 6
                }
            }
        }
    }
    0x3330715f = ItemRecommendationOverrideSet {
        mOverrides: list[embed] = {
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 11
                        mModeNameStringId: hash = "CLASSIC"
                        mPosition: hash = "jungle"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1102"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1101"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1103"
                            "Items/2003"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6697"
                            "Items/6699"
                        }
                        MaxCompletedItems: u32 = 1
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3009"
                            "Items/3158"
                            "Items/3010"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6698"
                            "Items/3814"
                            "Items/6696"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/6698"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/3031"
                            "Items/3072"
                            "Items/3026"
                        }
                        MaxCompletedItems: u32 = 5
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6694"
                            "Items/6673"
                            "Items/3026"
                            "Items/3156"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 11
                        mModeNameStringId: hash = "CLASSIC"
                        mPosition: hash = "Top"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1055"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1054"
                            "Items/2003"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3074"
                            "Items/6698"
                            "Items/6697"
                        }
                        MaxCompletedItems: u32 = 1
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3158"
                            "Items/3047"
                            "Items/3111"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6692"
                            "Items/6701"
                            "Items/3074"
                            "Items/6699"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3031"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6701"
                            "Items/6699"
                            "Items/3036"
                            "Items/3814"
                            "Items/6673"
                            "Items/3026"
                            "Items/3161"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 12
                        mModeNameStringId: hash = "ARAM"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3177"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3134"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3184"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6691"
                            "Items/6693"
                            "Items/6692"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3111"
                            "Items/3047"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3142"
                            "Items/3814"
                            "Items/3071"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3142"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6333"
                            "Items/3156"
                            "Items/3026"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6694"
                            "Items/6609"
                            "Items/6035"
                            "Items/3071"
                            "Items/6333"
                            "Items/3026"
                            "Items/3156"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 30
                        mModeNameStringId: hash = "cherry"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/223177"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/223184"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223111"
                            "Items/223047"
                            "Items/223005"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226691"
                            "Items/226693"
                            "Items/226692"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223142"
                            "Items/223071"
                            "Items/226696"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223142"
                            "Items/223814"
                            "Items/226696"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226333"
                            "Items/223156"
                            "Items/223026"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226694"
                            "Items/226609"
                            "Items/226035"
                            "Items/223071"
                            "Items/226333"
                            "Items/223026"
                            "Items/223156"
                        }
                    }
                }
            }
        }
    }
    0x4ebd1ade = RecSpellRankUpInfolist {
        RecSpellRankUpInfos: list[embed] = {
            recSpellRankUpInfo {
                MapId: u32 = 12
                position: hash = "None"
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
            recSpellRankUpInfo {
                MapId: u32 = 11
                position: hash = "jungle"
                IsDefaultRecommendation: bool = true
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
            recSpellRankUpInfo {
                MapId: u32 = 11
                position: hash = "Top"
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
        }
    }
    0x5f0ab59f = ItemRecommendationContextList {
        mAllStartingItemIds: map[u32,embed] = {
            11 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    1083
                    1054
                    1055
                    1056
                    3865
                    1006
                    1028
                    1029
                    1101
                    2031
                    1036
                    1102
                    1052
                    1103
                    2003
                    3070
                    1082
                }
            }
            12 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    3144
                    3051
                    3145
                    3044
                    1011
                    4642
                    3147
                    1042
                    3067
                    2508
                    2051
                    1043
                    3801
                    2022
                    6690
                    2031
                    3802
                    1036
                    3112
                    1058
                    1037
                    2003
                    3803
                    1038
                    1053
                    3006
                    3057
                    3108
                    2020
                    2021
                    1026
                    6660
                    1027
                    3133
                    3184
                    1028
                    3134
                    1029
                    3177
                    3076
                    1001
                    1052
                    3077
                    3070
                }
            }
        }
        mAllRecommendableItemIds: map[u32,embed] = {
            11 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    3173
                    3152
                    6694
                    6673
                    3073
                    8010
                    3046
                    3190
                    4643
                    6617
                    3171
                    6692
                    2503
                    3084
                    3869
                    3107
                    4633
                    3748
                    6609
                    3161
                    3742
                    3111
                    6653
                    3032
                    3155
                    3176
                    4629
                    6655
                    3157
                    6699
                    3078
                    3222
                    6620
                    3172
                    3072
                    3116
                    6697
                    3139
                    3118
                    3089
                    3068
                    3010
                    2502
                    3143
                    3033
                    6664
                    3158
                    3137
                    3087
                    3181
                    4401
                    6333
                    3110
                    6631
                    6610
                    2065
                    6675
                    3083
                    3004
                    3077
                    3302
                    4645
                    3050
                    6621
                    3508
                    3094
                    3175
                    3065
                    6696
                    3119
                    3142
                    3165
                    3877
                    3115
                    6665
                    6657
                    3036
                    3871
                    3109
                    3009
                    3153
                    2501
                    3865
                    3053
                    3003
                    6676
                    3047
                    3026
                    3070
                    4646
                    6701
                    3020
                    6672
                    3174
                    3124
                    6695
                    3074
                    6616
                    3170
                    4005
                    3091
                    6662
                    3041
                    3876
                    3135
                    2504
                    3085
                    3870
                    3006
                    3102
                    3814
                    3031
                    4628
                    3002
                    3075
                    3156
                    3504
                    6698
                    8020
                    3179
                    3100
                    3071
                }
            }
            12 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    3050
                    6621
                    3152
                    3508
                    126697
                    6694
                    6673
                    3094
                    3073
                    3065
                    6696
                    8010
                    3046
                    3190
                    6617
                    4004
                    3119
                    3142
                    6692
                    2503
                    3084
                    3165
                    3115
                    6665
                    3107
                    6657
                    3036
                    4633
                    3748
                    3109
                    6609
                    3161
                    3009
                    3153
                    2501
                    3111
                    3742
                    6653
                    3053
                    3032
                    3155
                    4629
                    3003
                    6676
                    6655
                    3157
                    3047
                    6699
                    3078
                    3222
                    3070
                    4646
                    6620
                    6701
                    3020
                    6672
                    3072
                    3124
                    6695
                    3116
                    3074
                    6616
                    3139
                    3118
                    3089
                    3068
                    4005
                    2502
                    3091
                    6662
                    3143
                    3033
                    3135
                    2504
                    6664
                    3085
                    3158
                    3137
                    3006
                    3087
                    3181
                    4401
                    6333
                    3110
                    3102
                    3814
                    6610
                    6631
                    2065
                    3031
                    4628
                    3002
                    6675
                    3083
                    3075
                    3156
                    3004
                    3504
                    6698
                    8020
                    3077
                    3179
                    3302
                    4645
                    3100
                    3071
                }
            }
            30 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    226664
                    223085
                    223158
                    223006
                    223087
                    4010
                    223181
                    224401
                    223508
                    223102
                    223814
                    226631
                    223031
                    224628
                    226675
                    223075
                    223177
                    223004
                    223504
                    226698
                    228020
                    223302
                    224645
                    223100
                    2049
                    223071
                    226621
                    223152
                    226694
                    226673
                    223094
                    4017
                    223073
                    223065
                    223146
                    226696
                    223748
                    3430
                    223046
                    223190
                    226617
                    222051
                    223111
                    223142
                    226692
                    222503
                    4015
                    223084
                    223165
                    223157
                    223115
                    223005
                    226665
                    223107
                    226657
                    223036
                    224633
                    223109
                    4011
                    2050
                    226609
                    223161
                    223009
                    223153
                    226653
                    223184
                    223074
                    223053
                    223032
                    224629
                    223003
                    226676
                    226655
                    223047
                    223026
                    226699
                    223078
                    223222
                    224646
                    223172
                    226620
                    226701
                    223020
                    226672
                    4016
                    223072
                    223124
                    226695
                    223116
                    223095
                    226616
                    226697
                    226333
                    223118
                    223089
                    223068
                    223039
                    224005
                    226610
                    447111
                    222502
                    223091
                    223112
                    226662
                    223185
                    223143
                    223033
                    223135
                }
            }
        }
        mContexts: list[embed] = {
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 12
                mModeNameStringId: hash = "ARAM"
                mPosition: hash = "None"
                mIsDefaultPosition: bool = true
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1001
                                        2003
                                        2003
                                        3134
                                        1036
                                        3134
                                        1036
                                        3133
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1001
                            2003
                            2003
                            3134
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1036
                            3134
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1036
                            3133
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/6676"
                    "Items/126697"
                    "Items/3111"
                    "Items/3077"
                    "Items/6698"
                    "Items/6610"
                    "Items/3031"
                    "Items/6699"
                    "Items/3158"
                    "Items/3036"
                    "Items/3084"
                    "Items/6692"
                    "Items/3047"
                    "Items/3814"
                    "Items/2502"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        6676
                                        3084
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AvM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4646
                                    }
                                }
                                "AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3084
                                        126697
                                    }
                                }
                                "Av5" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        2502
                                    }
                                }
                                "AwC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3047
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3074
                                        6631
                                    }
                                }
                                "AwG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3111
                                        3077
                                    }
                                }
                                "AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3047
                                    }
                                }
                                "Awc" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4646
                                        4645
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        6676
                                        6610
                                    }
                                }
                                "AxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        3158
                                    }
                                }
                                "AxQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4646
                                        4645
                                    }
                                }
                                "AxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        6676
                                        6692
                                    }
                                }
                                "A6k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "A7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                        6676
                                    }
                                }
                                "A+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        126697
                                        3111
                                    }
                                }
                                "BIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4646
                                        3020
                                        3089
                                    }
                                }
                                "BIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4645
                                        3100
                                    }
                                }
                                "BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6692
                                    }
                                }
                                "Bnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6610
                                    }
                                }
                                "Bn/" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4646
                                    }
                                }
                                "BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        126697
                                        3077
                                    }
                                }
                                "Bok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3111
                                        3047
                                    }
                                }
                                "Bon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6676
                                        126697
                                    }
                                }
                                "Boo" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "Boq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3158
                                    }
                                }
                                "Bor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3158
                                    }
                                }
                                "Bot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6676
                                        3158
                                    }
                                }
                                "e7p" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3077
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        3077
                                    }
                                }
                                "AnGAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        3065
                                    }
                                }
                                "AnGBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3065
                                    }
                                }
                                "AvBBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                    }
                                }
                                "AvMAwc" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                        4646
                                    }
                                }
                                "AvMAxQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4646
                                        4645
                                    }
                                }
                                "AvMBIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4646
                                        3089
                                        3100
                                    }
                                }
                                "AvMBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                        3100
                                        3089
                                    }
                                }
                                "AvMBn/" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4646
                                        4645
                                    }
                                }
                                "AvXBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3111
                                        3158
                                    }
                                }
                                "AvcBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                    }
                                }
                                "AvnAwC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        6610
                                    }
                                }
                                "AvnAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        2502
                                        3077
                                    }
                                }
                                "AvnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        6333
                                        2502
                                    }
                                }
                                "AvnBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "AvnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        3077
                                        3031
                                    }
                                }
                                "AvnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3077
                                    }
                                }
                                "Av5AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        2502
                                        3047
                                    }
                                }
                                "Av5BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "Av/BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3111
                                        6610
                                    }
                                }
                                "AwCAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        6692
                                    }
                                }
                                "AwCBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6692
                                    }
                                }
                                "AwFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        3111
                                        3074
                                    }
                                }
                                "AwFBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        3748
                                        6631
                                    }
                                }
                                "AwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3111
                                        3074
                                    }
                                }
                                "AwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3074
                                    }
                                }
                                "AwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        6699
                                    }
                                }
                                "AwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                    }
                                }
                                "AwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwGBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AwLAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        2502
                                    }
                                }
                                "AwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        2502
                                        3065
                                    }
                                }
                                "AwMAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        2502
                                        3065
                                    }
                                }
                                "AwMA6k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "AwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        2502
                                    }
                                }
                                "AwMBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3047
                                    }
                                }
                                "AwMBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AwRBIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                    }
                                }
                                "AwRBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4645
                                    }
                                }
                                "AwcBIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        3089
                                        4646
                                    }
                                }
                                "AwcBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        4645
                                        3089
                                    }
                                }
                                "AwnA+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        6676
                                    }
                                }
                                "AwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3065
                                        2502
                                    }
                                }
                                "AwnBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "AwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        3031
                                        3077
                                    }
                                }
                                "AwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        6676
                                        3077
                                    }
                                }
                                "AwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "AwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6610
                                        3077
                                    }
                                }
                                "AxQBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                    }
                                }
                                "AxWBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                    }
                                }
                                "AxWBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3161
                                        3065
                                    }
                                }
                                "AxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        126697
                                        3031
                                        3077
                                    }
                                }
                                "AxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        6676
                                    }
                                }
                                "AxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6699
                                    }
                                }
                                "AxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6701
                                        3077
                                    }
                                }
                                "AxZBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3111
                                    }
                                }
                                "A7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                        6699
                                    }
                                }
                                "A+kBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3111
                                        3031
                                    }
                                }
                                "BIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        3089
                                        3100
                                    }
                                }
                                "BImBn/" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                    }
                                }
                                "Bi9BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "BnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6692
                                    }
                                }
                                "BnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6333
                                    }
                                }
                                "BnSBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "BoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                        3031
                                    }
                                }
                                "BoUBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "BoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3036
                                    }
                                }
                                "BoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3158
                                    }
                                }
                                "BoUBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3158
                                    }
                                }
                                "BokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                    }
                                }
                                "BorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "e7pAu+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAvB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                    }
                                }
                                "e7pAvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3036
                                        3111
                                    }
                                }
                                "e7pAvc" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        6610
                                    }
                                }
                                "e7pAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3111
                                        6676
                                    }
                                }
                                "e7pAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3047
                                    }
                                }
                                "e7pAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        6610
                                    }
                                }
                                "e7pAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        6699
                                    }
                                }
                                "e7pA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6676
                                        3077
                                    }
                                }
                                "e7pA+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3158
                                    }
                                }
                                "e7pBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        6692
                                    }
                                }
                                "e7pBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3111
                                        3031
                                    }
                                }
                                "e7pBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3047
                                    }
                                }
                                "e7pBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3077
                                    }
                                }
                                "e7pBoo" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6676
                                    }
                                }
                                "e7pBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3158
                                    }
                                }
                                "e7pBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3077
                                    }
                                }
                                "e7pBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnFAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                    }
                                }
                                "AnFAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AnGAvnAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3075
                                        3065
                                        6610
                                    }
                                }
                                "AnGAvnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                    }
                                }
                                "AnGAv5AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "AnGAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        6610
                                        3075
                                    }
                                }
                                "AnGAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        3065
                                    }
                                }
                                "AnGAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        6692
                                    }
                                }
                                "AvMAwRBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                    }
                                }
                                "AvMAwcBIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3089
                                        4646
                                    }
                                }
                                "AvMAwcBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                        3089
                                    }
                                }
                                "AvMAxQBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                    }
                                }
                                "AvMBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3089
                                        3100
                                        3135
                                    }
                                }
                                "AvMBImBn/" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                    }
                                }
                                "AvXAvcBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3158
                                        3111
                                    }
                                }
                                "AvXAvnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvXAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6699
                                        3077
                                    }
                                }
                                "AvXAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6699
                                        3077
                                    }
                                }
                                "AvXBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3111
                                        3158
                                    }
                                }
                                "AvcAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvnAv5AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                    }
                                }
                                "AvnAwFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                    }
                                }
                                "AvnAwFBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AvnAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvnAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                        3077
                                        3065
                                    }
                                }
                                "AvnBi9BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        6692
                                    }
                                }
                                "AvnBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3077
                                        3065
                                    }
                                }
                                "Av5AwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                        6610
                                        3075
                                    }
                                }
                                "Av5AwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "Av5AwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        2502
                                        6692
                                    }
                                }
                                "Av/AwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Av/BnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AwCAwFBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "AwCAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6610
                                        3158
                                    }
                                }
                                "AwCAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                    }
                                }
                                "AwFAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                    }
                                }
                                "AwFAwMA6k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                        2501
                                    }
                                }
                                "AwFAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                    }
                                }
                                "AwFAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6631
                                        6698
                                    }
                                }
                                "AwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3074
                                    }
                                }
                                "AwFAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "AwFAwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3074
                                    }
                                }
                                "AwFAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3036
                                    }
                                }
                                "AwFBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6676
                                    }
                                }
                                "AwLAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                    }
                                }
                                "AwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                        3065
                                        3077
                                    }
                                }
                                "AwMAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        2502
                                        3077
                                    }
                                }
                                "AwMAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "AwMAxWBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                    }
                                }
                                "AwMBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AwRBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        3135
                                        3100
                                    }
                                }
                                "AwcBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        3089
                                    }
                                }
                                "AwnAxTBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwnAxTBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwnAxZBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "AwnA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                    }
                                }
                                "AwnBi9BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                    }
                                }
                                "AwnBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3031
                                        3077
                                    }
                                }
                                "AwnBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3065
                                        3077
                                    }
                                }
                                "AwnBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6610
                                        3031
                                    }
                                }
                                "AwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3036
                                    }
                                }
                                "AwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                        3077
                                    }
                                }
                                "AxWBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3089
                                    }
                                }
                                "AxWBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3065
                                        3077
                                    }
                                }
                                "AxWBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                    }
                                }
                                "AxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3814
                                        3036
                                    }
                                }
                                "AxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "Bi9BnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3111
                                    }
                                }
                                "BnSBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "e7pAvBAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvBBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                        6699
                                    }
                                }
                                "e7pAvXAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3036
                                    }
                                }
                                "e7pAvXAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3036
                                    }
                                }
                                "e7pAvXBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3111
                                        3077
                                    }
                                }
                                "e7pAvZBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvcBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                        3077
                                    }
                                }
                                "e7pAvnAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvnAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "e7pAvnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6333
                                        6692
                                    }
                                }
                                "e7pAvnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        6610
                                    }
                                }
                                "e7pAvnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "e7pAvnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6676
                                    }
                                }
                                "e7pAwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3111
                                        3047
                                    }
                                }
                                "e7pAwFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                    }
                                }
                                "e7pAwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6676
                                        3074
                                    }
                                }
                                "e7pAwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6676
                                    }
                                }
                                "e7pAwFA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFA+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "e7pAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3111
                                        3158
                                    }
                                }
                                "e7pAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3111
                                        3158
                                    }
                                }
                                "e7pAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3077
                                        6676
                                    }
                                }
                                "e7pAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "e7pAwnAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "e7pAwnA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAwnA+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3077
                                        6333
                                    }
                                }
                                "e7pAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        6610
                                    }
                                }
                                "e7pAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        6676
                                        3077
                                    }
                                }
                                "e7pAwnBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        3814
                                    }
                                }
                                "e7pAxWA+k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAxWBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                    }
                                }
                                "e7pAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        6699
                                    }
                                }
                                "e7pAxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6610
                                    }
                                }
                                "e7pAxWBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3077
                                        3814
                                    }
                                }
                                "e7pA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                        3077
                                    }
                                }
                                "e7pA+kBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3077
                                        3158
                                    }
                                }
                                "e7pBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3077
                                    }
                                }
                                "e7pBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "e7pBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3036
                                    }
                                }
                                "e7pBoUBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3111
                                        3031
                                    }
                                }
                                "e7pBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                        3036
                                    }
                                }
                                "e7pBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3077
                                    }
                                }
                                "e7pBoUBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                        3077
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnFAwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AnGAvnAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        3075
                                        3077
                                    }
                                }
                                "AnGAv5AwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3075
                                        6610
                                        3083
                                    }
                                }
                                "AnGAwDAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                    }
                                }
                                "AnGAwFAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                    }
                                }
                                "AnGAwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        3077
                                        3075
                                    }
                                }
                                "AvMAwRAwcBIl" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3135
                                        4646
                                    }
                                }
                                "AvMAwRAwcBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        4645
                                    }
                                }
                                "AvMAwRBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3135
                                        3100
                                        3157
                                    }
                                }
                                "AvMAwcBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3089
                                        3135
                                        3157
                                    }
                                }
                                "AvMAw/BIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3089
                                    }
                                }
                                "AvXAvcAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvXAvcAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6699
                                        3077
                                    }
                                }
                                "AvXAvcAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6699
                                    }
                                }
                                "AvXAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvXAwFAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvXAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3111
                                    }
                                }
                                "AvXAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        3077
                                    }
                                }
                                "AvXAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvcAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                    }
                                }
                                "AvcAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvnAv5AwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                    }
                                }
                                "AvnAwCAwFBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "AvnAwFAwMBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        3074
                                    }
                                }
                                "AvnAwFBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AvnAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                    }
                                }
                                "AvnBi9BnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        3071
                                        3077
                                    }
                                }
                                "Av5AwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                        2501
                                        3077
                                    }
                                }
                                "Av5AwnBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3071
                                        2502
                                    }
                                }
                                "AwCAwFAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        6333
                                    }
                                }
                                "AwCAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3031
                                        126697
                                    }
                                }
                                "AwCAwFBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "AwFAwMAwnA6k" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2501
                                        6610
                                        2502
                                    }
                                }
                                "AwFAwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        6698
                                        3074
                                    }
                                }
                                "AwFAwnBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFAwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                        3036
                                    }
                                }
                                "AwFAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                        3036
                                    }
                                }
                                "AwFAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "AwFBoUBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                    }
                                }
                                "AwMAwnBi9BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                    }
                                }
                                "AwRAwcBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                        3135
                                    }
                                }
                                "AwnAxTBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwnBi9BnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        3071
                                        3077
                                    }
                                }
                                "AwnBnSBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                    }
                                }
                                "e7pAvBAvXBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "e7pAvBAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvBAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "e7pAvXAvcBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3111
                                        3077
                                    }
                                }
                                "e7pAvXAvnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                    }
                                }
                                "e7pAvXAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvXAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "e7pAvXAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        6699
                                    }
                                }
                                "e7pAvXAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        6699
                                    }
                                }
                                "e7pAvXBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "e7pAvcAvnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvcAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvcAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3158
                                    }
                                }
                                "e7pAvcAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                        3814
                                    }
                                }
                                "e7pAvcAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                    }
                                }
                                "e7pAvcBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvnAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvnAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6610
                                        6699
                                    }
                                }
                                "e7pAvnAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvnBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "e7pAwCAwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                    }
                                }
                                "e7pAwFAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3074
                                    }
                                }
                                "e7pAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6610
                                        3031
                                    }
                                }
                                "e7pAwFAwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3031
                                        3036
                                    }
                                }
                                "e7pAwFAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBnSBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                    }
                                }
                                "e7pAwFBoUBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3158
                                    }
                                }
                                "e7pAwFBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFBonBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                    }
                                }
                                "e7pAwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                        6676
                                    }
                                }
                                "e7pAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3158
                                    }
                                }
                                "e7pAwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        2502
                                    }
                                }
                                "e7pAwMAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6610
                                    }
                                }
                                "e7pAwnAxTBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "e7pAwnAxTBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "e7pAwnA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6699
                                        3031
                                    }
                                }
                                "e7pAwnA+kBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "e7pAwnBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        3036
                                    }
                                }
                                "e7pAwnBnSBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "e7pAwnBoUBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6610
                                        3036
                                        3077
                                    }
                                }
                                "e7pAwnBoUBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3036
                                        3031
                                    }
                                }
                                "e7pAwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                        3036
                                    }
                                }
                                "e7pAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        3036
                                    }
                                }
                                "e7pAxWA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                        6699
                                    }
                                }
                                "e7pAxWBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3031
                                        6699
                                    }
                                }
                                "e7pAxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6699
                                    }
                                }
                                "e7pAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                        3814
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnGAv5AwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3075
                                        2501
                                        3077
                                    }
                                }
                                "AnGAwFAwMAwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        3074
                                    }
                                }
                                "AvMAwRAwcBIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3135
                                    }
                                }
                                "AvMAwRAw/BIlBIm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3100
                                    }
                                }
                                "AvXAvcAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvXAvcAwnBoRBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        3077
                                    }
                                }
                                "AvXAvcAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        3077
                                    }
                                }
                                "AvXAwFAwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6699
                                        6610
                                    }
                                }
                                "AvXAwFAxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvcAwFAwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwFAwMAwnA6kBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2502
                                        2501
                                    }
                                }
                                "AwFAwnBoUBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6610
                                        3036
                                    }
                                }
                                "AwFAxWBoUBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvBAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvXAvcAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvXAvcAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3077
                                        6699
                                    }
                                }
                                "e7pAvXAvcAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3814
                                        3077
                                    }
                                }
                                "e7pAvXAvnAwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvXAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvXAwFAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        6699
                                    }
                                }
                                "e7pAvXAwFAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvXAwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3036
                                    }
                                }
                                "e7pAvXAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6699
                                        3111
                                    }
                                }
                                "e7pAvXAwnBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "e7pAvXAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "e7pAvXAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "e7pAvcAwFAwnBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvcAwFAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvcAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                        3814
                                    }
                                }
                                "e7pAvcAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "e7pAvnAwFBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAvnAwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6699
                                        6610
                                    }
                                }
                                "e7pAwFAwnA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBnSBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                        6676
                                    }
                                }
                                "e7pAwFAwnBoUBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3031
                                        6610
                                    }
                                }
                                "e7pAwFAwnBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAwnBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3814
                                    }
                                }
                                "e7pAwFAxWA7mBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAxWBnSBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6699
                                        3036
                                    }
                                }
                                "e7pAwFAxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "e7pAwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                        3814
                                    }
                                }
                                "e7pAwFBnSBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                    }
                                }
                                "e7pAwFBoUBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3031
                                        3158
                                    }
                                }
                                "e7pAwnBoUBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 11
                mModeNameStringId: hash = "CLASSIC"
                mPosition: hash = "utility"
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2003
                                        2003
                                        3865
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            2003
                            2003
                            3865
                        }
                    }
                }
                UpgradeChoices: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3865"
                    "Items/3158"
                    "Items/3179"
                    "Items/3142"
                    "Items/6692"
                    "Items/6701"
                    "Items/3077"
                    "Items/6699"
                    "Items/6676"
                    "Items/3877"
                    "Items/3047"
                    "Items/3171"
                    "Items/6698"
                    "Items/3814"
                    "Items/3009"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3865
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "A8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3179
                                        3158
                                        3047
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvnA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3742
                                    }
                                }
                                "AwFA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AxGA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AxWA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3179
                                        3742
                                        6699
                                    }
                                }
                                "AxrA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3047
                                        3877
                                    }
                                }
                                "A8ZBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3047
                                    }
                                }
                                "A8ZBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvnA6eA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                        3174
                                    }
                                }
                                "AxWAxrA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3142
                                        3171
                                    }
                                }
                                "AxWA6eA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                    }
                                }
                                "AxrA8ZA8l" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AxGAxWAxrA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 11
                mModeNameStringId: hash = "CLASSIC"
                mPosition: hash = "bottom"
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1055
                                        2003
                                        1054
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                }
                UpgradeChoices: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3077"
                    "Items/3158"
                    "Items/6697"
                    "Items/3074"
                    "Items/6701"
                    "Items/6676"
                    "Items/6692"
                    "Items/6698"
                    "Items/3036"
                    "Items/3047"
                    "Items/3031"
                    "Items/6699"
                    "Items/3171"
                    "Items/3142"
                    "Items/3111"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6697
                                        6692
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AwC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                        3158
                                    }
                                }
                                "AxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6697
                                    }
                                }
                                "Bok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3047
                                        3077
                                    }
                                }
                                "Bop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        6676
                                    }
                                }
                                "Bor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "Bot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6701
                                        3047
                                    }
                                }
                                "AwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6697
                                    }
                                }
                                "AxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6676
                                        6701
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AwCAwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                                "AwCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AwCAwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 11
                mModeNameStringId: hash = "CLASSIC"
                mPosition: hash = "middle"
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1054
                                        2003
                                        1055
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                }
                UpgradeChoices: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3077"
                    "Items/3158"
                    "Items/3074"
                    "Items/6701"
                    "Items/6698"
                    "Items/3142"
                    "Items/6676"
                    "Items/6699"
                    "Items/3031"
                    "Items/3036"
                    "Items/6692"
                    "Items/3171"
                    "Items/6697"
                    "Items/3111"
                    "Items/3009"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 11
                mModeNameStringId: hash = "CLASSIC"
                mPosition: hash = "jungle"
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1102
                                        2003
                                        1101
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1102
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1101
                            2003
                        }
                    }
                }
                UpgradeChoices: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3158"
                    "Items/3077"
                    "Items/6701"
                    "Items/6699"
                    "Items/6698"
                    "Items/3036"
                    "Items/3142"
                    "Items/3814"
                    "Items/3171"
                    "Items/6697"
                    "Items/3031"
                    "Items/3009"
                    "Items/6695"
                    "Items/6676"
                    "Items/3033"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        3077
                                        6701
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        6697
                                        6701
                                    }
                                }
                                "AvC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        6697
                                        6701
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        6699
                                    }
                                }
                                "Awc" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                    }
                                }
                                "AxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        6701
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                    }
                                }
                                "AxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6699
                                        6701
                                        6697
                                    }
                                }
                                "A7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                        3047
                                        3111
                                    }
                                }
                                "BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        3031
                                    }
                                }
                                "Bok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        3047
                                    }
                                }
                                "Bon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        6701
                                    }
                                }
                                "Boo" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        3158
                                    }
                                }
                                "Bop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        3009
                                    }
                                }
                                "Boq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6701
                                        3047
                                    }
                                }
                                "Bor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        6701
                                    }
                                }
                                "Bot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        3142
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6699
                                        6701
                                    }
                                }
                                "AvBAxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        6676
                                        3077
                                    }
                                }
                                "AvBBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvBBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        6699
                                    }
                                }
                                "AvBBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3077
                                        6692
                                    }
                                }
                                "AvBBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3142
                                        6699
                                    }
                                }
                                "AvCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6697
                                    }
                                }
                                "AvCBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AvCBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                                "AvCBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3142
                                    }
                                }
                                "AvXBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvnAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                    }
                                }
                                "AvnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6610
                                        3071
                                    }
                                }
                                "AvnBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                    }
                                }
                                "AvnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3077
                                        6692
                                    }
                                }
                                "AvnBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3814
                                    }
                                }
                                "Av/BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3111
                                    }
                                }
                                "AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3047
                                        3111
                                    }
                                }
                                "AwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                        6701
                                    }
                                }
                                "AwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        6699
                                    }
                                }
                                "AwFA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                    }
                                }
                                "AwFBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6701
                                        6698
                                    }
                                }
                                "AwFBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                        6701
                                    }
                                }
                                "AwFBoo" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3158
                                    }
                                }
                                "AwFBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                        6701
                                    }
                                }
                                "AwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6701
                                        6699
                                    }
                                }
                                "AwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        6701
                                    }
                                }
                                "AwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3142
                                    }
                                }
                                "AwnBnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                    }
                                }
                                "AwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3077
                                        6692
                                    }
                                }
                                "AwnBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxGAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        6699
                                    }
                                }
                                "AxGBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AxGBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                    }
                                }
                                "AxGBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AxGBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3009
                                    }
                                }
                                "AxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                                "AxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                    }
                                }
                                "AxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        3071
                                    }
                                }
                                "AxWBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        6699
                                    }
                                }
                                "AxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3814
                                        6699
                                    }
                                }
                                "AxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3077
                                        6692
                                    }
                                }
                                "AxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3142
                                        6699
                                    }
                                }
                                "A7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                                "A7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                                "BoUBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3158
                                    }
                                }
                                "BoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "BoUBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "BokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        3047
                                    }
                                }
                                "BokBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "BonBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "BonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                                "BonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3814
                                    }
                                }
                                "BooBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3009
                                    }
                                }
                                "BooBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                    }
                                }
                                "BopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "BopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        6701
                                    }
                                }
                                "BopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                                "BoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        6701
                                    }
                                }
                                "BoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3814
                                    }
                                }
                                "BorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3036
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwFAxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                    }
                                }
                                "AvBAwFBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        6696
                                    }
                                }
                                "AvBAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        6699
                                        6697
                                    }
                                }
                                "AvBAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        6692
                                    }
                                }
                                "AvBAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3142
                                        6699
                                    }
                                }
                                "AvBAxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3077
                                        3036
                                    }
                                }
                                "AvBBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3077
                                    }
                                }
                                "AvBBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        3814
                                    }
                                }
                                "AvBBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        3077
                                    }
                                }
                                "AvBBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3170
                                        3077
                                    }
                                }
                                "AvCAwFAxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvCAwFBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                                "AvCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3142
                                    }
                                }
                                "AvXAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                    }
                                }
                                "AvXBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvZAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvZAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvZBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                    }
                                }
                                "AvcAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                        6698
                                    }
                                }
                                "AvcAxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3031
                                    }
                                }
                                "AvcAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3077
                                        3031
                                    }
                                }
                                "AvcAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                    }
                                }
                                "AvcBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                        3814
                                    }
                                }
                                "AvnAwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                    }
                                }
                                "AvnAwFAxG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvnAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                        3074
                                    }
                                }
                                "AvnAwFBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvnAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                        6701
                                        6697
                                    }
                                }
                                "AvnAwFBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6692
                                    }
                                }
                                "AvnAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3142
                                    }
                                }
                                "AvnBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3174
                                        3033
                                    }
                                }
                                "Av/AwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                    }
                                }
                                "AwCAwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3078
                                        6692
                                        3036
                                    }
                                }
                                "AwCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAwnBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAwnBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3814
                                        3071
                                    }
                                }
                                "AwFAwnBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAwnBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxGAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        3814
                                    }
                                }
                                "AwFAxGA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AwFAxGBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                    }
                                }
                                "AwFAxGBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxGBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3814
                                    }
                                }
                                "AwFAxGBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3009
                                    }
                                }
                                "AwFAxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwFAxWA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        6698
                                        3071
                                    }
                                }
                                "AwFAxWBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        3814
                                    }
                                }
                                "AwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3142
                                        3814
                                    }
                                }
                                "AwFAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        6695
                                    }
                                }
                                "AwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3142
                                        3814
                                    }
                                }
                                "AwFA7mBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3033
                                    }
                                }
                                "AwFA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        6698
                                    }
                                }
                                "AwFA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwFBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AwFBoUBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBokBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3158
                                    }
                                }
                                "AwFBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBokBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3033
                                        3009
                                    }
                                }
                                "AwFBonBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBonBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3033
                                    }
                                }
                                "AwFBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwFBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwFBooBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        6698
                                    }
                                }
                                "AwFBooBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3009
                                        3158
                                    }
                                }
                                "AwFBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AwFBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                    }
                                }
                                "AwFBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3814
                                    }
                                }
                                "AwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3814
                                    }
                                }
                                "AwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                        3036
                                    }
                                }
                                "AwnBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                    }
                                }
                                "AxGAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxGAxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6701
                                        3171
                                    }
                                }
                                "AxGAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AxGAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3077
                                    }
                                }
                                "AxGAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxGA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AxGBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AxGBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AxWA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        6701
                                    }
                                }
                                "AxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        3171
                                    }
                                }
                                "AxWBoUBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                        3171
                                    }
                                }
                                "AxWBoUBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                        3171
                                    }
                                }
                                "AxWBoUBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxWBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3171
                                        3077
                                    }
                                }
                                "AxWBokBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxWBonBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AxWBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        3171
                                    }
                                }
                                "AxWBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3814
                                        3033
                                    }
                                }
                                "AxWBooBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                        3814
                                    }
                                }
                                "AxWBooBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxWBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                    }
                                }
                                "AxWBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxWBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3077
                                    }
                                }
                                "AxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3077
                                    }
                                }
                                "A7mBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "A7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        3036
                                    }
                                }
                                "BonBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "BoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAvcBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3031
                                    }
                                }
                                "AvBAwFAxGBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        6701
                                    }
                                }
                                "AvBAwFAxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        6698
                                        3814
                                    }
                                }
                                "AvBAwFA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                    }
                                }
                                "AvBAwFBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                    }
                                }
                                "AvBAwFBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        6701
                                    }
                                }
                                "AvBAwFBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        6698
                                    }
                                }
                                "AvBAwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        3814
                                    }
                                }
                                "AvBAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        3814
                                    }
                                }
                                "AvBAwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        6698
                                        3036
                                    }
                                }
                                "AvBAxiBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvCAwFBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvXAvcAxWBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AvXAwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvXAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                    }
                                }
                                "AvZAwFAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6695
                                        6698
                                    }
                                }
                                "AvZAwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6695
                                    }
                                }
                                "AvZAwFBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvZAwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvZAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3814
                                    }
                                }
                                "AvZAwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                    }
                                }
                                "AvZAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        3077
                                        3171
                                    }
                                }
                                "AvcAvnBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcAwFAxGBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFAxGBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                    }
                                }
                                "AvcAwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3031
                                    }
                                }
                                "AvcAwFAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3814
                                        3171
                                    }
                                }
                                "AvcAwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3031
                                        3814
                                    }
                                }
                                "AvcAwFA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvcAwFBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3158
                                    }
                                }
                                "AvcAwFBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                        3814
                                    }
                                }
                                "AvcAwFBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                    }
                                }
                                "AvcAwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3814
                                        3031
                                    }
                                }
                                "AvcAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                        3814
                                    }
                                }
                                "AvcAwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        6698
                                    }
                                }
                                "AvcAxGAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3814
                                        3171
                                    }
                                }
                                "AvcAxWBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AvcAxWBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcAxWBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3814
                                    }
                                }
                                "AvcAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3814
                                        3171
                                    }
                                }
                                "AvcAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3171
                                        3077
                                    }
                                }
                                "AvcA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvnAv/AwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3174
                                    }
                                }
                                "AvnAwFAxGBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvnAwFBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3174
                                        6676
                                    }
                                }
                                "AvnAwFBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3174
                                    }
                                }
                                "AvnAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3174
                                    }
                                }
                                "AvnAwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "Av/AwFAxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AwFAwnA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAwnBokBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3065
                                    }
                                }
                                "AwFAwnBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3173
                                        3814
                                        3036
                                    }
                                }
                                "AwFAxGAxWA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                    }
                                }
                                "AwFAxGAxWBon" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxGAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AwFAxGAxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3036
                                    }
                                }
                                "AwFAxGAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                        3171
                                    }
                                }
                                "AwFAxGA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AwFAxGA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                    }
                                }
                                "AwFAxGBomBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxGBonBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxGBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxGBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAxGBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AwFAxWA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        6701
                                    }
                                }
                                "AwFAxWA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                        3033
                                    }
                                }
                                "AwFAxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                        3171
                                    }
                                }
                                "AwFAxWBoUBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                        3171
                                    }
                                }
                                "AwFAxWBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        6698
                                        6701
                                    }
                                }
                                "AwFAxWBokBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3033
                                        6698
                                    }
                                }
                                "AwFAxWBonBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBonBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        6701
                                    }
                                }
                                "AwFAxWBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3033
                                        3171
                                    }
                                }
                                "AwFAxWBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3033
                                        3814
                                    }
                                }
                                "AwFAxWBooBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                    }
                                }
                                "AwFAxWBooBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AwFAxWBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6701
                                        3171
                                    }
                                }
                                "AwFAxWBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        6698
                                        3036
                                    }
                                }
                                "AwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        3171
                                    }
                                }
                                "AwFAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AwFAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3036
                                    }
                                }
                                "AwFA7mBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFA7mBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AwFA7mBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFA7mBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                    }
                                }
                                "AwFA7mBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AwFA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        6698
                                    }
                                }
                                "AwFBokBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBomBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBonBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBonBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFBonBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AwFBonBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        6698
                                    }
                                }
                                "AwFBopBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AwFBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3036
                                        3009
                                    }
                                }
                                "AxGAxWAxjBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        3814
                                    }
                                }
                                "AxGAxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3077
                                    }
                                }
                                "AxGAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3814
                                        3036
                                    }
                                }
                                "AxWAxjBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6701
                                    }
                                }
                                "AxWAxjBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxWAxjBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxWAxjBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3077
                                        3814
                                    }
                                }
                                "AxWA7mBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxWA7mBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3036
                                    }
                                }
                                "AxWA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3077
                                    }
                                }
                                "AxWBokBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3171
                                        3036
                                    }
                                }
                                "AxWBonBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxWBopBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                    }
                                }
                                "AxWBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAvcAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3031
                                    }
                                }
                                "AvBAvcAwFBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3170
                                    }
                                }
                                "AvBAwFAxGBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                    }
                                }
                                "AvBAwFAxiBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvBAwFAxiBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvBAwFAxiBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                    }
                                }
                                "AvBAwFBonBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                    }
                                }
                                "AvBAwFBopBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                    }
                                }
                                "AvBAwFBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                    }
                                }
                                "AvXAvcAwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvXAvcAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        3171
                                        3077
                                    }
                                }
                                "AvXAwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvXAwFAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AvZAwFAxGAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                    }
                                }
                                "AvZAwFAxWA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvZAwFAxWBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3814
                                    }
                                }
                                "AvZAwFAxWBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                    }
                                }
                                "AvZAwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3814
                                    }
                                }
                                "AvZAwFAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        6695
                                        3031
                                    }
                                }
                                "AvZAwFAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3814
                                    }
                                }
                                "AvcAwFAxGAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3031
                                        6701
                                    }
                                }
                                "AvcAwFAxGAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3031
                                    }
                                }
                                "AvcAwFAxGBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFAxWA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                    }
                                }
                                "AvcAwFAxWA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvcAwFAxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                    }
                                }
                                "AvcAwFAxWBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvcAwFAxWBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvcAwFAxWBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3171
                                        3814
                                    }
                                }
                                "AvcAwFAxWBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AvcAwFAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                        3171
                                        3031
                                    }
                                }
                                "AvcAwFAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3814
                                        3171
                                    }
                                }
                                "AvcAwFAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3814
                                    }
                                }
                                "AvcAwFA7mBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3031
                                    }
                                }
                                "AvcAwFBonBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AvcAwFBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        3814
                                    }
                                }
                                "AvcAxGAxWAxjBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                    }
                                }
                                "AvcAxGAxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvcAxWAxjBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3077
                                        3814
                                    }
                                }
                                "AvcAxWA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3171
                                    }
                                }
                                "AvcAxWBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AwFAxGAxWAxjBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        6701
                                    }
                                }
                                "AwFAxGAxWAxjBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6698
                                        3814
                                    }
                                }
                                "AwFAxGAxWA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3036
                                        6701
                                    }
                                }
                                "AwFAxGAxWA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        6694
                                        3036
                                    }
                                }
                                "AwFAxGAxWBomBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3814
                                        3171
                                    }
                                }
                                "AwFAxGAxWBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                    }
                                }
                                "AwFAxGAxWBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AwFAxGAxWBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AwFAxGAxWBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWAxjA7mBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAxWAxjA7mBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAxWAxjBokBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWAxjBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3033
                                        6698
                                    }
                                }
                                "AwFAxWAxjBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        6701
                                    }
                                }
                                "AwFAxWAxjBopBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWAxjBopBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        6698
                                    }
                                }
                                "AwFAxWAxjBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        6701
                                    }
                                }
                                "AwFAxWAxjBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3814
                                        3142
                                    }
                                }
                                "AwFAxWAxjBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3036
                                        3814
                                    }
                                }
                                "AwFAxWA7mBonBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWA7mBonBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3036
                                    }
                                }
                                "AwFAxWA7mBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3033
                                    }
                                }
                                "AwFAxWA7mBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3033
                                    }
                                }
                                "AwFAxWA7mBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3033
                                    }
                                }
                                "AwFAxWA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        3036
                                    }
                                }
                                "AwFAxWBoUBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAxWBokBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBomBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AwFAxWBomBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AwFAxWBomBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                    }
                                }
                                "AwFAxWBonBopBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAxWBonBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3033
                                    }
                                }
                                "AwFAxWBonBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3033
                                    }
                                }
                                "AwFAxWBonBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6698
                                        3171
                                        6694
                                    }
                                }
                                "AwFAxWBopBoqBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwFAxWBopBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                    }
                                }
                                "AwFAxWBoqBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3171
                                        3814
                                    }
                                }
                                "AxGAxWAxjA7mBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AxWAxjA7mBorBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 107
                mMapID: u32 = 11
                mModeNameStringId: hash = "CLASSIC"
                mPosition: hash = "Top"
                mIsDefaultPosition: bool = true
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1055
                                        2003
                                        1054
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                }
                UpgradeChoices: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3077"
                    "Items/3074"
                    "Items/6692"
                    "Items/3047"
                    "Items/6701"
                    "Items/3158"
                    "Items/3036"
                    "Items/3071"
                    "Items/6698"
                    "Items/6699"
                    "Items/3111"
                    "Items/3814"
                    "Items/3009"
                    "Items/3031"
                    "Items/3174"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6692
                                        3047
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6692
                                        3074
                                    }
                                }
                                "Av/" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                    }
                                }
                                "AwC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3158
                                        3047
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        3047
                                        6698
                                    }
                                }
                                "Awc" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3020
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6692
                                    }
                                }
                                "AxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3077
                                    }
                                }
                                "BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                    }
                                }
                                "BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "Bok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3077
                                        3158
                                    }
                                }
                                "Bop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                    }
                                }
                                "Bor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3077
                                        3009
                                    }
                                }
                                "Bot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3158
                                        3047
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AvBBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AvnAwC" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        6701
                                    }
                                }
                                "AvnAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AvnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3071
                                        6701
                                    }
                                }
                                "AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3158
                                        3009
                                    }
                                }
                                "AwCAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        6692
                                    }
                                }
                                "AwCBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                                "AwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        3158
                                        3047
                                    }
                                }
                                "AwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3047
                                        6701
                                    }
                                }
                                "AwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3074
                                    }
                                }
                                "AwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        6699
                                        6701
                                    }
                                }
                                "AxWBop" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "AxWBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        3814
                                        6692
                                    }
                                }
                                "AvBAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AvnAv/AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AvnAv/Bok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                        3174
                                    }
                                }
                                "AvnAwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3071
                                        6692
                                        6701
                                    }
                                }
                                "AvnAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AvnAwFBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        6701
                                        6699
                                    }
                                }
                                "Av/AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3047
                                    }
                                }
                                "AwCAwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                        3071
                                        6701
                                    }
                                }
                                "AwCAwFAxW" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                        6692
                                        6697
                                    }
                                }
                                "AwCAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3047
                                        3158
                                        3111
                                    }
                                }
                                "AwCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                        3009
                                        3047
                                    }
                                }
                                "AwFAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFAxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                        6698
                                    }
                                }
                                "AwFAxWBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6701
                                    }
                                }
                                "AwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3074
                                    }
                                }
                                "AwFBoqBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3158
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwCAwFA7m" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                        3170
                                    }
                                }
                                "AvBAwCAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3071
                                    }
                                }
                                "AvBAwCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3170
                                        3036
                                        3814
                                    }
                                }
                                "AvnAv/AwCAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3174
                                        6333
                                        6692
                                    }
                                }
                                "AvnAwCAwFBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3174
                                        3071
                                        3033
                                    }
                                }
                                "AvnAwCAwFBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3174
                                        3036
                                        3814
                                    }
                                }
                                "AvnAwFBokBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3174
                                    }
                                }
                                "Av/AwCAwFAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3173
                                    }
                                }
                                "AwCAwFAwnBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3173
                                        6701
                                    }
                                }
                                "AwCAwFAxWBok" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        6701
                                        3071
                                    }
                                }
                                "AwCAwFAxWBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                        3036
                                        3814
                                    }
                                }
                                "AwFAxWBokBoq" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3171
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AvBAwCAwFAxiBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3814
                                    }
                                }
                                "AvnAv/AwCAwFAxm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6692
                                    }
                                }
                                "AvnAwCAwFAxmBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                                "AwCAwFAxWAxjBot" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3036
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    0x79fd0c7a = ChampionRuneRecommendationsContext {}
    0x9ac98f63 = JunglePathRecommendation {
        OrderJunglePath: list[pointer] = {
            TakeCamp {
                Camp: u8 = 4
            }
            TakeCamp {
                Camp: u8 = 5
            }
            TakeCamp {
                Camp: u8 = 3
            }
            TerminatePath {}
        }
        ChaosJunglePath: list[pointer] = {
            TakeCamp {
                Camp: u8 = 10
            }
            TakeCamp {
                Camp: u8 = 11
            }
            TakeCamp {
                Camp: u8 = 9
            }
            TakeCamp {
                Camp: u8 = 8
            }
            TakeCamp {
                Camp: u8 = 6
            }
            TakeCamp {
                Camp: u8 = 7
            }
            TerminatePath {}
        }
    }
    "Characters/Rengar/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
