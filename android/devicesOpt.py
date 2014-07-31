#encoding: utf-8
import commands

def deviceName():

    #adb devices
    #adb commands path
    adbCommand = '/Users/rensirui/android/adt-bundle-mac-x86_64-20131030/sdk/platform-tools/adb'
    commandTogetPhoneNum = adbCommand + ' devices'
    adbOutput = commands.getoutput(commandTogetPhoneNum)

    return adbOutput[adbOutput.index('\n') + 1: adbOutput.index('\t')]
