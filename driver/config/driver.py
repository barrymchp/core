# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

################################################################################
#### Business Logic ####
################################################################################
def genDriverHeaderRootFile(symbol, event):
    symbol.setEnabled(event["value"])

def genDriverHeaderCommonFile(symbol, event):
    symbol.setEnabled(event["value"])

############################################################################
#### Code Generation ####
############################################################################
genDriverCommonFiles = harmonyCoreComponent.createBooleanSymbol("ENABLE_DRV_COMMON", None)
genDriverCommonFiles.setLabel("Generate Harmony Driver Common Files")
genDriverCommonFiles.setVisible(False)
genDriverCommonFiles.setDefaultValue(False)

driverHeaderRootFile = harmonyCoreComponent.createFileSymbol("DRIVER_ROOT", None)
driverHeaderRootFile.setSourcePath("driver/driver.h")
driverHeaderRootFile.setOutputName("driver.h")
driverHeaderRootFile.setDestPath("driver/")
driverHeaderRootFile.setProjectPath("config/" + configName + "/driver/")
driverHeaderRootFile.setType("HEADER")
driverHeaderRootFile.setOverwrite(True)
driverHeaderRootFile.setEnabled(False)
driverHeaderRootFile.setDependencies(genDriverHeaderRootFile, ["ENABLE_DRV_COMMON"])

driverHeaderCommonFile = harmonyCoreComponent.createFileSymbol("DRIVER_COMMON", None)
driverHeaderCommonFile.setSourcePath("driver/driver_common.h")
driverHeaderCommonFile.setOutputName("driver_common.h")
driverHeaderCommonFile.setDestPath("driver/")
driverHeaderCommonFile.setProjectPath("config/" + configName + "/driver/")
driverHeaderCommonFile.setType("HEADER")
driverHeaderCommonFile.setOverwrite(True)
driverHeaderCommonFile.setEnabled(False)
driverHeaderCommonFile.setDependencies(genDriverHeaderCommonFile, ["ENABLE_DRV_COMMON"])
