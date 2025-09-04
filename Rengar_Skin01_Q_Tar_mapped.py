"Shared/Particles/Rengar_Skin01_Q_Tar" = VfxSystemDefinitionData {
    complexEmitterDefinitionData: list[pointer] = {
        VfxEmitterDefinitionData {
            rate: embed = ValueFloat { constantValue: f32 = 80 }
            particleLifetime: embed = ValueFloat { constantValue: f32 = 0.75 }
            particleLinger: option[f32] = { 10.75 }
            lifetime: option[f32] = { 0.15 }
            emitterName: string = "SlashBase_Hunter"
            shape: embed = VfxShape {
                birthTranslation: embed = ValueVector3 { constantValue: vec3 = { 0, 50, 0 } }
            }
            0x4ffce322: pointer = 0xb13097f0 { scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291 }
            primitive: pointer = VfxPrimitiveMesh {
                mMesh: embed = VfxMeshDefinitionData {
                    mSimpleMeshName: string = "NewFXs/Rengar_Skin01_Z_WeaponTrail.sco"
                }
            }
            blendMode: u8 = 1
            color: embed = ValueColor {
                dynamics: pointer = VfxAnimatedColorVariableData {
                    times: list[f32] = { 0, 0.5, 1 }
                    values: list[vec4] = {
                        { 1, 1, 1, 1 },
                        { 1, 1, 1, 1 },
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
                            keyTimes: list[f32] = { 0, 1 }
                            keyValues: list[f32] = { 1, -1 }
                        }
                        VfxProbabilityTableData {}
                    }
                    times: list[f32] = { 0 }
                    values: list[vec3] = { { 180, 90, -90 } }
                }
            }
            birthScale0: embed = ValueVector3 {
                constantValue: vec3 = { 300, 50, 100 }
                dynamics: pointer = VfxAnimatedVector3fVariableData {
                    probabilityTables: list[pointer] = {
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.5, 1.5 } }
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.5, 1.5 } }
                        VfxProbabilityTableData {}
                    }
                    times: list[f32] = { 0 }
                    values: list[vec3] = { { 300, 50, 100 } }
                }
            }
            scale0: embed = ValueVector3 { constantValue: vec3 = { 2, 2, 1 } }
            texture: string = "NewFXs/Rengar_Skin01_Z_WeaponTrail.dds"
            numFrames: u16 = 4
            startFrame: u16 = 1
            texDiv: vec2 = { 4, 1 }
            0xbc022424: pointer = 0x7f70a2b2 { orientation: u8 = 1 }
            birthUvScrollRate: embed = ValueVector2 { constantValue: vec2 = { 0, -1.5 } }
        }
        VfxEmitterDefinitionData {
            rate: embed = ValueFloat { constantValue: f32 = 80 }
            particleLifetime: embed = ValueFloat { constantValue: f32 = 0.75 }
            particleLinger: option[f32] = { 10.75 }
            lifetime: option[f32] = { 0.15 }
            emitterName: string = "SlashAdd_Hunter"
            shape: embed = VfxShape {
                birthTranslation: embed = ValueVector3 { constantValue: vec3 = { 0, 50, 0 } }
            }
            0x4ffce322: pointer = 0xb13097f0 { scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291 }
            primitive: pointer = VfxPrimitiveMesh {
                mMesh: embed = VfxMeshDefinitionData {
                    mSimpleMeshName: string = "NewFXs/Rengar_Skin01_Z_WeaponTrail.sco"
                }
            }
            blendMode: u8 = 4
            color: embed = ValueColor {
                dynamics: pointer = VfxAnimatedColorVariableData {
                    times: list[f32] = { 0, 0.5, 1 }
                    values: list[vec4] = {
                        { 1, 1, 1, 1 },
                        { 1, 1, 1, 1 },
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
                            keyTimes: list[f32] = { 0, 1 }
                            keyValues: list[f32] = { 1, -1 }
                        }
                        VfxProbabilityTableData {}
                    }
                    times: list[f32] = { 0 }
                    values: list[vec3] = { { 180, 90, -90 } }
                }
            }
            birthScale0: embed = ValueVector3 { constantValue: vec3 = { 300, 50, 100 } }
            scale0: embed = ValueVector3 { constantValue: vec3 = { 2, 2, 1 } }
            texture: string = "NewFXs/Rengar_Skin01_Z_WeaponTrail.dds"
            numFrames: u16 = 4
            startFrame: u16 = 1
            texDiv: vec2 = { 4, 1 }
            0xbc022424: pointer = 0x7f70a2b2 { orientation: u8 = 1 }
            birthUvScrollRate: embed = ValueVector2 { constantValue: vec2 = { 0, -1.5 } }
        }
    }
    simpleEmitterDefinitionData: list[pointer] = {
        VfxEmitterDefinitionData {
            rate: embed = ValueFloat { constantValue: f32 = 1300 }
            particleLifetime: embed = ValueFloat {
                constantValue: f32 = 1
                dynamics: pointer = VfxAnimatedFloatVariableData {
                    probabilityTables: list[pointer] = {
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.5, 1 } }
                    }
                    times: list[f32] = { 0 }
                    values: list[f32] = { 1 }
                }
            }
            particleLinger: option[f32] = { 10 }
            lifetime: option[f32] = { 0.15000000596046448 }
            emitterName: string = "blood_01"
            birthVelocity: embed = ValueVector3 {
                constantValue: vec3 = { 0, 500, 0 }
                dynamics: pointer = VfxAnimatedVector3fVariableData {
                    probabilityTables: list[pointer] = {
                        VfxProbabilityTableData {}
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.4, 1.5 } }
                        VfxProbabilityTableData {}
                    }
                    times: list[f32] = { 0 }
                    values: list[vec3] = { { 0, 500, 0 } }
                }
            }
            birthDrag: embed = ValueVector3 { constantValue: vec3 = { 1, 2, 1 } }
            shape: embed = VfxShape {
                birthTranslation: embed = ValueVector3 { constantValue: vec3 = { 0, 20, 0 } }
                emitRotationAngles: list[embed] = {
                    ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0, 10 } }
                            }
                            times: list[f32] = { 0 }
                            values: list[f32] = { 1 }
                        }
                    }
                    ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0, 360 } }
                            }
                            times: list[f32] = { 0 }
                            values: list[f32] = { 1 }
                        }
                    }
                }
                emitRotationAxes: list[vec3] = {
                    { 0, 0, 1.00000012 }
                    { 0, 1.00000012, 0 }
                }
            }
            0x4ffce322: pointer = 0xb13097f0 { scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291 }
            particleColorTexture: string = "NewFXs/Rengar_Skin01_Z_Blood_RGBA.dds"
            blendMode: u8 = 1
            meshRenderFlags: u8 = 0
            colorLookUpTypeY: u8 = 3
            isDirectionOriented: flag = true
            texture: string = "NewFXs/Rengar_Skin01_Z_Blood.dds"
            frameRate: f32 = 16
            numFrames: u16 = 16
            texDiv: vec2 = { 4, 4 }
            0xbc022424: pointer = 0x7f70a2b2 {
                birthScale: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.4, 1.2 } }
                        }
                        times: list[f32] = { 0, 0.5, 1 }
                        values: list[f32] = { null, null, null }
                    }
                }
                particleBind: vec2 = { 0, 0 }
            }
        }
        VfxEmitterDefinitionData {
            rate: embed = ValueFloat { constantValue: f32 = 450 }
            particleLifetime: embed = ValueFloat {
                constantValue: f32 = 1
                dynamics: pointer = VfxAnimatedFloatVariableData {
                    probabilityTables: list[pointer] = {
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.5, 1 } }
                    }
                    times: list[f32] = { 0 }
                    values: list[f32] = { 1 }
                }
            }
            particleLinger: option[f32] = { 10 }
            lifetime: option[f32] = { 0.3 }
            emitterLinger: option[f32] = { -1 }
            emitterName: string = "blood_02"
            birthVelocity: embed = ValueVector3 {
                constantValue: vec3 = { 0, 100, 0 }
                dynamics: pointer = VfxAnimatedVector3fVariableData {
                    probabilityTables: list[pointer] = {
                        VfxProbabilityTableData {}
                        VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.4, 2 } }
                        VfxProbabilityTableData {}
                    }
                    times: list[f32] = { 0 }
                    values: list[vec3] = { { 0, 100, 0 } }
                }
            }
            birthDrag: embed = ValueVector3 { constantValue: vec3 = { 1, 1, 1 } }
            shape: embed = VfxShape {
                birthTranslation: embed = ValueVector3 { constantValue: vec3 = { 0, 20, 0 } }
                emitRotationAngles: list[embed] = {
                    ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0, 10 } }
                            }
                            times: list[f32] = { 0 }
                            values: list[f32] = { 1 }
                        }
                    }
                    ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0, 360 } }
                            }
                            times: list[f32] = { 0 }
                            values: list[f32] = { 1 }
                        }
                    }
                }
                emitRotationAxes: list[vec3] = {
                    { 0, 0, 1.00000012 }
                    { 0, 1.00000012, 0 }
                }
            }
            0x4ffce322: pointer = 0xb13097f0 { scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291 }
            particleColorTexture: string = "NewFXs/Rengar_Skin01_Z_Blood_RGBA.dds"
            blendMode: u8 = 1
            meshRenderFlags: u8 = 0
            colorLookUpTypeY: u8 = 3
            isDirectionOriented: flag = true
            texture: string = "NewFXs/Rengar_Skin01_Z_Blood.dds"
            frameRate: f32 = 16
            numFrames: u16 = 16
            texDiv: vec2 = { 4, 4 }
            0xbc022424: pointer = 0x7f70a2b2 {
                birthScale: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData { keyTimes: list[f32] = { 0, 1 } keyValues: list[f32] = { 0.4, 1.2 } }
                        }
                        times: list[f32] = { 0, 0.5, 1 }
                        values: list[f32] = { null, null, null }
                    }
                }
                particleBind: vec2 = { 1, 1 }
            }
        }
    }
    particleName: string = "Rengar_Skin01_Q_Tar"
    particlePath: string = "Shared/Particles/Rengar_Skin01_Q_Tar"
    flags: u16 = 198
}